import urllib.request
import json
import jsonpath

url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1723372670080_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v': '2.5.14',
    'cookie': 'isg=BOrqQypyeB0EMfTxN8VwKLcsO1CMW261iWiReXSisT3Ip4phXOoBxX7ZN9O7V-ZN',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://www.taopiaopiao.com/?tbpm=3',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'x-requested-with': 'XMLHttpRequest'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]

with open('jsonpath基本使用.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

# json读取文件不能直接写文件名 会出错 须用open打开文件
obj = json.load(open('jsonpath基本使用.json', 'r', encoding='utf-8'))
region_list = jsonpath.jsonpath(obj, '$..regionName')

print(region_list)
