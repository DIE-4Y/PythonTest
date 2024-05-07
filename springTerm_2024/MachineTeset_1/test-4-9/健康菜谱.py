diet = ["西红柿", "花椰菜", "黄瓜", "牛排", "虾仁"]
for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            print("{}{}".format(diet[i], diet[j]))
