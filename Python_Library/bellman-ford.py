V, E, r = map(int, input().split()) # グラフGの頂点の数|V|，辺の数|E|，始点の番号rの受け取り

"""
Input:
    - 始点の頂点番号r
Description:
    負の重みをもつ辺を含むグラフG(V,E)と始点sについて，単一始点最短経路の重みリストを返す
    ベルマンフォード法
"""
def bellman_ford(G, r):
    dist = [float('inf')]*V # 全ての頂点への最短経路の重みの総和を∞で初期化する
    dist[r] = 0     # 始点から始点への最短経路の重みの総和は0
    for _ in range(V):  # 頂点の個数の回数だけ繰り返す
        update = 0  # 頂点を更新したかどうか
        for v, e in enumerate(G):   # 各辺の頂点について
            for t, cost in e:   # 頂点vに隣接する頂点tとそれを結ぶ辺の重みcostについて
                if dist[v]!=float('inf') and dist[v] + cost < dist[t]:  # 頂点tへの最短経路が頂点vを経由する形で更新できれば
                    dist[t] = dist[v] + cost    # 最短距離を更新する
                    update = 1  # 更新したことを記録する
        if not update:  # 更新がなければ
            return dist # 終了して，各頂点への最短経路の重みの総和のリストを返す
    # V回目のループで更新できる頂点があった場合
    return -1   # 負閉路を検出したとして-1を返す

G = [[] for _ in range(V)]  # 各辺の重みを記録するリスト
for i in range(E):  # グラフGの各辺（0~|E|-1）について
    s, t, d = map(int, input().split()) # 2頂点s，tとそれを結ぶ辺のコストdの受け取り
    G[s].append((t, d)) # 頂点sに，頂点tとを結ぶ辺のコストdを記録
result = bellman_ford(G, r)    # 始点rについて，単一始点最短経路の重みリストを求める
if result == -1:    # 負閉路が存在する場合
    print("NEGATIVE CYCLE") # "NEGATIVE CYCLE"と出力する
else:   # 負閉路が存在しない場合
    for i in range(V):  # 各頂点について
        if result[i] != float('inf'):   # 頂点iへの最短経路上の重みの総和が∞でない場合
            print(result[i])    # 重みの総和を出力
        else:   # 頂点iへの最短経路上の重みの総和が∞である場合
            print('INF')    # 頂点iへの経路が存在しないのでINFを出力