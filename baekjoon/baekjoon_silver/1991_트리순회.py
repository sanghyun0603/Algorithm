def preorder(n):
    if n:
        print(chr(n+64),end='')
        preorder(ch1[n])
        preorder(ch2[n])
def inorder(n):
    if n:
        inorder(ch1[n])
        print(chr(n+64),end='')
        inorder(ch2[n])
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(chr(n+64),end='')
N = int(input())
ch1 = [0]*(N+1)
ch2 = [0]*(N+1)
for i in range(N):
    p,l,r = input().split()
    pa = ord(p)-64
    if l != '.':
        ch1[pa] = ord(l)-64
    if r != '.':
        ch2[pa] = ord(r)-64
preorder(1)
print()
inorder(1)
print()
postorder(1)