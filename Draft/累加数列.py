print("这是一个计算累加的循环代码")
print("他将从1+2+3+......+N")
num = 0
print("请输入数字N的值")
N = int(input())
for i in range(1, N+1):
    num = num + i
print("累加值为%d"%num)
print("-------------------------")
print("for是从1循环到N，而不是到N+1")