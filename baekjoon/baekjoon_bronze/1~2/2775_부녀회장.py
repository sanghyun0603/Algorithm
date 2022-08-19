T = int(input())
for tc in range(1,T+1):
    k = int(input())
    n = int(input())
    sums = 0
    mat = [[0]*14 for _ in range(k+1)]
    for i in range(k+1):
        for j in range(0,n):
            if j == 0:
                mat[i][j] = 1
            elif i > 0 :
                mat[i][j] = mat[i][j-1] + mat[i-1][j]
            else:
                mat[i][j] = j+1
    print(mat[k][n-1])