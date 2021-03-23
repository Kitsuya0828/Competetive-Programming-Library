import heapq

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * 10 # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

h,w = map(int,input().split())
e = [[] for _ in range(10)]
for i in range(10):
    alist = list(map(int,input().split()))
    for j in range(10):
        if i != j:
            e[i].append((alist[j], j))


l = []
for i in range(h):
    for a in list(map(int,input().split())):
        if a != -1:
            l.append(a)

ans = 0
for i in l:
    ans += dijkstra(i)[1]
print(ans)