#include <iostream>
#include <vector>
using namespace std;

// Union-Find
struct UnionFind {
    vector<int> par, siz;

    // 初期化
    UnionFind(int n) : par(n,-1), siz(n,1) {}

    // 根を求める
    int root(int x) {
        if (par[x] == -1) return x;  // x が根の場合は x を直接返す
        else return par[x] = root(par[x]);  // x の親 par[x] を根に設定する（経路圧縮）
    }

    // x と y が同じグループに属するかどうか（根が一致するかどうか）
    bool issame(int x, int y) {
        return root(x) == root(y);
    }

    // x を含むグループと y を含むグループを併合する
    bool unite(int x, int y) {
        // x, y をそれぞれ根まで移動する
        x = root(x); y = root(y);

        // すでに同じグループのときは何もしない
        if (x==y) return false;

        // union by size （y 側のサイズが小さくなるようにする）
        if (siz[x] < siz[y]) swap(x,y);

        // y を x の子とする
        par[y] = x;
        siz[x] += siz[y];
        return true;
    }

    // x を含むグループのサイズ
    int size(int x) {
        return siz[root(x)];
    }
};

int main() {
    UnionFind uf(7);  // {0},{1},{2},{3},{4},{5},{6}

    uf.unite(1,2);  // {0},{1,2},{3},{4},{5},{6}
    uf.unite(2,3);  // {0},{1,2,3},{4},{5},{6}
    uf.unite(5,6);  // {0},{1,2,3},{4},{5,6}

    cout << uf.issame(1,3) << endl;  // true
    cout << uf.issame(2,5) << endl;  // false

    uf.unite(1,6);  // {0},{1,2,3,5,6},{4}
    cout << uf.issame(2,5) << endl;  // true
}


// --------------------------------------------------------------

// 無向グラフの連結成分の個数を求める
// Union-Find中の「根付き木の根となっている頂点」の個数を数える
int main() {
    // 頂点数と辺数
    int N,M;
    cin >> N >> M;

    // Union-Find を要素数 N で初期化
    UnionFind uf(N);

    // 各辺に対する処理
    for (int i=0; i<M; ++i) {
        int a, b;
        cin >> a >> b;
        uf.unite(a,b);  // a を含むグループと b を含むグループを併合する
    }

    // 集計
    int res = 0;
    for (int x = 0; x < N; ++x) {
        if (uf.root(x) == x) ++res;
    }
    cout << res << endl;
}