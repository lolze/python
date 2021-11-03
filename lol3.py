s = str(input())
m = 1
n = 1
j = s[n:n+1]
for i in s:
    if i in j:
        m += 1
    else:
        print(i, end='')
        print(m, end='')
        m = 1
    n += 1
    j = s[n:n+1]