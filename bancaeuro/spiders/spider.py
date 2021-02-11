import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import BancaeuroItem
from itemloaders.processors import TakeFirst


class BancaeuroSpider(scrapy.Spider):
	name = 'bancaeuro'
	start_urls = ['http://www.bancaeuro.it/it/news/comunicati.aspx']

	def parse(self, response):
		post_links = response.xpath('//div[@class="P-link"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)


	def parse_post(self, response):
		title = response.xpath('//header[@class="Tit TitPagina"]/span/text()').get()
		description = response.xpath('//div[@class="P-cont"]/div[@class="P-box_1"]//text()[normalize-space() and not(ancestor::div[@class="P-dat"])]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="P-box_1"]/div[@class="P-dat"]/text()').get()
		if date:
			date = re.findall(r"(\d+\s[a-zA-Z]+\s\d+)", date)[0]

		item = ItemLoader(item=BancaeuroItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
