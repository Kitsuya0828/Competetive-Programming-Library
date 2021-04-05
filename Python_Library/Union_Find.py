class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n+1)]  # 各要素の親要素の番号を格納するリスト
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)  # 根（ルート）の場合、そのグループの要素数を格納するリスト

    # 要素 x が属するグループの根を返す
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 要素 x が属するグループと要素 y が属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 要素 x, y が同じグループに属するかどうかを返す
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    
    # 要素 x が属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(1,self.n+1) if self.find(i) == root]

    # 要素 x が属するグループのサイズ（要素数）を返す
    def get_size(self, x):
        return self.size[self.find(x)]

    # すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.par) if x == i and i != 0]
    
    # グループの数を返す
    def group_count(self):
        return len(self.roots())
    
    # {ルート要素: [そのグループに含まれる要素のリスト], ...} の辞書を返す
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
n,q = map(int,input().split())
uf = UnionFind(n)
for i in range(q):
    p,a,b = map(int,input().split())
    if p:
        print(1 if uf.same_check(a,b) else 0)
        continue
    else:
        uf.union(a,b)