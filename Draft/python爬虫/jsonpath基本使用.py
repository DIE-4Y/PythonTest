import json
import jsonpath

obj = json.load(open('jsonpath基本使用.json', 'r', encoding='utf-8'))

# # 所有价格
# price_list = jsonpath.jsonpath(obj, '$.store..price')
# print(price_list)

# # 所有书的名称
# book_list = jsonpath.jsonpath(obj, '$.store..book[*].title')
# print(book_list)

# # 第三本书
# book3 = jsonpath.jsonpath(obj, '$.store..book[3]')
# print(book3)

# # 最后一本书
# book_1 = jsonpath.jsonpath(obj, '$.store..book[(@.length-1)]')
# print(book_1)

# # 前两本书
# book_list = jsonpath.jsonpath(obj, '$..book[0,1].title')
# book_list = jsonpath.jsonpath(obj, '$..book[:2].title')
# print(book_list)


# # 条件过滤需要加（）
# # 包含isbn的书
# book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)].title')
# print(book_list)

# 超过8元的书
book_list = jsonpath.jsonpath(obj, '$..book[?(@.price>8)].title')
print(book_list)


