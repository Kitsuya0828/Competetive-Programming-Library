import heapq    # heapqモジュールのimport

V, E = map(int, input().split())    # グラフGの頂点の数|V|，辺の数|E|の受け取り
G = [[] for _ in range(V)]  # グラフGの隣接リスト
for i in range(E):  # 辺の数の回数だけ
    s, t = map(int, input().split())    # 頂点番号s，tの受け取り
    G[s].append(t)  # sがtよりも先に位置するように並べる

"""
Input:
    - グラフG(V,E)と，その頂点の数|V|
Description:
    DAG（有向非巡回グラフ）に対して，トポロジカルソートを行った頂点の並びを返す
"""
def topological_sort(V, G):
    in_number = [0]*V   #各頂点の入次数をカウントするためのリスト
    
    for after_v in G:   # 任意の頂点vよりも後に位置する頂点のリストにおいて
        for u in after_v:   # 各頂点uについて
            in_number[u] += 1   # 頂点uの入次数をカウントする（1つずつ増やす）

    S = []  # トポロジカル順に頂点を入れる空のリストを用意
    que = [i for i in range(V) if in_number[i] == 0]    # 入次数が0の頂点を記録するためのリスト
    heapq.heapify(que)  # リストを優先度付きキューに変換
    
    while que:  # 入次数が0の頂点がなくなるまで繰り返す
        u = heapq.heappop(que)  # 入次数が0かつ最小の頂点uを取り出す
        S.append(u) # リストに，入次数が0かつ最小の頂点uを追加する
        for v in G[u]:  # uに隣接する各頂点vについて
            in_number[v] -= 1   # vの入次数を1つ減らす
            if in_number[v] == 0:   # vの入次数が0になると，vを訪問できるようになるので
                heapq.heappush(que, v)  # vを優先度付きキューに追加する
    return S    # トポロジカル順に頂点を入れたリストを返す

ans = topological_sort(V, G)    # トポロジカルソートした頂点の並びのリストが求められる
if len(ans) != V:   # リストの長さが頂点の個数と同じでなければ
    print(-1)   # トポロジカルソートできない（閉路を含む）  
# トポロジカルソートできる ⇔ DAG（有向非巡回グラフ，閉路のない有向グラフ）である
else:   # そうでなければ
    for i in range(V):  # トポロジカルソートした頂点のリストから順番に
        print(ans[i])   # 頂点の番号を出力する