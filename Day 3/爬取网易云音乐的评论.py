import requests
from crypto.Cipher import AES
from base64 import b64encode
import json
#要首先获得网易云加密的参数
#请求方式是Post

"""

可以得到固定的值，想要破解params和encSecKey就差那个动态的值了
bsk5p(["流泪", "强"])
'010001'
bsk5p(["爱心", "女孩", "惊恐", "大笑"])
'0CoJUm6Qyw8W8jud'


 function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length, 
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    
    h.encText=
    h.encText=b(h.encText)
    h.encSeckey=
    return h
    

window.asrsea=d             
  
var bVe7X = window.asrsea(d=JSON.stringify(i5n), e=bsk5p(["流泪", "强"]), f=bsk5p(Vx0x.md), g=bsk5p(["爱心", "女孩", "惊恐", "大笑"]))

a返回的值是随机的,所以i是随机的 i=a(16)
e g is certain
c函数没有随机数值，所以c是未被加密的,只有

"""



url='https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

i='HgRp9T81n5gDdFu2'
e='010001'
f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g='0CoJUm6Qyw8W8jud'

def get_encSecKey():
    encSecKey="b1878e90c3a5dce170b958a92f976701afa59d90c8e2eb09565f8b50e0ea0628974ec7b1681aba94336d4ec8b301ebeaa8d8857a794f5427bf2247c7316e131fbe34af431798157f042dd9cf216600d8ca6f5b8342cf40da3dda663cb3eafa3d8dd9f18d282c7e41166ff9f0da25412c34763ee3fabe423397daa2202e7e0cce"
    return encSecKey

def get_params(data):
    first=enc_params(data,g)
    enc_Text=enc_params(first,i)
    return enc_Text

    pass

def enc_params(data,key):
    iv='0102030405060708'
    #字符串转字节'utf-8'
    aes=AES.new(key=key.encode("utf-8"),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    bs=aes.encrypt(data)#加密
    #utf-8无法直接识别，所以需要新的模块
    return str(b64encode(bs),'utf-8')#变成字符串




    pass



resp=requests.post(url=url,data={
    'params':get_params(json.dumps()),#
    'encSecKey':get_encSecKey()

                                 })

print(resp.text)