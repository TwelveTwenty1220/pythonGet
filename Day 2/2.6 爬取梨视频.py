import requests
import re


def getVideo(url):


    obj=re.compile(r'contId=(?P<id>.*?)&',re.S)

    contId=obj.findall(url)[0]

    headers={'Referer':f'https://www.pearvideo.com/video_{contId}'}

    resp=requests.get(url=url,headers=headers)
    systemTime=resp.json()['systemTime']
    srcUrl=resp.json()['videoInfo']['videos']['srcUrl']

    srcUrl=srcUrl.replace(systemTime,f'cont-{contId}')

    content=requests.get(srcUrl).content

    with open('viedo.mp4','wb') as f :
        f.write(content)


if __name__=='__main__':
    print('开始爬取')
    url= 'https://www.pearvideo.com/videoStatus.jsp?contId=1194846&mrd=0.620560995840675'
    getVideo(url)
    print('爬取结束')