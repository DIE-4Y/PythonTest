count_dict = {}
user_input = input("请输入一个字符串包含数字和字母（以回车结束）: ")
for char in user_input:
    if char.isalnum():
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
print(count_dict)
