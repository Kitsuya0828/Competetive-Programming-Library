import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

maxn = 18
t = [[0]*maxn for _ in range(maxn)]

dp = [[-1]*(maxn) for _ in range(1<<maxn)]

def rec(S,v):
    if dp[S][v] >= 0:   # すでに探索済みだったらリターン
        return dp[S][v]
    if S==(1<<n)-1 and v==0:  # 初期値
        dp[S][v] = 0
        return dp[S][v]
    tmp = 10**9   # 答えを格納する変数
    for u in range(n):    # vの手前のノードとしてuを全探索
        if not (S>>u &1):
            tmp = min(tmp,rec(S|1<<u,u)+t[v][u])   # 再帰的に探索
    dp[S][v] = tmp
    return dp[S][v]

for i in range(n):
    for j in range(n):
        t[i][j] = abs(l[j][0]-l[i][0])+abs(l[j][1]-l[i][1])+max(0,l[j][2]-l[i][2])   # 辺の重みに相当するもの
print(rec(0,0))




