def bubun(n,r,s):
    if r==0:
        for j in range(6):
            print(bu[5-j],end=' ')
        print('')
        return
    else:
        for i in range(s,n-r+1):
            bu[r-1] = num_li[i]
            bubun(n,r-1,i+1)
while True:
    num_li = list(map(int,input().split()))
    if num_li[0] == 0:
        break
    del num_li[0]
    n = len(num_li)
    bu = [0]*6
    bubun(n,6,0)
    print()
