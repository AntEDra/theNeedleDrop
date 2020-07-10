# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TndreviewsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    artist = scrapy.Field()
    album = scrapy.Field()
    score = scrapy.Field()
    pass
