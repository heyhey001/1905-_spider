import scrapy

from testfile.items import yi905Item

class yi905Spider(scrapy.Spider):
    name = "1905"
    #allowed_domains = ["1905.com"]
    yingku = 'http://www.1905.com/mdb/film/list/'
    start_urls = [ yingku ]
        	
    def parse(self, response):
    	film_list = response.xpath('//ul[@class="inqList pt18"]/li')
    	
    	for sel in film_list:
    		item = yi905Item()
    		item['title'] = sel.xpath('div/p[1]/a/text()').extract()

    		item['pingfen'] = sel.xpath('div/p[2]/b/text()').extract()
    	

    		item['zhuyan'] =	sel.xpath('div/p[3]/a/text()').extract()
    		

    		item['leixing'] = sel.xpath('div/p[4]/a/text()').extract()
    	

    		yield item
    	
    	new_page = response.xpath('/html/body/div/div[@class="leftArea"]/div[@id="new_page"]/a/@href')
    	if new_page:
    		url = response.urljoin(new_page[-1].extract())
    		yield scrapy.Request(url, self.parse)

    




        
        

