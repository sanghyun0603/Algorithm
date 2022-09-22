N = int(input())
if N < 100:
    hannum = N
else:
    hannum = 99
    for i in range(100,N+1):
        i = str(i)
        num_li = list(map(int,i))
        if num_li[1]-num_li[0] == num_li[2]-num_li[1]:
            hannum +=1
print(hannum)