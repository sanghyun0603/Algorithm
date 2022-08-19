N = int(input())

if N < 10 :
    new_num = '0'+str(N)
    search_num = new_num
else:
    new_num = str(N)
    search_num = str(N)
cnt = 0
while True:
    cnt += 1
    sums = int(new_num[0]) + int(new_num[1])
    sums = str(sums)
    new_num = new_num[1] + sums[-1]
    if new_num == search_num:
        break

print(cnt)