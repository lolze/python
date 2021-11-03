sum = 0
a = [int(i) for i in input().split()]
for m in range(0, len(a)):
    sum = sum + a[m]
    m += 1
print(sum)