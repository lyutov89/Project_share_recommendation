import scrapy
from scrapy.http import HtmlResponse
from shareparser.items import ShareparserItem
from scrapy.loader import ItemLoader

class FinvizSpider(scrapy.Spider):
    name = 'finviz'
    allowed_domains = ['finviz.com']
    start_urls = ['https://finviz.com/screener.ashx?v']

    def __init__(self):
        self.start_urls = ['https://finviz.com/screener.ashx?v']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='screener_arrow']/@href").extract_first()
        yield response.follow(next_page, callback=self.parse)

        ticker_links = response.xpath("//a[@class='screener-link-primary']/@href").extract()
        for link in ticker_links:
            yield response.follow(link, callback=self.ticker_parce)

    def ticker_parce(self, response:HtmlResponse):
        ticker1 = response.xpath("//a[@id='ticker']/text()").extract()
        info_params1 = response.xpath("//td[@class='snapshot-td2']/b[1]//descendant-or-self ::*/text()").extract()
        info_features1 = response.xpath("//td[@class='snapshot-td2-cp']/text()").extract()
        info_industry1 = response.xpath("//td[@class='fullview-links']/a[@class='tab-link'][1]/text()").extract()
        yield ShareparserItem(ticker=ticker1, info_features=info_features1,
                              info_params=info_params1, info_industry=info_industry1)

