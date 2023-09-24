import scrapy

from ..items import DogaItem
import re


class DogaSpiderSpider(scrapy.Spider):
    name = "doga_spider"
    allowed_domains = ["xunta.gal"]

    start_urls = [
        "https://www.xunta.gal/diario-oficial-galicia/mostrarContenido.do?ruta=/u01/app/oracle/shared/resources/pxdog100/doga/Publicados/2023/20230922/Secciones1_gl.html",
        "https://www.xunta.gal/diario-oficial-galicia/mostrarContenido.do?ruta=/u01/app/oracle/shared/resources/pxdog100/doga/Publicados/2023/20230921/Secciones1_gl.html",
        "https://www.xunta.gal/diario-oficial-galicia/mostrarContenido.do?ruta=/u01/app/oracle/shared/resources/pxdog100/doga/Publicados/2023/20230920/Secciones1_gl.html",
        "https://www.xunta.gal/diario-oficial-galicia/mostrarContenido.do?ruta=/u01/app/oracle/shared/resources/pxdog100/doga/Publicados/2023/20230919/Secciones1_gl.html"
    ]





    def parse(self, response):
        base_url = "https://www.xunta.gal/diario-oficial-galicia/"
        # Obtengo los enlaces a secciones y subsecciones
        links = response.css('li.dog-toc-sumario a::attr(href)').extract()
        # Las subsecciones se distinguen por usar el caracter #ANCHOR, las elimino porque duplican los enlaces
        filtered_links = [link for link in links if not re.search(r'#', link)]
        for link in filtered_links:
            print("link")
            yield scrapy.Request(url=f'{base_url}{link}', callback=self.parse_sections)


    def parse_sections(self, response):
        base_url = "https://www.xunta.gal"
        content_links = response.css("div.story a::attr(href)").extract()
        for link in content_links:
            yield scrapy.Request(url=f'{base_url}{link}', callback=self.parse_content)

    def parse_content(self, response):
        item = DogaItem()
        item['document_number'] = response.css("span#DOGNumero::text").get().strip().split(".")[1]
        item['document_page'] = response.css("span#DOGPaxina::text").get().strip().split(".")[1]
        item['document_url'] = response.request.url

        month_traslation = {
            "xaneiro": "January",
            "febreiro": "February",
            "marzo": "March",
            "abril": "April",
            "maio": "May",
            "xuño": "June",
            "xullo": "July",
            "agosto": "August",
            "setembro": "September",
            "outubro": "October",
            "novembro": "November",
            "decembro": "December"
        }
        publication = response.css("span#DOGData::text").get().strip().split(" de ")
        item['publication_day'] = publication[0].split(",")[1]
        item['publication_month'] = month_traslation[publication[1]]
        item['publication_year'] = publication[2]

        item['announcement_section'] = response.css("span.dog-texto-seccion::text").get()
        item['announcement_subsection'] = response.css("span.dog-texto-subseccion::text").get()
        item['announcement_issuer'] = response.css("span.dog-texto-organismo::text").get()
        item['announcement_summary'] = response.css("span.dog-texto-sumario::text").get()
        # Concateno la lista de cadenas de contenido
        content = ''.join(response.css("div.story p::text").getall())
        # La almaceno eliminando caracteres \t \r \n
        item['announcement_content'] =  re.sub(r'\s+', ' ', content)

        yield item