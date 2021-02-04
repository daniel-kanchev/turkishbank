import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from turkishbank.items import Article


class TurkishSpider(scrapy.Spider):
    name = 'turkish'
    allowed_domains = ['turkishbank.com']
    start_urls = ['https://www.turkishbank.com/category/blog/']

    def parse(self, response):
        links = response.xpath('//h2/a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h2[@class="entry-title fusion-post-title"]//text()').get().strip()

        content = response.xpath('//div[@class="post-content"]//text()').getall()
        content = '\n'.join(content).strip()

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()