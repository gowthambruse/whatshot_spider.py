import scrapy

class FormSpider2(scrapy.Spider):
    name = 'formspider'
    start_urls = ['http://www.whatshot.in/']

    def start_requests(self):
        return [scrapy.FormRequest("http://www.whatshot.in/search/index/",
                                   formdata={'city': 'bangalore', 'start': '1','limit':'11','type':'event',
                                   'bydate':'event',
                                   'parentid':'getallfeeds','mainURL':'http://www.whatshot.in/search/index'},
                                   callback=self.logged_in)]

    def logged_in(self, response):
         for quote in response.css('div.feeds-data'):
            yield scrapy.Request(url=quote.xpath('a/@href').extract()[0], callback=self.parse)
            
    def parse(self, response):
    	yield{
    		'eventTitle': response.xpath("//h1/text()").extract(),
    		'eventTime':str(response.xpath("//div[@class='venue']/text()").extract()[1]).strip(),
    		'eventLocation':response.xpath("//div[2][@class='venue']/a/text()").extract()[0],
    		}
