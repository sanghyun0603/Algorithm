T = int(input())
for test_case in range(1, T + 1):
    N = input()
    a= list(map(int,input().split()))
    count = 0
    max = 0
    ma =0
    for i in reversed(range(0,len(a))):
        count += 1
        if max < a[i]:
            max = a[i]
            while count > 0 :
                ma += (max-a[i-count])
                count -= 1
    print(max,ma)