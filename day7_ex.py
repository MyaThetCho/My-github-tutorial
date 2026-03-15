number = [1, 2, 4, 2, 4, 4, 1]
tmp = []


max = number[0]
min = number[0]

for i in number:
    if i < min:
        min=i
    if i > max:
        max=i
    if i not in tmp:
        tmp.append(i)

print("Min :", min)
print("Max :", max)
print(tmp)



