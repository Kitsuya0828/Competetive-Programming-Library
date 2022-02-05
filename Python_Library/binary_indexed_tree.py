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