import scrapy

from ..items import PublicationItem
import re, json, datetime
from w3lib.html import remove_tags

class BoeSpiderSpider(scrapy.Spider):
    name = "boe_spider"
    allowed_domains = ["boe.es"]
    start_urls = None


    def start_requests(cls):
        # Cargo las urls iniciales de un fichero
        file_path = "data/BOE_start_urls.json"
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

        h3_elements = response.css('div.sumario h3')

        for h3_element in h3_elements:
            # Obtén el texto del elemento <h3>
            h3_text = remove_tags(h3_element.extract().strip())

            # Obtén los elementos <h4> y <h5> dentro del div.sumario actual
            headers = h3_element.xpath('following-sibling::h4 | following-sibling::h5')

            for header in headers:
                # Extrae el texto del elemento actual
                h5_text = remove_tags(header.extract().strip())

                # Verifica si es un elemento <h5>
                if header.css('h5'):
                    # Extrae el texto del elemento <h4> anterior usando selector CSS
                    h4_text = h3_element.xpath('preceding-sibling::h4[1]/text()').extract_first()

                    # Imprime la cadena deseada
                    if h4_text:
                        current_text= None
                        url = None

                        ul_elements = header.xpath('following-sibling::ul')
                        for ul_element in ul_elements:
                            # Extrae el contenido de los elementos <li> con clase 'dispo'
                            li_dispo_elements = ul_element.css('li.dispo')

                            for li_dispo_element in li_dispo_elements:
                                #print(li_dispo_element)
                                # Extrae el contenido de los elementos <p> y <div> con clase 'enlacesDoc'
                                current_text = li_dispo_element.css('p::text').extract_first()
                                url_pdf = 'https://www.boe.es'+li_dispo_element.css('div.enlacesDoc ul li.puntoPDF a::attr(href)').extract_first()
                                url_html = 'https://www.boe.es' + li_dispo_element.css(
                                    'div.enlacesDoc ul li.puntoHTML a::attr(href)').extract_first()
                                #print(f'{h3_text}/{h4_text}/{h5_text}>{current_text}|{url_pdf}')

                                item = PublicationItem()
                                item['publication_id'] = "BOE"
                                item['document_number'] = response.css('span.no_partir::text').get().split("-")[-1]
                                fecha_wo_format = response.css('li.destino::text').get().split(" - ")[0].split("/")
                                item['publication_date'] = f'{fecha_wo_format[2]}-{fecha_wo_format[1]}-{fecha_wo_format[0]}'
                                item['document_url'] = url_pdf
                                item['announcement_section'] = re.sub(r"^(?:I{1,3}|IV|V|VI{1,3}|IX|X)(?:\. )", "", h3_text)
                                item['announcement_subsection'] = h5_text
                                item['announcement_issuer'] = h4_text
                                item['announcement_summary'] = current_text
                                date_today = datetime.date.today()
                                date_today_fmt = date_today.strftime("%Y-%m-%d")
                                item['retrieval_date'] = date_today_fmt
                                # Recojo el contenido y numero de página en otra url
                                yield scrapy.Request(url=url_html, callback=cls.parseDateContent, cb_kwargs={"item":item})


    def parseDateContent(cls, response, item):

        item['document_page'] = remove_tags(" ".join(response.css('div.metadatos dl dd').extract())).split(', páginas ')[1].split(" ")[0]
        item['announcement_content'] = re.sub(r'\s+', ' ', remove_tags(" ".join(response.css('div#textoxslt').extract())))
        yield item


