import scrapy

from ..items import PublicationItem
import re, json, datetime


class DogaSpiderSpider(scrapy.Spider):
    name = "doga_spider"
    allowed_domains = ["xunta.gal"]
    start_urls = None

    def start_requests(cls):
        # Cargo las urls iniciales de un fichero
        file_path = "data/DOGA_start_urls.json"
        try:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
            # Extract the "urls" array from the loaded data
            cls.start_urls = data["urls"]
        except FileNotFoundError:
            print(f"The file '{file_path}' was not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except KeyError as e:
            print(f"JSON does not contain a 'urls' key: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        # Creo una petición para cada URL
        for url in cls.start_urls:
            yield scrapy.Request(url=url, callback=cls.parse)

    def parse(cls, response):
        base_url = "https://www.xunta.gal/diario-oficial-galicia/"
        # Obtengo los enlaces a secciones y subsecciones
        links = response.css('li.dog-toc-sumario a::attr(href)').extract()
        # Las subsecciones se distinguen por usar el caracter #ANCHOR, las elimino porque duplican los enlaces
        filtered_links = [link for link in links if not re.search(r'#', link)]
        for link in filtered_links:
            print("link")
            yield scrapy.Request(url=f'{base_url}{link}', callback=cls.parse_sections)


    def parse_sections(cls, response):
        base_url = "https://www.xunta.gal"
        content_links = response.css("div.story a::attr(href)").extract()
        for link in content_links:
            yield scrapy.Request(url=f'{base_url}{link}', callback=cls.parse_content)

    def parse_content(cls, response):
        item = PublicationItem()
        item['publication_id'] = "DOGA"
        item['document_number'] = response.css("span#DOGNumero::text").get().strip().split(". ")[1]
        item['document_page'] = response.css("span#DOGPaxina::text").get().strip().split(". ")[1]
        item['document_url'] = response.request.url

        publicacion = response.css("span#DOGData::text").get().strip().split(" de ")
        item['publication_date'] = cls._format_date(publicacion)

        # almaceno la secccion tras eliminar las cadenas de inicio I, II, III, IV...
        section=response.css("span.dog-texto-seccion::text").get()
        item['announcement_section'] = re.sub(r"^(?:I{1,3}|IV|V|VI{1,3}|IX|X)(?:\. )","",section)

        # almaceno la subsecccion tras eliminar las cadenas de inicio a),b)...
        subsection = response.css("span.dog-texto-subseccion::text").get()
        item['announcement_subsection'] = re.sub(r"^[a-z]\) ", "", subsection)

        item['announcement_issuer'] = response.css("span.dog-texto-organismo::text").get()
        item['announcement_summary'] = response.css("span.dog-texto-sumario::text").get()
        # TODO: Utilizar beautifulsoup para extraer contenido de los tags html
        # Concateno la lista de cadenas de contenido
        content = ''.join(response.css("div.story p::text").getall())
        # La almaceno eliminando caracteres \t \r \n
        item['announcement_content'] = re.sub(r'\s+', ' ', content)
        date_today = datetime.date.today()
        date_today_fmt = date_today.strftime("%Y-%m-%d")
        item['retrieval_date'] = date_today_fmt

        yield item

    def _format_date(cls, publication):
        month_traslation = {
            "xaneiro": 1,
            "febreiro": 2,
            "marzo": 3,
            "abril": 4,
            "maio": 5,
            "xuño": 6,
            "xullo": 7,
            "agosto": 8,
            "setembro": 9,
            "outubro": 10,
            "novembro": 11,
            "decembro": 12
        }
        day = int(publication[0].split(",")[1])
        month = int(month_traslation[publication[1]])
        year = int(publication[2])
        # Creo objeto datetime
        date_obj = datetime.datetime(year, month, day)


        # Formateo la fecha como ISO 8601 el formato que utiliza ES
        # return date_obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        return date_obj.strftime('%Y-%m-%d')