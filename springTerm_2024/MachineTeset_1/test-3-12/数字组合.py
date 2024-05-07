sum = 0
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                z = (i * 100 + j * 10 + k)
                print(z)
                count += 1
                sum += z
print("一共{}种,总和为{}".format(count, sum))
