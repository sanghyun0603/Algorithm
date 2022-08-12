x_li = []
y_li = []
for i in range(3):
    x1, y1 = map(int, input().split())
    x_li.append(x1)
    y_li.append(y1)
x_li.sort()
y_li.sort()
if x_li.count(x_li[0]) == 1:
    x = x_li[0]
elif x_li.count(x_li[-1]) ==1:
    x = x_li[-1]
if y_li.count(y_li[0]) == 1:
    y = y_li[0]
elif y_li.count(y_li[-1]) ==1:
    y = y_li[-1]
print(x,y)