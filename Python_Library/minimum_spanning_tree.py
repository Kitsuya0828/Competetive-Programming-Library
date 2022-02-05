import heapq    # heapqモジュールのimport
V, E = map(int, input().split()) # グラフGの頂点の数|V|，辺の数|E|の受け取り

"""
Input:
    - グラフGの隣接リスト
Description:
    グラフG(V,E)について，最小全域木の辺の重みの総和を返す
    プリムのアルゴリズム
"""
def prim(G):
    visited = [0]*V # 訪問済みリスト
    connection = 0  # 最小全域木に属する頂点の数
    hq = [(0, 0)]   # 空リストに，始点のコスト0と頂点番号sのタプルを追加
    heapq.heapify(hq)   # リストを優先度付きキューに変換
    ans = 0 # 最小全域木の辺の重みの総和
    
    while hq:   # 優先度付きキューが空になるまで繰り返す
        cost, v = heapq.heappop(hq)    # 優先度付きキューから，コストが最小である頂点の（コスト，番号）を取り出す
        if visited[v]:  # 頂点が訪問済みならば
            continue    # 何もしない
        
        visited[v] = 1  # コスト最小の頂点を訪問済みにする
        connection += 1 # 最小全域木に属する頂点の数を1増やす
        ans += cost # 最小全域木の辺の重みの総和を更新する
        
        for u in G[v]:  # 取り出した頂点に隣接する頂点uを優先度付きキューに追加する
            heapq.heappush(hq, u)    # 優先度付きキューに更新した頂点の（コスト，番号）を追加する
        
        if connection == V: # 全ての頂点が最小全域木に属した場合
            break   # 処理を停止する
    return ans  # 最小全域木の辺の重みの総和を返す

G = [[] for _ in range(V)]  # グラフGの隣接リスト
for i in range(E):  # 辺の数の回数だけ
    s, t, w = map(int, input().split()) # 2頂点s，tとそれを結ぶ辺の重みwの受け取り
    G[s].append((w, t)) # 頂点sに，頂点tとを結ぶ辺の重みwを記録
    G[t].append((w, s)) # 頂点tに，頂点sとを結ぶ辺の重みwを記録（無向グラフ）
print(prim(G))  # 最小全域木の辺の重みの総和を出力