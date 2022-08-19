N = int(input())
num = 1
while num < N:
    num_list = list(map(int,str(num)))
    sums = num
    for i in num_list:
        sums += i
    if sums ==N:
        break
    num +=1
if num == N:
    print(0)
else:
    print(num)