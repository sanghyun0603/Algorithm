N = int(input())
for game in range(1,N+1):
    s = str(game)
    crap = 0
    for i in s:
        if (i =='3') or (i == '6') or (i == '9'):
            crap += 1
    if crap == 0:
        print(game, end=' ')
    else:
        print('-'*crap, end = ' ')