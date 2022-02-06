from collections import deque, defaultdict  # collectionsモジュールからdeque，defaultdictをimport
import sys  # sysモジュールのimport
sys.setrecursionlimit(2**20)    # 再帰回数の上限を変更

class LowLink:
    """与えられたグラフの関節点と橋を求める
    """
    def __init__(self, v):
        """コンストラクタ

        Args:
            v : グラフの隣接リスト
        """
        self.size = len(v)  # グラフの頂点の数
        self.v = v  # グラフの隣接リスト
        self.pre = [None]*self.size # 深さ優先探索で頂点を何番目に訪問したかのリスト
        self.low = [None]*self.size # lowlinkのリスト
        self.articulations = [] # 関節点のリスト
        self.bridges = []   # 橋のリスト
        for x in range(self.size):  # グラフの各頂点について
            if self.pre[x] is None: # 未訪問ならば
                self.cnt = 0    # カウンタの初期化
                self.dfs(x, None)   # 深さ優先探索により橋と関節点を求める
    
    def dfs(self, x, prev):
        """深さ優先探索により橋と関節点を求め，lowlinkを返す
        
        Args:
            x : 現在訪問しているノード
            prev : 1つ前のノード
        """
        self.pre[x] = self.low[x] = self.cnt # 初期化
        self.cnt += 1 # カウンタをインクリメントする
        is_articulation = False # 関節点かどうかを記録する
        n = 0 # xから出ている子の個数
        for y in self.v[x]: # xから出ている全ての子yについて
            if self.pre[y] is None: # yが未訪問ならば
                n += 1  # xから出ている子の個数を1増やす
                low_y = self.dfs(y, x)  # 再帰呼び出し
                if low_y < self.low[x]: # 最小値を更新できるなら
                    self.low[x] = low_y # xのlowlinkを更新する
                if self.pre[x] <= low_y:    # 深さ優先探索木におけるxの訪問順がlowlink以下ならば
                    if self.pre[x]: # 深さ優先探索木の根でなければ
                        is_articulation = True  # 関節点である
                    if self.pre[x] < low_y: # # 深さ優先探索木におけるxの訪問順がlowlink未満ならば
                        self.bridges.append((min(x,y), max(x,y)))    # 橋のリストに追加する
            else:   # yが訪問済みならば
                if y != prev and self.pre[y] < self.low[x]: # yが1つ前のノードでなくて，yの訪問順がlowlink未満ならば
                    self.low[x] = self.pre[y]   # xのlowlinkをyの訪問順で更新する
        
        if prev is None and n > 1:  # xが根であり，かつ根xから子が2個以上出てるなら
            is_articulation = True  # 関節点である
        
        if is_articulation: # 関節点ならば
            self.articulations.append(x)    # 関節点のリストに追加する
        
        return self.low[x]  # lowlinkのリストを返す

V, E = map(int, input().split())    # 頂点の数と辺の数の受け取り
G = defaultdict(list)   # グラフの隣接リスト
for _ in range(E):  # 辺の数の回数だけ繰り返す
    s, t= map(int, input().split()) # 頂点s，ｔの受け取り
    G[s].append(t)  # 頂点sの隣接リストにtを追加する
    G[t].append(s)  # 頂点tの隣接リストにsを追加する

lowlink = LowLink(G)    # グラフGのlowlinkを求める

arti = lowlink.articulations    # 関節点のリストを取得する
arti.sort() # 関節点を昇順に並べ替える
for a in arti:  # 全ての関節点について
    print(a)    # 頂点番号を出力する

brid = lowlink.bridges    # 橋のリストを取得する
brid.sort() # 橋を昇順に並べ替える
for s,t in brid:  # 全ての橋について
    print(s, t)    # 頂点番号の組を出力する