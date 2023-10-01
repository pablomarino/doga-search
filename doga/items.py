# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DogaItem(scrapy.Item):
    document_number = scrapy.Field()
    document_page = scrapy.Field()
    document_url = scrapy.Field()
    publication_date = scrapy.Field()
    announcement_section = scrapy.Field()
    announcement_subsection = scrapy.Field()
    announcement_issuer = scrapy.Field()
    announcement_summary = scrapy.Field()
    announcement_content = scrapy.Field()
    # anouncement_key_places =
    # anouncement_key_opo informatica, ingenieria,
    # anouncement_key_company buscar terminos S.A. S.L. S.L.U. Coop. fundacion, asociacion entidade organizacion ong
    pass
