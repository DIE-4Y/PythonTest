import json
import re

with open('《全唐诗》作者：曹寅.txt', 'r', encoding='utf-8') as fp:
    text = fp.read()

# 正则表达式，匹配古诗的标题、作者和正文
# 注意：这里使用了非贪婪匹配（*?）和换行符匹配（. 匹配包括换行符在内的任意字符）
pattern = r"(?s)◎卷\.\d+【(.*?)】(.*?)\n(.*?)(?=(?:◎卷\.\d+【.*?】.*?\n)|$)"

# 使用re.finditer来找到所有匹配项
matches = re.finditer(pattern, text, re.DOTALL)

# 存储提取的古诗信息
poems = []

for match in matches:
    title = match.group(1).strip()  # 古诗名
    author = match.group(2).strip()  # 作者
    if not author:
        author = "无名氏"
    content = [line.strip() for line in match.group(3).split('\n') if line.strip()]
    # 将提取的信息添加到列表中
    poems.append({
        "title": title,
        "author": author,
        "dynasty": "（唐代）",
        "content": content
    })

# 将诗歌信息转换为JSON格式并写入文件
with open('全唐诗.json', 'w', encoding='utf-8') as json_file:
    # json.dump(poems, json_file, ensure_ascii=False, indent=4)
    print(json.dump(poems, json_file, ensure_ascii=False, indent=4))

print("JSON文件已生成！")

# 打印提取的古诗信息
# for poem in poems:
#     print(f"古诗名: {poem['title']}")
#     print(f"作者: {poem['author']}")
#     print(f"正文:\n{poem['content']}\n")