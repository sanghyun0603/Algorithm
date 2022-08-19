s = input()
lit = [[0],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],
       ['P','Q','R','S'],['T','U','V'],['X','Y','W','Z']]
cnt = 0
for i in range(1,len(lit)):
    N = len(lit[i])
    for j in range(N):
        for k in range(len(s)):
            if s[k] in lit[i][j]:
                cnt += i+2
print(cnt)