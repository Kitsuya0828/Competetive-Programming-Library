# 再帰関数は，PypyよりPythonのほうが高速

import sys
sys.setrecursionlimit(10**7)
h,w = map(int,input().split())
l = [list(input()) for i in range(h)]

def dfs(x,y):
    if not(0 <= x < h) or not(0 <= y < w) or l[x][y] == '#':
        return
    if l[x][y] == 'g':
        print('Yes')
        exit()
    
    l[x][y] = '#'
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

for i in range(h):
    for j in range(w):
        if l[i][j] == 's':
            sx,sy = i,j

dfs(sx,sy)
print('No')