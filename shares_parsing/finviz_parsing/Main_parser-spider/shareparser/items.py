# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShareparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    ticker = scrapy.Field()
    info_params = scrapy.Field()
    info_features = scrapy.Field()
    info_industry = scrapy.Field()
    pass
