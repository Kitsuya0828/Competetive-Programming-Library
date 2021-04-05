class RUQ:
    """Range Update Query(RUQ)
    区間更新（al,al+1,...,ar−1 の値を x に更新）：計算量 O(logN)
    値取得（ai の現在の値を計算）：計算量 O(logN)
    """
    def __init__(self, n):
        # n: 処理する区間の長さ
        self.n0 = 2**(n-1).bit_length()
        self.INF = (-1, 2**31-1)
        self.data = [None]*(2 * self.n0)

    def update(self, l, r, v):
        "区間[l, r)の値をvに書き換える"
        L = l + self.n0
        R = r + self.n0
        while L < R:
            if R & 1:
                R -= 1
                self.data[R-1] = v
            if L & 1:
                self.data[L-1] = v
                L += 1
            L >>= 1
            R >>= 1
    
    def query(self, k):
        "a_iの値を取得"
        k += self.n0-1
        s = self.INF
        while k >= 0:
            if self.data[k]:
                s = max(s, self.data[k])
            k = (k-1)//2
        return s[1]
    
n,q = map(int,input().split())
ruq = RUQ(n)
for i in range(q):
    l = list(map(int,input().split()))
    if l[0]:
        print(ruq.query(l[1]))
    else:
        _,s,t,x = l
        ruq.update(s,t+1,(i,x))