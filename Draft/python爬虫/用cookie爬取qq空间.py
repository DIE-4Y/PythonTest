import urllib.request
import json

base_url = 'https://user.qzone.qq.com/3314023551/infocenter'

"""由：开头的屏蔽 包含encoding的屏蔽"""
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': '3314023551_todaycount=0; 3314023551_totalcount=139; RK=v1u9U6W5s1; ptcz=b1f61e56517049c6c528dcc93b873deecc6d669f1fc08055a89db75df1987cbe; pgv_pvid=7343921848; qq_domain_video_guid_verify=c104418e24630ea8; o_cookie=3314023551; _qimei_fingerprint=28e27f13e024b4e72ed41740c05847af; _qimei_q36=; _qimei_h38=2db817bc60ee9037ba5f6e1c0200000451791c; eas_sid=T1Z7s0k5s8i420P8Z3a9H4Z076; uin=o3314023551; skey=@Kx39nJSPw; p_uin=o3314023551; pt4_token=oQifkp3GPICCFYE56by4PnaWE-i3UH*TvKmZ04gs9u8_; p_skey=rbLiCz2ZPCbPSzTMd1n0znFdBFEd6ztm1uVZm-WtzmA_; Loading=Yes; qz_screen=1536x864; pgv_info=ssid=s9306733113; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0',
    'dnt': '1',
    'if-modified-since': 'Fri, 09 Aug 2024 06:11:49 GMT',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 请求对象定制
request = urllib.request.Request(url=base_url, headers=headers)

# 模拟浏览器发送请求
response = urllib.request.urlopen(request)
print(type(response))
content = response.read().decode('utf-8')

# 下载数据
# print(content)
# print(type(content))

with open('QQ_space.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
