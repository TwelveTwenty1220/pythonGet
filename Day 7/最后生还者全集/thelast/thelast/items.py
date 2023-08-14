# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ThelastItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    m3u8_url= scrapy.Field()
    mixed_url=scrapy.Field()
    ts_url=scrapy.Field()

