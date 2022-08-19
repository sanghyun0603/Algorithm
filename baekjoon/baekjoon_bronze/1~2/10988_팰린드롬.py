s = input()
mid = len(s)//2
cnt = 1
for i in range(1,len(s)//2 +1):
    if len(s)%2 == 1:
        if s[mid-i] != s[mid+i]:
            cnt = 0
            break
    else:
        if s[mid-i] != s[mid+i-1]:
            cnt =0
            break
print(cnt)