# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


#pipe默认不生效，要手动启动,去settings启动
class TempPipeline:
    def process_item(self, item, spider):
        print(item)
        print(spider.name)
        return item
