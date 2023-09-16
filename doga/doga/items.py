# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DogaItem(scrapy.Item):
    # numero
    numero = scrapy.Field()
    # dia_semana
    dia_semana = scrapy.Field()
    # dia
    dia = scrapy.Field()
    # mes
    mes = scrapy.Field()
    # ano
    ano = scrapy.Field()
    # ligazons a seccions
    ligazons_seccions = scrapy.Field()
    # las posiciones de este array corresponden a:
    #   0 disposicions_xerais
    #   1 autoridades_persoal
    #   2 autoridades_persoal_cesamentos
    #   3 autoridades_persoal_nomeamentos
    #   4 autoridades_persoal_substitucions
    #   5 outras_disposicions
    #   6 oposicions_concursos
    #   7 administracion_xustiza
    #   8 anuncios
    #   9 anuncios_administracion_autonomica
    #   10 anuncios_administracion_local
    #   11 anuncios_outros

    # Ligazons ó contido de cada sección
    ligazons_contido = scrapy.Field()



    pass
