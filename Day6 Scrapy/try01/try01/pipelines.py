# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class Try01Pipeline:


    def open_spider(self,spider):
        self.f=open('./4399下游戏.csv', 'a', encoding='utf-8')

    def close_spider(self,spider):
        if self.f:
            self.f.close()

    def process_item(self, item, spider):

        self.f.write(f'name: {item["name"][0]} categroy: {item["category"][0]} time: {item["time"]}'+'\n')

        return item

class MyPepeLine:
    def process_item(self,item,spider):
        item['love']='如果，可惜没有如果'
        return item