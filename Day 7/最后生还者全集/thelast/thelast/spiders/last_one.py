
import scrapy
import re
import os
from thelast.items import ThelastItem


class LastOneSpider(scrapy.Spider):
    name = "last_one"
    allowed_domains = ["mjw21.com","vip.lz-cdn14.com"]
    start_urls = ["https://mjw21.com/dp/NTIxMy0xLTA=.html"]
    temp=''

    def parse(self, resp,**kwargs):
        obj=re.compile(r'var vid="(?P<url>.*?)"')
        m3u8_url=obj.search(resp.xpath('/html/body/section/script[1]/text()').extract_first()).group('url')
        self.name_video=resp.xpath('/html/body/section/div/div/div[2]/h4/a/text()').extract_first()\
             +resp.xpath('/html/body/section/div/div/div[2]/h4/span/text()').extract_first()
        yield scrapy.Request(url=m3u8_url,method='get',callback=self.save_m3u8,dont_filter=True)


        with open('G:\Day 7\最后生还者全集\\thelast\\video\\m3u8\\url.txt','r',encoding='utf-8') as f:
            for line in f:
                yield scrapy.Request(url=line.strip(),callback=self.parse,dont_filter=True)


    def save_m3u8(self,resp,**kwargs):
        if os.path.exists(f'video/m3u8/{self.name_video}.txt'):
            pass
        else:
            with open(f'video/m3u8/{self.name_video}.txt','wb') as f:
                f.write(resp.body)
            print(f'{self.name_video} m3u8下载完毕')

            with open(f'video/m3u8/list.txt','a') as f:
                f.write(self.name_video+'\n')

        with open(f'video/m3u8/{self.name_video}.txt', 'r', encoding='utf-8')as f:
            for line in f:
                if line.startswith('#'):
                    continue
                else:
                    url = line.strip()
                    print(resp.urljoin(url))
                    yield scrapy.Request(url=resp.urljoin(url),method='get',callback=self.save_mixed,dont_filter=True)

    def save_mixed(self,resp):
        item=ThelastItem()
        if os.path.exists(f'video/m3u8/{self.name_video}mixed.txt'):
            pass
        else:
            with open(f'video/m3u8/{self.name_video}mixed.txt','wb')as f:
                f.write(resp.body)
            print(f'{self.name_video}mixed下载完毕')
        with open(f'video/m3u8/{self.name_video}mixed.txt','r',encoding='utf-8') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                else:
                    url=line.strip()
                    item['name']=self.name_video
                    item['ts_url']=resp.urljoin(url)
                    yield item



