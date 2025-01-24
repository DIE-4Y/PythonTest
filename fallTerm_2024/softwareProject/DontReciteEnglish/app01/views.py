import random
from django.http import HttpResponse
from .models import poetry, similar_words
import re
# from DontReciteEnglish.app01.models import poetry, similar_words

# 函数：从数据库中随机取出一个content，并随机取出三个字
def replace_words():
    # 随机选择一个content
    poet = poetry.objects.order_by('?').first()

    content = poet.content
    pattern = re.compile(r'[^\u4e00-\u9fff]+')
    cleaned_content = re.sub(pattern, '', content)
    # 随机选择三个字
    if len(cleaned_content) >= 3:
        chars = random.sample(list(cleaned_content), 3)
    else:
        chars = cleaned_content

    # 查找这三个字对应的related_character
    replaced_chars = []
    for char in chars:
        similarword = similar_words.objects.filter(main_character=char).first()
        if similarword:
            # 从related_character中随机选择一个字
            replaced_chars.append(random.choice(list(similarword.related_character)))
        else:
            replaced_chars.append(char)  # 如果没有找到，保留原字符

    # 替换原来的字
    new_contents = []
    for i in range(3):
        new_content = list(content)
        for j, char in enumerate(chars):
            new_content[content.index(char) + i * len(chars)] = replaced_chars[j]
        new_contents.append(''.join(new_content))

    return content, new_contents

def random_poetry(request):
    content, new_contents = replace_words()
    if content and new_contents:
        result = f"Original Content: {content}<br><br>New Contents:<br>{'<br>'.join(new_contents)}"
        return HttpResponse(result)
    else:
        return HttpResponse("未能从数据库中获取内容。")

