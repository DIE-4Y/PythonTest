# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import time
import requests
import urllib
import sys
lfasr_host = 'https://raasr.xfyun.cn/v2/api'
# 请求的接口名
api_upload = '/upload'
api_get_result = '/getResult'

""" 
    长语音转文字目前应该只支持中文 英文暂未测试
    使用方式>>:
        （1）调用 w2t() 需要文件传入 文件名 ==>会自动生成一个 相同名字+".txt" 的文件
"""


class RequestApi(object):
    def __init__(self, appid, secret_key, upload_file_path):
        self.appid = appid
        self.secret_key = secret_key
        self.upload_file_path = upload_file_path
        self.ts = str(int(time.time()))
        self.signa = self.get_signa()

    def get_signa(self):
        appid = self.appid
        secret_key = self.secret_key
        m2 = hashlib.md5()
        m2.update((appid + self.ts).encode('utf-8'))
        md5 = m2.hexdigest()
        md5 = bytes(md5, encoding='utf-8')
        # 以secret_key为key, 上面的md5为msg， 使用hashlib.sha1加密结果为signa
        signa = hmac.new(secret_key.encode('utf-8'), md5, hashlib.sha1).digest()
        signa = base64.b64encode(signa)
        signa = str(signa, 'utf-8')
        return signa

    def upload(self):
        print("上传部分：")
        upload_file_path = self.upload_file_path
        file_len = os.path.getsize(upload_file_path)
        file_name = os.path.basename(upload_file_path)

        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict["fileSize"] = file_len
        param_dict["fileName"] = file_name
        param_dict["duration"] = "200"
        print("upload参数：", param_dict)
        data = open(upload_file_path, 'rb').read(file_len)

        response = requests.post(url=lfasr_host + api_upload + "?" + urllib.parse.urlencode(param_dict),
                                 headers={"Content-type": "application/json"}, data=data)
        print("upload_url:", response.request.url)
        result = json.loads(response.text)
        print("upload resp:", result)
        return result

    def get_result(self):
        uploadresp = self.upload()
        orderId = uploadresp['content']['orderId']
        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict['orderId'] = orderId
        param_dict['resultType'] = "transfer,predict"
        print("")
        print("查询部分：")
        print("get result参数：", param_dict)
        status = 3
        # 建议使用回调的方式查询结果，查询接口有请求频率限制
        while status == 3:
            response = requests.post(url=lfasr_host + api_get_result + "?" + urllib.parse.urlencode(param_dict),
                                     headers={"Content-type": "application/json"})
            # print("get_result_url:",response.request.url)
            result = json.loads(response.text)
            print(result)
            status = result['content']['orderInfo']['status']
            print("status=", status)
            if status == 4:
                break
            time.sleep(5)
        print("get_result resp:", result)
        return result


def contentDeal(content, filename):
    content = content['lattice']

    for item in content:
        # json_1best 是dic类型
        json_1best = json.loads(item['json_1best'])

        # rt 是只有一个元素的list
        rt = json_1best['st'].get('rt')[0]

        # ws是list
        ws = rt.get('ws')
        for item2 in ws:
            # 得到word词语和标点
            word = item2.get('cw')[0].get('w')
            # print(word)
            with open('../totext/result/' + filename + '.txt', 'a', encoding='utf-8') as fp2:
                fp2.write(word)


# 输入讯飞开放平台的appid，secret_key和待转写的文件路径
def w2t(file):
    filename = file.split('.')[0]
    print(f"Processing audio file: {file}")
    api = RequestApi(appid="b870f1cb",
                     secret_key="6a442fcb7c5ddb15987c85cb65072893",
                     upload_file_path=r"../bili2text-main/audio/conv/" + file)

    result = api.get_result()

    # 处理并下载返回的信息
    orderResult = result['content']['orderResult']
    print("=============orderResult========type==============")
    print(type(orderResult))
    print(orderResult)
    contentDeal(json.loads(orderResult), filename)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
        pos = audio_path.rfind('\\')
        if pos != -1:
            audio_path = audio_path[pos + 1:]

        print(audio_path)
        w2t(audio_path)
    else:
        print("No audio path provided.")
