num = eval(input("请输入要计算的阶乘"))
result = 1
if num != 0:
    for i in range(1, num+1):
        result *= i
print("{}！={}".format(num, result))