import json
import re

# 定义正则表达式来匹配诗歌的标题、作者、朝代和内容
title_pattern = re.compile(r'《(.*?)》')
author_pattern = re.compile(r"作者：([^，。\s\n]+)")
# author_dynasty_pattern = re.compile(r'^(.+?)·(.*?)\s*〔(.*?)〕')
pattern = r"(?s)(?:作者：.*?)\n(.*?)(?=\n【注解】|\n【评析】|\n{2,})"

# 初始化一个空列表来存储诗歌信息
poems = []

# 读取文本文件
with open('./唐诗三百首.txt', 'r', encoding='utf-8') as file:  # 替换为实际的文件路径
    text = file.read()


# 分割文本为独立的诗歌块（假设每首诗歌之间有两个换行符分隔）
poem_blocks = text.split('\n\n\n')

# 遍历每个诗歌块
for block in poem_blocks:
    print("==========================")
    # print(block)
    # 尝试匹配标题
    title_match = title_pattern.search(block)
    if not title_match:
        continue  # 如果没有找到标题，则跳过该块

    title = title_match.group(1).strip()
    # print(title)

    # 尝试匹配作者和朝代
    author_match = author_pattern.search(block)
    author = author_match.group(1)
    # print(author)
    dynasty = '（唐代）'

    # 尝试匹配诗歌内容
    matches = re.findall(pattern, block, re.DOTALL)

    # 打印提取的古诗正文
    for match in matches:
        # 去除可能的首尾空白字符
        content = match.strip()
        print(content + "\n")

    # 将诗歌信息添加到列表中
    poems.append({
        'title': title,
        'author': author,
        'dynasty': dynasty,
        'content': [line.strip() for line in content.split('\n')]  # 将内容拆分为行并去除首尾空格
    })

# 将诗歌信息转换为JSON格式并写入文件
with open('唐诗三百首.json', 'w', encoding='utf-8') as json_file:
    # json.dump(poems, json_file, ensure_ascii=False, indent=4)
    print(json.dump(poems, json_file, ensure_ascii=False, indent=4))

print("JSON文件已生成！")


import re

with open('./唐诗三百首.txt', 'r', encoding='utf-8') as file:  # 替换为实际的文件路径
    text = file.read()

# 正则表达式，匹配从“作者：”之后到“【注解】”或“【评析】”之前的古诗正文
# 注意：这里使用了非贪婪匹配（*?）和换行符匹配（. 匹配包括换行符在内的任意字符）
pattern = r"(?s)(?:作者：.*?)\n(.*?)(?=\n【注解】|\n【评析】|\n{2,})"

# 使用re.findall来找到所有匹配项
matches = re.findall(pattern, text, re.DOTALL)

# 打印提取的古诗正文
for match in matches:
    # 去除可能的首尾空白字符
    poem_body = match.strip()
    print(poem_body + "\n")
