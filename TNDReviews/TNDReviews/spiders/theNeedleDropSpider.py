"""
Created on July 6, 2020
by Anthony Drake
"""

import json
import scrapy
from scrapy.spiders import Spider
from ..items import TheneedledropItem

class needledropspider(Spider):
    name = 'theneedledrop'
    start_urls = ['https://www.theneedledrop.com/articles?category=Reviews']

    def parse(self, response):

        urls = response.xpath('//div[@class="blog-content"]/article/header/h1/a/@href').getall()

        for u in urls:
            yield scrapy.Request(response.urljoin(u), self.parse_detail)

        next_url = response.urljoin(response.xpath('//div[@class="older"]/a/@href').get())
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):

        script = response.xpath('//script[@type="application/ld+json"]/text()')[2].get()
        desc = json.loads(script)
        items = TheneedledropItem()
        items['url'] = desc['url']
        items['date'] = desc['datePublished']
        try:
            items['artist'] = desc['headline'].split('-')[0].strip()
            items['album'] = desc['headline'].split('-')[1].strip()
        finally:
            items['name'] = desc['headline']

        try:
        	items['score'] = response.xpath('//a[contains(text(),"/")]/text()').get().split('/')[0]
        except:
        	items['score'] = "N/A"


        items['tags'] = " | ".join(response.xpath('//*[@class="entry-tags"]/a/text()').getall())
        yield items
