num_li = []
odd_li = []
for i in range(7):
    N = int(input())
    num_li.append(N)
for i in num_li:
    if i%2 == 1:
        odd_li.append(i)
if odd_li == []:
    print(-1)
else:
    print(sum(odd_li))
    print(min(odd_li))
