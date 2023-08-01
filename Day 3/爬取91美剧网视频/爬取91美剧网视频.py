import requests
import re


# url='https://mjw21.com/dp/NDcxOC0xLTA=.html'
# resp=requests.get(url=url)
#
# result=re.compile(r'<script type="text/javascript">.*vid="(?P<vid>.*?)"',re.S).findall(resp.text)
# m3u8_url=result[0]
# print(m3u8_url)
# resp.close()

m3u8_url='https://vip.lz-cdn16.com/20230724/32539_87c2b467/2000k/hls/mixed.m3u8'
#下载m3u8文件
resp2=requests.get(m3u8_url)

with open('风骚女子.m3u8','wb') as f:
    f.write(resp2.content)

resp2.close()

#解析m3u8文件
n=1
with open('风骚女子.m3u8','r',encoding='utf-8') as f :
    url='https://vip.lz-cdn16.com/20230724/32539_87c2b467/2000k/hls/'

    for line in f :
        line=line.strip()
        if(line.startswith('#')):
            continue
        url1=url+line

        print(url1)
        #下载视频片段
        # resp3=requests.get(url1)
        # f=open(f'video2/{n}.ts','wb')
        # f.write(resp3.content)
        # f.close()
        # resp3.close()
        # n+=1
        # print('当前进度'+f'{n}')