import scrapy
class CoroNews(scrapy.Spider):
    name = 'corona'
    start_urls = ['https://inshorts.com/en/read']
    
    def parse(self, response):
        news = response.css('.news-right-box .clickable span::text')[:5].extract()
        yield{'titletext': news}