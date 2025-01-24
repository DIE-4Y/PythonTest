# import urllib.request
# import urllib.parse
#
#
# def get_word_cloud(file, color):
#     url = "http://niningqi.com/api/wordcloud"
#     with open('../totext/result/' + file, 'r', encoding='utf-8') as fp:
#         content = ''.join(fp.readlines())  # 将所有行合并为一个字符串
#
#     changed_content = urllib.parse.quote(content.encode('utf-8'))
#     requst_url = url + '?keywords=' + '{' + changed_content + '}&bgColor=' + color
#     req = urllib.request.Request(url=url)
#     response = urllib.request.urlopen(req)
#     content = response.read().decode('utf-8')
#     print(content)
#
#
# if __name__ == '__main__':
#     get_word_cloud("final_lfasr_涉政.txt", "black")


import urllib.request
import urllib.parse


def get_word_cloud(file, color):
    url = "http://niningqi.com/api/wordcloud"

    # 读取文件内容并合并为一个字符串
    with open('../totext/result/' + file, 'r', encoding='utf-8') as fp:
        content = ''.join(fp.readlines())  # 将所有行合并为一个字符串

    # 对内容进行 URL 编码
    changed_content = urllib.parse.quote(content)

    # 构建请求 URL
    requst_url = url + '?keywords=' + '{' + changed_content + '}&bgColor=' + color
    req = urllib.request.Request(url=requst_url)  # 将完整 URL 添加到请求中

    # 发送请求并获取响应
    try:
        response = urllib.request.urlopen(req)
        content = response.read()  # 获取返回内容（字节）

        # 假设返回的内容是 HTML 或图像，保存到文件
        with open('wordcloud_result.html', 'wb') as output_file:
            output_file.write(content)

        print("内容已保存到 'wordcloud_result.html' 文件中。")

    except Exception as e:
        print(f"请求失败：{e}")


if __name__ == '__main__':
    get_word_cloud("final_lfasr_涉政.txt", "black")
