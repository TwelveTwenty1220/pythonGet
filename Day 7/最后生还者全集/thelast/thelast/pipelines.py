# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.files import FilesPipeline
import scrapy
import os

class Merge_Pipeline:
    def process_item(self, item, spider):
        name = item['name'].split(' ')[-1][4:6]
        print(name)
        if os.path.exists(f'video/ts/猎魔人/{name}index.txt'):
            pass
        else:
            print(f'开始合并{item["name"]}')
            with open(f'video/m3u8/{item["name"]}mixed.txt','r',encoding='utf-8') as f:
                list=[]
                for line in f:
                    if line.startswith('#'):
                        continue
                    else:
                        line=line.strip().split('/')[-1]
                        list.append(line)

            with open(f'video/ts/猎魔人/{name}index.txt','w') as f:
                for i in list:
                    content=f"file '{i}'"
                    f.write(content+'\n')

            print(f'合并完毕{item["name"]}')

        # print(os.getcwd())
        # os.chdir(f'video/ts')
        # if os.path.exists('final'):
        #     os.chdir(f'{item["name"]}')
        #     command = f"ffmpeg -f concat -safe 0 -i index.txt -c copy ..\\final\\{item['name'].split(' ')[-1]}.mp4"
        #     os.system(command)
        # else:
        #     os.mkdir('final')
        #     os.chdir(f'{item["name"]}')
        #     command = f"ffmpeg -f concat -safe 0 -i index.txt -c copy ..\\final\\{item['name'].split(' '[-1])}.mp4"
        #     os.system(command)
        return item


class Download_ts_Pipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        self.video_name=item['name']
        yield scrapy.Request(url=item['ts_url'],dont_filter=True)


    def file_path(self, request, response=None, info=None, *, item=None):
        if os.path.exists(f'video/ts/猎魔人'):
            name=request.url.split('/')[-1]
            return f'ts/猎魔人/{name}'
        else:
            os.mkdir(f'video/ts/猎魔人')
            name = request.url.split('/')[-1]
            return f'ts/猎魔人/{name}'


    def item_completed(self, results, item, info):
        print(results[0])
        return item






