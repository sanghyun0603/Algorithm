def baby(playn,n,win):
    global winner
    play = set(playn)
    play = list(play)
    play.sort()
    while n < len(play) - 2:
        if play[n] == play[n + 1] - 1 and play[n + 1] == play[n + 2] - 1:
            winner = win
            return
        n += 1
    if winner != 0:
        return
    for j in play:
        if playn.count(j) == 3:
            winner = win
            return
T = int(input())
winner_li = []
for tc in range(1,T+1):
    num_li = list(map(int,input().split()))
    play1 = []
    play2 = []
    winner = 0

    for i in range(len(num_li)):
        if i%2 == 0:
            play1.append(num_li[i])
        else:
            play2.append(num_li[i])
        n1 = 0
        n2 = 0
        if i>= 4 and i%2 == 0:
            baby(play1,n1,1)
            if winner !=0:
                break
        if i>=5 and i%2 ==1:
            baby(play2,n2,2)
            if winner !=0:
                break
    winner_li.append(winner)
for i in range(len(winner_li)):
    print(f'#{i+1} {winner_li[i]}')