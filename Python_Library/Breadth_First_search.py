from collections import deque
h,w = map(int,input().split())
l = [['*'] * (w+2)]
for i in range(h):
    l.append(['*'] + list(input()) + ['*'])
l.append(['*'] * (w+2))
# print(l)

for i in range(h+2):
    for j in range(w+2):
        if l[i][j] == 's':
            start = (i,j)
        elif l[i][j] == 'g':
            goal = (i,j)

coordinates = [(1,0),(0,1),(-1,0),(0,-1)]

que = deque([start])
l[start[0]][start[1]] = -1

while que:
    x = que.pop()
    for cd in coordinates:
        y = (x[0]+cd[0], x[1]+cd[1])
        if l[y[0]][y[1]] in ['.','g']:
            que.append(y)
            l[y[0]][y[1]] = -1
    # print(que)
if l[goal[0]][goal[1]] == -1:
    print('Yes')
else:
    print('No')


# UnionFindやりましょう