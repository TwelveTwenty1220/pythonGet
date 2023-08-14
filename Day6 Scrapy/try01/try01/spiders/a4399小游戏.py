import scrapy
from try01.items import Try01Item



class A4399小游戏Spider(scrapy.Spider):
    name = "4399小游戏"
    allowed_domains = ["4399.com"]
    start_urls = ["http://www.4399.com/flash/"]


    def parse(self, response,**kwargs):
        #可以直接提取数据
        #获取所有的游戏名字
        li_list=response.xpath('//*[@id="skinbody"]/div[8]/ul/li')
        for li in li_list:
                name=li.xpath('./a/b/text()').extract_first()
                category=li.xpath('./em[1]/a/text()').extract_first()
                time=li.xpath('./em[2]/text()').extract_first()
                # print(name+'\n'+category+'\n'+time+'\n'+'=========='+'\n')

                item=Try01Item()

                item['name']=name,
                item['category']=category,
                item['time']=time

                yield  item




