#666 1666 2666 3666 4666 5666 6666 7666 8666 9666 10666 11666
# 16665
N = int(input())
num = 666
cnt = 0
while True:
    num = str(num)
    if '666' in num:
        cnt +=1
        if cnt == N:
            break
    num = int(num)
    num +=1
print(num)