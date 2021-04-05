class RMQ:
    """Range Minimum Query(RMQ)
    更新（ai の値を x に更新）：計算量 O(logN)
    区間最小値（al,al+1,...,ar−1 の最小値を求める）：計算量 O(logN)
    """
    def __init__(self, n):
        # n: 処理する区間の長さ
        self.n0 = 2**(n-1).bit_length()
        self.INF = 2**31-1
        self.data = [self.INF]*(2 * self.n0)

    def update(self, k, x):
        "a_k の値を x に更新"
        k += self.n0-1
        self.data[k] = x
        while k >= 0:
            k = (k-1)//2
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])
    
    def query(self, l, r):
        "区間[l,r)の最小値"
        L = l + self.n0
        R = r + self.n0
        s = self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])
            if L & 1:
                s = min(s, self.data[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return s

n,q = map(int,input().split())
rmq = RMQ(n)
for i in range(q):
    com,x,y = map(int,input().split())
    if com:
        print(rmq.query(x,y+1))
    else:
        rmq.update(x,y)