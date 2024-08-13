import urllib.request
import json
import urllib.parse

base_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'carve',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '493030.222935',
    'token': 'b89a2a60db14a303276525d842bb7d29',
    'domain': 'common',
    'ts': '1723107494591'
}

# Post请求参数必须编码 然后调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制
headers = {
    'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br, zstd', # 这句必须注释 这个是用于标识编码格式
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'acs-token': '1723100409001_1723107494592_oLzim9UmM+lRtZzcN69RDU8Xqte2ePJ3LgUVxwxbDRshLqK3FZqGfyl7tPbzILrYAMFbmw7kQx2ztL0qYJEnznGots5kuxuNqAWB1Kf5b0mi/h3QuYwFTYtvDFScQga+3YIlD+XYr86GRWBRfgV1+26RsGvtQwR2lngKMHkHSgbsX4XpUzuEHo2HfmLGoLVMcFQpQcrXaJD6V0N5k7yej71u+vR9woW5tF0SSOkD8c/mHszlEkvoLcaXRStn+3ZcxsdJT9E5fw1Uij1o/L6EfgMFSkl6zO4/Nq/WQ0xOh8r+N2X3lxXygQ3VktPK0HA1aieHaZB7G35KNNDD3jKUvhWcN2N4c478LRefRj6OXfAY0hHXqVOQI2IfRXBFYDgSjAxEumUXSsPnvvsHbcetKWKPXxAWPNQHNbyEBu1/VIPn6BD281Gxl1bQ9BDcBOANFBWiv9xgxBXG9UVtx/NgDyX3F09wh5BHc9jOK5h9xddMUlkQvRkxdacrxHa2jSIp',
    'connection': 'keep-alive',
    'content-length': '153',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    """cookie是这个百度翻译最需要的内容 没有就无法爬取"""
    'cookie': 'BAIDUID=F5AB37725B9ECA93D4682ED2037863F9:FG=1; BIDUPSID=F5AB37725B9ECA93D4682ED2037863F9; PSTM=1694859083; BDUSS=1Fbkk2bkowaVB6ekZBN3o3bTk4d2EwakxtcFRxSUtyV2hveDRHTk94NmtLSEJtRVFBQUFBJCQAAAAAAQAAAAEAAABf07k6xONESUXguAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKSbSGakm0hmbk; BDUSS_BFESS=1Fbkk2bkowaVB6ekZBN3o3bTk4d2EwakxtcFRxSUtyV2hveDRHTk94NmtLSEJtRVFBQUFBJCQAAAAAAQAAAAEAAABf07k6xONESUXguAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKSbSGakm0hmbk; BAIDUID_BFESS=F5AB37725B9ECA93D4682ED2037863F9:FG=1; H_PS_PSSID=60449_60523_60568; ZFY=X6:BRo1s2z5LLgdAFuYiYAeaL186uKwq5s368DiDCnwY:C; smallFlowVersion=old; RT="z=1&dm=baidu.com&si=2e26c44a-b317-4c69-a27e-adb45c112155&ss=lzl1o4rx&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=htww3&ul=18tu&hd=1933"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1723107482; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1723107482; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1',
    'dnt': '1',
    'host': 'fanyi.baidu.com',
    'origin': 'https://fanyi.baidu.com',
    'referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}
req = urllib.request.Request(url=base_url, data=data, headers=headers)

# 发送请求 对内容解码
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')

obj = json.loads(content)
print(obj)
