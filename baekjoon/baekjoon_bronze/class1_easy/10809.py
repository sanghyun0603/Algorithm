alpha = {alpha : -1 for alpha in 'abcdefghijklmnopqrstuvwxyz'}
s = input()
for i in range(len(s)):
    if alpha[s[i]] == -1:
        alpha[s[i]] = i
print(*alpha.values())