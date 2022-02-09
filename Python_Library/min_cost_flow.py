from heapq import heapify, heappush, heappop # heapqモジュールからheapify，heappush，heappopをimport

class MinCostFlow:
    """最小費用流を求める
    """
    INF = 10**18    # INFを非常に大きい数で初期化

    def __init__(self, N):
        """コンストラクタ

        Args:
            N : 頂点の数
        """
        self.N = N  # 頂点の数
        self.G = [[] for i in range(N)] # フローネットワークGの隣接リスト

    def add_edge(self, fr, to, cap, cost):
        """フローネットワークに辺を追加する

        Args:
            fr : 辺の始点
            to : 辺の終点
            cap : 辺の容量
            cost : 辺のコスト
        """
        self.G[fr].append([to, cap, cost, len(self.G[to])]) # 辺：終点，残容量，コスト，逆辺
        self.G[to].append([fr, 0, -cost, len(self.G[fr])-1])    # 逆辺：始点，残容量0，負のコスト，辺

    def flow(self, s, t, f):
        """フローネットワークの始点sから終点tへの最小コストとなるパスを求め，そのパスに流量fのフローを流すときの最小コストを返す

        Args:
            s : フローネットワークの始点
            t : フローネットワークの終点
            f : 流したい流量
        """
        N = self.N  # 頂点の数
        G = self.G  # フローネットワークの隣接リスト
        INF = MinCostFlow.INF   # INFを大きい数で初期化

        res = 0 # 答えを0で初期化
        H = [0]*N   # ポテンシャルのリスト
        prv_v = [0]*N   # 1つ前の頂点のリスト
        prv_e = [0]*N   # 1つ前の辺のリスト

        while f:    # 流せるフローが0にならない限り繰り返す
            dist = [INF]*N  # 距離のリスト
            dist[s] = 0 # 始点の距離を0にする
            que = [(0, s)]  # リストに始点の距離と頂点番号を追加
            heapify(que)    # リストを優先度付きキューに変換
            
            # ダイクストラ法
            while que:  # キューが空にならない限り繰り返す
                c, v = heappop(que) # 最も小さい距離を持つ頂点vを取り出す
                if dist[v] < c: # 頂点vの距離が現在の距離よりも大きければ
                    continue    # 何もしない
                for i, (w, cap, cost, rev) in enumerate(G[v]):  # vに隣接する全ての辺に対して
                    if cap > 0 and dist[w] > dist[v] + cost + H[v] - H[w]:  # 残容量があり，頂点wの距離がポテンシャルより大きい場合
                        dist[w] = r = dist[v] + cost + H[v] - H[w]  # 頂点wの距離をポテンシャルで更新する
                        prv_v[w] = v    # 1つ前の頂点をvとする
                        prv_e[w] = i    # 1つ前の辺の番号を記録する
                        heappush(que, (r, w))   # 優先度付きキューに頂点wを追加する
            if dist[t] == INF:  # 終点の距離が更新されていない（流せない）場合
                return -1   # -1を返す

            for i in range(N):  # 全ての頂点に対して
                H[i] += dist[i] # ポテンシャルを更新する

            d = f; v = t    # 終点から辿る
            while v != s:   # 現在の頂点が始点と一致しない限り
                d = min(d, G[prv_v[v]][prv_e[v]][1])    # 辺の残容量との最小値をとる 
                v = prv_v[v]    # 1つ前の頂点で更新する
            f -= d  # フローをdだけ減らして更新する
            res += d*H[t] # 最小費用流に合計する
            v = t   # 終点から辿る
            while v != s:   # 現在の頂点が始点と一致しない限り
                e = G[prv_v[v]][prv_e[v]]   # 1つ前の辺
                e[1] -= d   # 残容量をdだけ減らす
                G[v][e[3]][1] += d  # 逆辺の残容量をdだけ増やす
                v = prv_v[v]    # 1つ前の頂点で更新する
        return res  # 最小費用流を返す


V, E, F = map(int, input().split()) # 頂点の数|V|，辺の数|E|，流したい流量Fの受け取り

mcf = MinCostFlow(V)    # 頂点の数Vのフローネットワークの最小費用流を求める
for i in range(E):  # 辺の数の回数だけ繰り返す
    u, v, c, d = map(int, input().split())  # 頂点uから頂点vに向かう辺の容量c，コストdの受け取り
    mcf.add_edge(u, v, c, d)    # 辺の追加
print(mcf.flow(0, V-1, F))  # 始点0から終点|V|-1へ，流量Fのフローを流したときの最小費用流を出力する