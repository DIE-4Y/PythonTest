import mysql.connector
import json

# 数据库连接配置
"""修改数据库的 用户名 密码 数据库名称 为自己的 再运行这个文件"""
db_config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'dontreciteenglish'
}

# 创建数据库连接
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# 创建表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shici (
        id INT AUTO_INCREMENT PRIMARY KEY,
        word VARCHAR(255),
        mean TEXT
    )
''')

def insert_json_to_db(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            word = item.get('word', '')
            mean = '\n'.join(item.get('mean', []))
            cursor.execute('''
                INSERT INTO shici (word, mean) 
                VALUES (%s, %s)
            ''', (word, mean))
        conn.commit()

# 使用函数将JSON文件插入到数据库中
insert_json_to_db('shici.json')

# 关闭数据库连接
cursor.close()
conn.close()
