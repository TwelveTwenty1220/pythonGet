
import scrapy
import os
class GetUrlSpider(scrapy.Spider):
    name = "get_url"
    allowed_domains = ["mjw21.com"]
    start_urls = ["https://mjw21.com/dp/NTM0NC0xLTA=.html"]
    temp=''
    def parse(self, resp,**kwargs):
        self.name_video = resp.xpath('/html/body/section/div/div/div[2]/h4/a/text()').extract_first() \
                          + resp.xpath('/html/body/section/div/div/div[2]/h4/span/text()').extract_first()
        next_url = resp.xpath('/html/body/section/div/div/div[2]/ul/li[2]/a[contains(text(),"下一集")]/@href').extract_first()
        if next_url:
            if self.temp == next_url:
                print('已经全部获得')
            else:
                with open('G:\Day 7\最后生还者全集\\thelast\\video\m3u8\\url.txt','a') as f:
                    f.write(resp.urljoin(next_url)+'\n')
                yield scrapy.Request(url=resp.urljoin(next_url),
                                     callback=self.parse, dont_filter=True)
            self.temp = next_url
        # with open('G:\Day 7\最后生还者全集\\thelast\\video\m3u8\\url.txt','r',encoding='utf-8') as f:
        #     for line in f:
        #         print(line)
