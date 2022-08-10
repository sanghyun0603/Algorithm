while 1:
    try:
        N, S = map(int, input().split())
        if S >= (N + 1):
            print(S // (N + 1))
        else:
            print(0)
    except EOFError:
        break
        
# EOF 문제