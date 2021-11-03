sum = 0
m = 0
a = [int(i) for i in input().split()]
if len(a) == 1:
        sum = a[m]
        print(sum)
elif len(a) == 2:
        sum = a[1] * 2
        print(sum, end=' ')
        sum = a[0] * 2
        print(sum)
else:
    sum = a[m-1] + a[m+1]
    print(sum, end=' ')
    for m in range(1, len(a)-1):
            sum = a[m-1] + a[m+1]
            m += 1
            print(sum, end=' ')
    sum = a[m-1] + a[0]
    print(sum)