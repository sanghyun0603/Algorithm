s = input()
postfix = []
top = -1
stack = [0]*(len(s)//2)
for i in range(len(s)):
    if s[i].isalpha():
        postfix.append(s[i])
    else:
        if s[i] == '(':
            top +=1
            stack[top] = s[i]
        elif s[i] == ')':
            while True:
                if stack[top] == '(':
                    top -=1
                    break
                else:
                    postfix.append(stack[top])
                    top -= 1
        elif s[i] == '+':
            while True:
                if stack[top] == '+' or stack[top] == '*' or stack[top] == '/' or stack[top] == '-':
                    postfix.append(stack[top])
                    top -= 1
                else:
                    top += 1
                    stack[top] = s[i]
                    break
        elif s[i] == '*':
            while True:
                if stack[top] == '*' or stack[top] =='/':
                    postfix.append(stack[top])
                    top -= 1
                else:
                    top += 1
                    stack[top] = s[i]
                    break
        elif s[i] == '-':
            while True:
                if stack[top] == '-' or stack[top] == '+' or stack[top] == '*' or stack[top] == '/':
                    postfix.append(stack[top])
                    top -= 1
                else:
                    top += 1
                    stack[top] = s[i]
                    break
        elif s[i] == '/':
            while True:
                if stack[top] == '/' or stack[top] == '*':
                    postfix.append(stack[top])
                    top -= 1
                else:
                    top += 1
                    stack[top] = s[i]
                    break
while True:
    if top == -1:
        break
    else:
        postfix.append(stack[top])
        top -= 1
print(''.join(postfix))