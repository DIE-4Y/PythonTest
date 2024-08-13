from lxml import etree

# xpath解析 必须有结束标签否则会报错
# （1）本地文件
# （2）服务器响应

# 本地解析
tree = etree.parse('xpath基本使用.html')
# print(tree)

"""路径查询>>:  //表示所有后续结点  /表示直接后继结点"""

# # （1）判断li标签的个数
li_list = tree.xpath('//body//li')
# li_list = tree.xpath('//body//ul/li')
print(li_list)
print(len(li_list))

# （2）查找有id的li标签
# text()获取标签中的内容
id_list = tree.xpath('//ul/li[@id]/text()')
print(id_list)
print(len(id_list))
# 查找id为1的标签并获取内容
id_list2 = tree.xpath('//ul/li[@id="1"]/text()')
print(id_list2)
print(len(id_list2))

# （3）属性查询
# 查找id为1的属性
li1 = tree.xpath('//ul/li[@id="1"]/@class')
print(li1)

# （4）模糊查询
# 查找id中包含1的标签
li2 = tree.xpath('//ul/li[contains(@id,"1")]/text()')
print(li2)
# 查询id以3开头的标签
li3 = tree.xpath('//ul/li[starts-with(@id,"3")]/text()')
print(li3)

# （5）
