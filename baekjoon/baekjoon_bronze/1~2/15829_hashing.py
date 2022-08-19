alpha_dict = {chr(96+i):i for i in range(1,27)}
L = int(input())
s = input()
hashing = 0
for i in range(len(s)):
    hashing += alpha_dict[s[i]] * (31**i)
print(hashing%1234567891)