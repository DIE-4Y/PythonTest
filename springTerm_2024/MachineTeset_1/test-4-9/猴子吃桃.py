days = eval(input("请输入吃桃的天数:>"))
sum = 1
for i in range(1, days):
    sum = (sum + 1) * 2
print("桃子总数共有{}".format(sum))
