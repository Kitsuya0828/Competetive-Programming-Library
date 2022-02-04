import heapq    # heapqモジュールのimport
V, E, r = map(int, input().split()) # グラフGの頂点の数|V|，辺の数|E|，始点の番号rの受け取り

"""
Input:
    - 始点の頂点番号s
Description:
    グラフG(V,E)と始点sについて，単一始点最短経路の重みリストを返す
    ダイクストラのアルゴリズム（優先度付きキュー）
"""
def dijkstra(s):
    hq = [(0, s)]   # 空リストに，始点のコスト0と頂点番号sのタプルを追加
    heapq.heapify(hq)   # リストを優先度付きキューに変換
    cost = [float('inf')]*V # 始点以外のVに属する全ての頂点に対して，コストを∞にする
    cost[s] = 0 # 始点のコストを0にする
    while hq:   # 優先度付きキューが空になるまで繰り返す
        c, v = heapq.heappop(hq)    # 優先度付きキューから，コストが最小である頂点の（コスト，番号）を取り出す
        if c > cost[v]: # 取り出したコストが現在のコストよりも高ければ
            continue    # 何もしない
        for d, u in e[v]:   # 取り出した頂点vに隣接する全ての頂点（コストd，番号u）について
            tmp = d + cost[v]   # 頂点vのコストに，頂点uと頂点vを結ぶ辺の重みを足す
            if tmp < cost[u]:   # 頂点uの現在のコストよりも低ければ
                cost[u] = tmp   # 頂点uのコストを更新する
                heapq.heappush(hq, (tmp, u))    # 優先度付きキューに更新した頂点のコストtmpと番号uを追加する
    return cost # 各ノードへの最短経路のコストを格納したリストを返す
        
e = [[] for _ in range(V)]  # 各辺の重みを記録するリスト
for i in range(E):  # グラフGの各辺（0~|E|-1）について
    s, t, d = map(int, input().split()) # 2頂点s，tとそれを結ぶ辺のコストdの受け取り
    e[s].append((d, t)) # 頂点sに，頂点tとを結ぶ辺のコストdを記録

result = dijkstra(r)    # 始点rについて，単一始点最短経路の重みリストを求める
for res in result:  # 各ノードの最短経路のコストについて
    if res != float('inf'): # 最短経路のコストが∞でなければ
        print(res)  # 始点からノードへの最短経路のコストを出力
    else: # 最短経路のコストが∞ならば
        print('INF')    # INFと出力する