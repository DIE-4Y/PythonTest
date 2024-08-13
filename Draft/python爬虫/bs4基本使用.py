from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs4基本使用.html', 'r', encoding='utf-8'), 'lxml')

# # 获取第一个对应的标签
# print(soup.a)

# # 获取标签的属性和值
# print(soup.a.attrs)

"""bs4的三个函数:>>"""
# # （1）find
# # 直接寻找标签
# print(soup.find('a'))
# # 可通过标签属性找到对应标签
# print(soup.find('a', title='a2'))
# # 根据class标签寻找 class是关键字需加下划线
# print(soup.find('li', class_='c1'))

# # （2）find_all
# # 查找多个标签要用列表
# print(soup.find_all(['span', 'a']))
# # 限制返回个数
# print((soup.find_all('li', limit=3)))

# # （3）select
# # 属性选择器
# # 查找a标签
# print(soup.select('a'))
# # 查找类标签为c1
# print(soup.select('.c1'))
# # 查找id为l3的标签
# print(soup.select('#l3'))
# # 查找li标签中有id的标签
# print(soup.select('li[id]'))
# # 查找li标签中id为l1的标签
# print(soup.select('li[id="l1"]'))

# # 层级选择器
# # 后代选择器 选择div中的li 以空格隔开
# print(soup.select('div li'))
# # 子代（直接后代）选择器
# print(soup.select('div>ul>li'))
# # 查找a和span标签 与上边的find_all不同 不用列表
# print(soup.select('a,span'))

"""节点信息:>>"""
# # get_text()和string在标签内没有其他标签只有内容时 两方法作用相同
# # 标签内有标签时 string无法获取内容 get_text()可以
# obj = soup.select('#d1')[0]
# print(obj.string)
# print(obj.get_text())

"""节点属性:>>"""
obj = soup.select('#p1')[0]
# 获取结点标签的名称
print(obj.name)
# 获取结点的所有属性
print(obj.attrs)
# 获取节点的特定属性 三种方法
print(obj.attrs.get("class"))
print(obj.get("class"))
print(obj['class'])
