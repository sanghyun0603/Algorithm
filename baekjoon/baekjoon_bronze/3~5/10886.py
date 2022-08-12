N = int(input())
cute_li = []
for i in range(N):
    ans = int(input())
    cute_li.append(ans)
cute = cute_li.count(1)
not_cute = cute_li.count(0)
if cute > not_cute :
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')