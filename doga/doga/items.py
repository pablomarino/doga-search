# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DogaItem(scrapy.Item):
    document_number = scrapy.Field()
    document_page = scrapy.Field()
    document_url = scrapy.Field()
    publication_week_day = scrapy.Field()
    publication_day = scrapy.Field()
    publication_month = scrapy.Field()
    publication_year = scrapy.Field()
    announcement_section = scrapy.Field()
    announcement_subsection = scrapy.Field()
    announcement_issuer = scrapy.Field()
    announcement_summary = scrapy.Field()
    announcement_content = scrapy.Field()
    #announcement_signature = scrapy.Field()
    pass
