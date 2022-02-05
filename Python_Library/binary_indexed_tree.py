class BIT:
    """Binary Indexed Tree (Fenwick Tree)
    """
    def __init__(self, n):
        """コンストラクタ
        
        Args:
            n : 配列の要素数
        """
        self.tree = [0]*(n+1)   # データの格納先（1-indexed）．初期値は0
        self.n = n  # 配列の要素数
    
    def add(self, i, v):
        """1点加算（i番目の値にvを加算する）

        Args:
            i : 加算する要素のインデックス
            v : 加算する値
        """
        while i <= self.n:  # iから始める
            self.tree[i] += v   # i番目の値にvを加える
            i += i & -i # iに最後の1が立っているビットを加算する（∵負の数はビット反転+1で表される）
        
    def _sum(self, i):
        """最初からi番目までの和の取得

        Args:
            i : 和を求める最後の要素のインデックス
        """
        ret = 0 # 和を0で初期化
        while i:    # iから始める
            ret += self.tree[i] # i番目の値を合計していく
            i -= i & -i # iに最後の1が立っているビットを減算する（∵負の数はビット反転+1で表される）
        return ret  # 最初からi番目までの和を返す
    
    def sum(self, l, h):
        """l番目からh番目までの和の取得

        Args:
            l : 左端の要素のインデックス
            h : 右端の要素のインデックス
        """
        return self._sum(h) - self._sum(l-1)    # （最初からh番目までの和）-（最初からl-1番目までの和）を返す
    
# 線分交差問題（マンハッタン幾何）
import bisect   # bisectモジュールのimport

n = int(input())    # 線分の数の受け取り
vx = [] # 端点のリスト
xs = set()  # y軸に平行な線分のx座標のセット
for _ in range(n):  # 線分の数の回数だけ
    x1, y1, x2, y2 = map(int, input().split())  # 線分の端点の座標の受け取り
    if x1 == x2:    # y軸に平行な線分の場合
        if y1 > y2: # y1がy2よりも大きいならば
            y1, y2 = y2, y1 # y1とy2を入れ替えてy2が必ず大きくなるようにする
        vx.append((y1, float('-inf'), x1))  # 端点のソート基準は，[下端点]→左端点→右端点→上端点の優先度
        vx.append((y2, float('inf'), x2))   # 端点のソート基準は，下端点→左端点→右端点→[上端点]の優先度
        xs.add(x1)  # セットに線分のx座標を追加する
    else:   # x軸に平行な線分の場合
        if x1 > x2: # x1がx2よりも大きいならば
            x1, x2 = x2, x1 # x1とx2を入れ替えてx2が必ず大きくなるようにする
        vx.append((y1, x1, x2)) # 端点のソート基準は，下端点→[左端点→右端点]→上端点の優先度
vx.sort()   # 端点のリストを昇順に並べ替える

bit = BIT(len(xs))  # 二分探索木
xs = [float('-inf')] + sorted(xs)   # 二分探索のための番兵を設置
ix = {v: i for i, v in enumerate(xs)}   # y軸に平行な線分のx座標の，二分探索木におけるインデックス
ans = 0 # 交点の数を0で初期化

for y, j, x2 in vx: # 全ての端点について
    if j == float('-inf'):  # 下端点ならば
        bit.add(ix[x2], 1)   # 二分探索木に，線分の下端点のx座標を追加
    elif j == float('inf'): # 上端点ならば
        bit.add(ix[x2], -1) # 二分探索木から，線分の上端点のx座標を削除
    else:   # 左右端点ならば
        l = bisect.bisect_left(xs, j)   # 線分の左端点を二分探索木のインデックスで二分探索
        r = bisect.bisect(xs, x2) - 1   # 線分の右端点を二分探索木のインデックスで二分探索
        ans += bit.sum(l, r)    # 二分探索木で[l,r]の範囲で交点の数を求める
        
print(ans)  # 交点の数を出力する