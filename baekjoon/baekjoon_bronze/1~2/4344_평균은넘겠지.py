T = int(input())
for tc in range(1,T+1):
    li = list(map(int,input().split()))
    N = li.pop(0)
    avg = sum(li)/N
    avg_over = 0
    for i in li:
        if i > avg:
            avg_over += 1
    per = round((avg_over/len(li))*100,3)
    print('%.3f'%per,end='')
    print('%')