from collections import deque   # collectionsモジュールからdequeのimport

n = int(input())    # 木の頂点の個数
prv = [None for _ in range(n)]    # prv[u]: 頂点uの一つ上の祖先頂点
G = [[] for _ in range(n)]  # G[v]: 頂点vの子頂点 (親頂点は含まない)
for i in range(n):  # 木の頂点の個数の回数だけ繰り返す
    k, *G[i] = list(map(int, input().split()))   # 入力の受け取り
    for c in G[i]:  # 頂点iの全ての子頂点について
        prv[c] = i  # 子頂点の祖先頂点を頂点iとする

depth = [0]*n   # 各頂点の根からの深さ
que = deque([0])    # 根をキューに入れる
while que:  # キューが空になるまで
    v = que.popleft()   # キューから頂点を1つポップする
    d = depth[v]    # 頂点vの深さを取得する
    for w in G[v]:  # vの子頂点wについて
        depth[w] = d+1  # 深さは（祖先頂点の深さ）+1とする
        que.append(w)   # キューに子頂点wを追加する

LV = (n-1).bit_length() # 木の深さは，高々log2(頂点数)を超えない


"""
Input:
    - 頂点の一つ上の祖先頂点のリストprv
Description:
    ダブリングによって2^k先の祖先を求め，各頂点の2^k個上の祖先頂点を入れた二次元リストを返す
"""
def construct(prv):
    kprv = [prv]    # 子頂点の2^k(k=0)個上の祖先頂点としてprvをそのまま用いる
    S = prv # Sは一つ前の結果
    for k in range(LV): # 木の高さ1~LVまで
        T = [0]*n   # 各頂点について2^(k+1)個上の祖先頂点を入れるリスト
        for i in range(n):  # 各頂点について
            if S[i] is None:    # 2^k個上の祖先頂点が無ければ
                continue    # 何もしない
            T[i] = S[S[i]]  # 「2^k先の要素の2^k先」を求めることで「2^(k+1)先の要素」を求める
        kprv.append(T)  # 2^(k+1)個上の祖先頂点を入れたリストを元のリストに追加する
        S = T   # 1つ前の結果を更新する
    return kprv # 各頂点の2^k個上の祖先頂点を入れたリストを返す

"""
Input:
    - 最小共通祖先を求めたい頂点u，v
    - 頂点の2^k個上の祖先頂点のリストkprv
    - 各頂点の根からの深さのリストdepth
Description:
    頂点uと頂点vの最小共通祖先を返す
"""
def lca(u, v, kprv, depth):
    dd = depth[v] - depth[u]    # 頂点vと頂点uの深さの差
    if dd < 0:  # 頂点uの方が深い場合
        u, v = v, u # uとvをswapする（vの方が深くなる）
        dd = -dd    # 深さの差の正負を反転させる

    for k in range(LV+1):   # 木の深さ0~LVまで
        if dd & 1:  # ddの最下位ビットが1ならば
            v = kprv[k][v]  # 最小共通祖先までの距離が同じになるようにvを上にさかのぼらせる
        dd >>= 1    # 深さの差を更新する

    if u == v:  # uとvが同じ場合
        return u    # 最小共通祖先としてuを返す

    for k in range(LV-1, -1, -1):   # 木の深さLV-1から0まで
        pu = kprv[k][u] # 頂点uの2^k個上の祖先頂点
        pv = kprv[k][v] # 頂点vの2^k個上の祖先頂点
        if pu != pv:    # それぞれの祖先頂点が異なる場合（同じになるまで）
            u = pu  # uを祖先頂点で更新する
            v = pv  # vを祖先頂点で更新する

    return kprv[0][u]   # u（とv）の1個上の祖先頂点が最小共通祖先である

kprv = construct(prv)   # kprv[k][u]: 頂点uの2^k個上の祖先頂点（ダブリングによって求める） 

q = int(input())    # クエリの数
for i in range(q):  # クエリの数の回数だけ繰り返す
    u, v = map(int, input().split())    # 頂点の組u，vの受け取り
    ans = lca(u, v, kprv, depth)    # uとvの最小共通祖先を求める
    print(ans)  # 最小共通祖先を出力する