rabbit = 3
print("python定义变量不用定义类型")
print("第一年有%d只兔子，每年都会翻倍"%rabbit)
print("请输入第N年，程序将打印出N年后兔子的数量")
N = int(input())
for i in range (0, N):
    rabbit = rabbit * 2;
print("%d年后有%d只兔子"%(N, rabbit))
print("--------------------------------")
print("使用循环时需要加上  :  表示后边是它的内容")
print("python通过对齐表明从属关系")
print("python定义函数时不需要指定类型")
print("python用input函数读入值时需要指定类型")
print("用%d输出时如果有多个相同类型的数字连着就要用%()放在一起")
