T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(input().split())
    shuffle = []
    mid = len(card)//2
    for i in range(mid):
        if len(card)%2 == 0:
            shuffle.append(card[i])
            shuffle.append(card[i+mid])
        else:
            shuffle.append(card[i])
            shuffle.append(card[i+mid+1])
    if len(card)%2 == 1:
        shuffle.append(card[mid])
    print(f'#{tc}',*shuffle)
