import urllib.request

# 下载网页源码
url_page = 'http://www.baidu.com'
urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载网页图片
url_img = 'https://tse2-mm.cn.bing.net/th/id/OIP-C.cGjCuP5ghtV5SuGhFWIqUAHaHa?w=208&h=208&c=7&r=0&o=5&dpr=1.3&pid=1.7'
urllib.request.urlretrieve(url_img, 'shanshui.jpg')

# 下载网页视频
url_video = 'http://vod.v.jstv.com/2024/07/31/JSTV_JSWSNEW_1722388795918_Ha2qgd9_1934.mp4'
urllib.request.urlretrieve(url_video, 'video.mp4')