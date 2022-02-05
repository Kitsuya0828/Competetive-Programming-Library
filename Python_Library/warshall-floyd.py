V, E = map(int, input().split()) # グラフGの頂点の数|V|，辺の数|E|の受け取り

"""
Input:
    - グラフGの隣接行列dist
Description:
    重み付き有向グラフdist(V,E)について，全点対間最短経路の距離を求める
    ワ―シャルフロイド法
"""
def warshall_floyd(dist):
    V = len(dist)  # 頂点の個数（隣接行列の長さ）
    for k in range(V):  # 経由点k=0からV-1まで繰り返す
        for i in range(V):  # 始点i=0からV-1まで繰り返す
            for j in range(V):  # 終点j=0からV-1まで繰り返す
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]) # i→k→jという経路の重みが，dist[i][j]よりも小さければ更新する
    return  # 処理を終了する

dist = [[float('inf')]*V for _ in range(V)] # グラフGの隣接行列（∞は経路が存在しない）
for i in range(E):  # 辺の数の回数だけ
    s, t, d = map(int, input().split()) # 2頂点s，tとそれを結ぶ辺の重みdの受け取り
    dist[s][t] = d  # 頂点sから頂点tへの最短経路（辺）の重みはd
for i in range(V):  # 全ての頂点について
    dist[i][i] = 0  # 自分から自分への最短経路を0で初期化
    
warshall_floyd(dist)    # 全点対間最短経路の距離を求める
if any([dist[i][i] for i in range(V)]): # 閉路の重みの総和が0となる場合
    print('NEGATIVE CYCLE') # 'NEGATIVE CYCLE'と出力する
    exit()  # プログラムを終了する
for i in range(V):  # 始点i=0からV-1まで繰り返す
    for j in range(V):  # 終点j=0からV-1まで繰り返す
        if dist[i][j] == float('inf'):  # 頂点iから頂点jへの経路が存在しない場合
            dist[i][j] = 'INF'  # 'INF'を出力
        print(dist[i][j], end=' ' if j!= V-1 else '\n') #  # 頂点iから頂点jへの最短経路を出力する