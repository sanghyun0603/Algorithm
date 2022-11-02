T = int(input())
for tc in range(1,T+1):
    s = input()
    top = 0
    for i in s:
        if i == '(':
            top += 1
        elif i == ')':
             top -=1
        if top < 0:
            break
    if top == 0:
        print('YES')
    else:
        print('NO')