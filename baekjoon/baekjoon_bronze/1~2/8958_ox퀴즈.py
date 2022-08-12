T = int(input())
for tc in range(1,T+1):
    ox = list(input())
    sums = 0
    cnt = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt += 1
        else:
            cnt = 0
        sums += cnt
    print(sums)
