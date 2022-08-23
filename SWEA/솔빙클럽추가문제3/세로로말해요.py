T = int(input())
for tc in range(1,T+1):
    mat= [input() for _ in range(5)]
    max_len = 0
    for i in mat:
        if max_len < len(i):
            max_len = len(i)
    for i in range(len(mat)):
        if len(mat[i]) != max_len:
            mat[i] = mat[i] + '@'*(max_len-len(mat[i]))
    print(f'#{tc}',end=' ')
    for i in range(max_len):
        for j in range(5):
            if mat[j][i] != '@':
                print(mat[j][i],end='')
    print()