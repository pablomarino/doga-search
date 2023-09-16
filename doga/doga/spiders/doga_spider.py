import scrapy

from ..items  import DogaItem
from ..FechaParser import FechaParser
import datetime


class DogaSpiderSpider(scrapy.Spider):
    name = "doga_spider"
    allowed_domains = ["xunta.gal"]
    start_urls = ["https://www.xunta.gal/diario-oficial-galicia"]

    def parse(self, response):
        item = DogaItem()
        # Obtengo el Número del Diario Oficial de Galicia
        # dog_numero = response.xpath('//span[@id="DOGNumero"]/text()').extract_first()
        dog_numero = response.css('span#DOGNumero::text').getall()[0].split(" ")[1]
        item['numero'] = dog_numero
        # Obtengo la fecha FIXME: Datos de la fecha desordenados
        # dog_data = response.xpath('//span[@id="DOGData"]/text()').extract_first()
        dog_data = response.css('span#DOGData::text').getall()[0]
        item['dia_semana'], item['dia'],  item['mes'],item['ano']  = FechaParser.extract(dog_data)
        # Obtengo los enlaces a las secciones
        elementos_li = response.css('li.dog-toc-sumario')
        #   Inicializa una lista para almacenar los href o None si no se encuentran
        base_url = "https://www.xunta.gal/diario-oficial-galicia/"
        item['ligazons_seccions'] = []
        #   Itera a través de los elementos <li> encontrados
        for elemento_li in elementos_li:
            # Intenta obtener el href del enlace dentro del <li>
            href = elemento_li.css('a::attr(href)').get()
            # Si no se encuentra un enlace, agrega None a la lista
            if href is None:
                item['ligazons_seccions'].append(None)
            else:
                item['ligazons_seccions'].append(f"{base_url}{href}")
        # Obtengo los enlaces del contenido de las secciones
        # TODO: Parsear los enlaces antes de devolver el ITEM
        print(")))))))))))))))))))))))))", item)

        yield item
