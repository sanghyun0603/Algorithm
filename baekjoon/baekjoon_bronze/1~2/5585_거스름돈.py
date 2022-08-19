M = 1000 - int(input())
yen = [500,100,50,10,5,1]
cnt = 0
for i in yen:
    if M >= i:
        cnt += M//i
        M = M%i
print(cnt)
