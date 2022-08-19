def fn_d(n):
    n = str(n)
    summ = 0
    for i in n:
        summ += int(i)
    n = int(n)
    return summ + n

for i in range(1,10000):
    for j in range(i+1):
        if fn_d(j) == i:
            break
    else:
        print(i)