import mysql.connector
import json

from django.utils.lorem_ipsum import words

# 初始化一个空字典来存储数据
data_dict = {}

# 打开TXT文件并读取内容
with open('Shape.txt', 'r', encoding='utf-8') as txt_file:
    for line in txt_file:
        # 去除每行的前后空白字符
        line = line.strip()
        # 如果行不是空的
        if line:
            # 将第一个汉字作为键，其余的作为值
            key = line[0]
            value = line[1:].split()
            # 将键值对添加到字典中
            data_dict[key] = value

# 将字典转换为JSON格式并写入文件
with open('SimilarWord.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=4)

with open('SimilarWord.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# 数据库连接配置
db_config = {
    'user': 'root',
    'password': 'jch040208',
    'host': '127.0.0.1',
    'database': 'dontreciteenglish'
}

# 创建数据库连接
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# 创建表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS similar_words (
        id INT AUTO_INCREMENT PRIMARY KEY,
        main_character VARCHAR(255) NOT NULL,
        related_characters TEXT
    );
''')

for main_char, related_chars in data.items():
    # 将列表转换为JSON字符串
    related_chars_json = json.dumps(related_chars)
    # 插入数据到数据库
    query = "INSERT INTO similar_words (main_character, related_characters) VALUES (%s, %s)"
    cursor.execute(query, (main_char, related_chars_json))

conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()
