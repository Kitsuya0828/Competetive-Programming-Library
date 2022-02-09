class FordFulkerson:
    """フォード・ファルカーソンのアルゴリズム
    最大流を求める
    """
    def __init__(self, N):
        """コンストラクタ

        Args:
            N : フローネットワークの頂点の数
        """
        self.N = N  # 頂点の数
        self.G = [[] for i in range(N)] # フローネットワークGの隣接リスト

    def add_edge(self, fr, to, cap):
        """フローネットワークに辺を追加する

        Args:
            fr : 辺の始点
            to : 辺の終点
            cap : 辺の容量
        """
        forward = [to, cap, None]   # 辺：終点，残容量，逆辺
        forward[2] = backward = [fr, 0, forward]    # 逆辺：始点，残容量0，辺
        self.G[fr].append(forward)    # 辺を追加する
        self.G[to].append(backward)    # 逆辺を追加する

    def dfs(self, v, t, f):
        """深さ優先探索で始点から終点への経路を見つけ，経路上の辺に流すフローを返す

        Args:
            v : 深さ優先探索の始点
            t : 深さ優先探索（とフローネットワーク）の終点
            f : フロー
        """
        if v == t:  # 始点と終点が一致した場合
            return f    # フローをそのまま返す
        used = self.used    # 訪問済みリスト
        used[v] = 1 # 始点vを訪問済みにする
        for e in self.G[v]: # vに隣接する全ての辺に対して
            w, cap, rev = e # 辺の始点，辺の残容量，逆辺
            if cap and not used[w]: # 残容量があり，辺の終点が訪問済みでなければ
                d = self.dfs(w, t, min(f, cap)) # 再帰的に，辺の終点からフローネットワークの終点までの深さ優先探索を行う
                if d:   # wからtまで流せる任意の経路が見つかった場合
                    e[1] -= d   # 辺の残容量をフローdだけ減らす
                    rev[1] += d # 逆辺の逆容量をフローdだけ増やす
                    return d    # 流したフローを返す
        return 0    # vに隣接する辺がなければ0を返す

    def flow(self, s, t):
        """フローネットワークの始点sから終点tへの最大流を返す

        Args:
            s : フローネットワークの始点
            t : フローネットワークの終点
        """
        flow = 0    # 最大流を0で初期化する
        f = INF = 10**9+7   # 最大の数
        N = self.N  # 頂点の数
        while f:    # 流せるフローが0にならない限り繰り返す
            self.used = [0]*N   # 訪問済みリスト
            f = self.dfs(s, t, INF) # sからtまで辿れるような増大道を深さ優先探索で見つけ，流せるだけのフローを求める
            flow += f   # 最大流に流せるフローを合計する
        return flow # 最大流を返す

    
V, E = map(int, input().split())    # 頂点の数|V|と辺の数|E|の受け取り
ff = FordFulkerson(V)   # フォードファルカーソン法で最大流を求める
for i in range(E):  # 辺の数だけ繰り返す
    u, v, c = map(int, input().split()) # 頂点uから頂点vに向かう辺の容量cの受け取り
    ff.add_edge(u, v, c)    # 辺の追加
print(ff.flow(0, V-1))  # 始点0から終点|V|-1までの最大流を出力する