# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Field, Item

class CrawledWebsiteItem(Item):

    domain = Field()
    url = Field()
    tor2web_url = Field()
    title = Field()
    h1 = Field()
    h2 = Field()
    server_header = Field()
    text = Field()
    date_inserted = Field()
    id = Field()
    django_ct = Field()
    django_id = Field()
    crawling_session = Field()
