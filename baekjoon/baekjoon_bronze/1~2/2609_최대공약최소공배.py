N1, N2 = map(int,input().split())
num = 1
max_gong = 0
min_gongbae = 0
big_li =[]
if N1 > N2:
    pass
elif N1 < N2:
    N1,N2 = N2,N1
while True:
    if N1 == N2:
        min_gongbae = N1
        break
    N1_m = N1 * num
    N2_m = N2 * num
    big_li.append(N1_m)
    if N2_m in big_li :
        min_gongbae = N2_m
        break
    num += 1
for i in range(min(N1,N2),0,-1):
    if N1%i == 0 and N2%i == 0:
        max_gong = i
        break
print(max_gong)
print(min_gongbae)