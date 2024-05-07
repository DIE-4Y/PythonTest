user_dict = {"zhaoyi":"zhaoPSD",
             "qianer":"qianPSD",
             "sunsan":"sunPSD",
             "lisi":"liPSD",
             "zhouwu":"zhouPSD"}
user = input("请输入你的账号")
password = input("请输入你的密码")
if user in user_dict.keys():
    if password == user_dict[user]:
        print("success")
    elif password != user_dict[user]:
        print("password errorr")
else:
    print("not found")
