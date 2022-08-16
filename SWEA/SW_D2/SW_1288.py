T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    basu_num = 1
    num_set = set()
    while True:
        sheep = str(basu_num * N)
        for i in range(len(sheep)):
            num_set.add(sheep[i])
        if len(num_set) ==10:
            break
        basu_num +=1
    print(f'#{tc} {basu_num*N}')
        
