import scrapy


class GameSpider(scrapy.Spider):
    name = "game"
    allowed_domains = ["4399.com"]
    start_urls = ["http://www.4399.com/flash/"]

    def parse(self, response):
        pass



