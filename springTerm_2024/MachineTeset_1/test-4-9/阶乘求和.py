num = eval(input("请输入要求的数字:>"))
result = 0
for i in range(1, num +1):
    temp = 1
    for j in range(1, i+1):
        temp *= j
#    print("{}".format(temp), end=" ")
    result += temp
# print()
if num > 1:
    for i in range(1, num):
        print("{}! + ".format(i) ,end="")
    print("{}! = ".format(num), end="")
print(result)
