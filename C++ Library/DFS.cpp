#include <iostream>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;

// 深さ優先探索   O(|V|+|E|)
vector<bool> seen;
void dfs(const Graph &G, int v) {
    seen[v] = true;  // v を訪問済みにする

    // v から行ける各頂点 next_v について
    for (auto next_v : G[v]) {
        if (seen[next_v]) continue;  // next_v が探索済みならば探索しない
        dfs(G, next_v);  // 再帰的に探索
    }
}



int main() {
    // 頂点数と辺数
    int N, M;
    cin >> N >> M;

    // グラフ入力受け取り（ここでは有向グラフを想定）
    Graph G(N);
    for (int i=0; i<M; ++i) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
    }

    // 探索
    // 一般にグラフ G において、ある１つの頂点 v ⊂ V に対して dfs(G, v) を呼び出しても、全ての頂点が探索されるとは限らない
    // 未訪問頂点がなくなるまで関数 dfs を呼び出している
    seen.assign(N, false);  // 初期状態では全頂点が未訪問
    for (int v=0; v<N; ++v) {
        if (seen[v]) continue;  // すでに訪問済みなら探索しない
        dfs(G, v);
    }
}

// --------------------------------------------------------------

// s-tパスがあるかどうかを深さ優先探索を用いて判定
int main() {
    // 頂点数と変数、s と t
    int N, M, s, t;
    cin >> N >> M >> s >> t;

    // グラフ入力受け取り
    Graph G(N);
    for (int i=0; i<M; ++i) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
    }
    // 頂点 s をスタートとした探索
    seen.assign(N, false);  // 全頂点を「未訪問」に初期化
    dfs(G,s);

    // t にたどり着けるかどうか
    if (seen[t]) cout << "Yes" << endl;
    else cout << "No" << endl;
}

// --------------------------------------------------------------

#include <iostream>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;

// 二部グラフ（bipartite graph）判定
// 「白色の頂点同士が隣接することはなく、黒色の頂点同士が隣接することもない」という条件を満たすように、各頂点を白色または黒色に塗分けることが可能なグラフ
vector<int> color;
bool dfs_bipartite(const Graph &G, int v, int cur = 0) {
    color[v] = cur;
    for (auto next_v : G[v]) {
        // 隣接頂点がすでに色確定していた場合
        if (color[next_v] != -1) {
            // 同じ色が隣接した場合は二部グラフではない
            if (color[next_v] == cur) return false;

            // 色が確定していた場合には探索しない
            continue;
        }

        // 隣接頂点の色を変えて、再帰的に探索
        // false が返ってきたら false を返す
        if (! dfs_bipartite(G, next_v, 1-cur)) return false;
    }
    return true;
}

int main() {
    // 頂点数と辺数
    int N, M;
    cin >> N >> M;

    // グラフ入力受け取り
    Graph G(N);
    for (int i=0; i<M; ++i) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    // 探索
    color.assign(N,-1);
    bool is_bipartite = true;
    for (int v=0; v<N; ++v) {
        if (color[v] != -1) continue;  // v が探索済みの場合は探索しない
        if (! dfs_bipartite(G,v)) is_bipartite = false;
    }

    if (is_bipartite) cout << "Yes" << endl;
    else cout << "No" << endl;
}

// --------------------------------------------------------------

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using Graph = vector<vector<int>>;

// トポロジカルソート   O(|V|+|E|)
// トポロジカルソート可能 ⇔ 有向グラフが DAG(Directed Acyclic Graph)である、すなわちグラフが有向サイクルを持たない
// 深さ優先探索における再帰関数を抜けた順序に頂点を並べ、それを逆順に並べ直すことでトポロジカルソート順が得られる
vector<bool> seen;
vector<int> order;  // トポロジカルソート順を表す
void Topological_Sort(const Graph &G, int v) {
    seen[v] = true;
    for (auto next_v : G[v]) {
        if (seen[next_v]) continue;  // すでに訪問済みならば探索しない
        Topological_Sort(G, next_v);
    }

    // v-out を記録する
    order.push_back(v);
}

int main() {
    int N,M;
    cin >> N >> M;   // 頂点数と枝数
    Graph G(N);   // 頂点数 N のグラフ
    for (int i=0; i<M; ++i) {
        int a,b;
        cin >> a >> b;
        G[a].push_back(b);
    }

    // 探索
    seen.assign(N, false);   // 初期状態では全頂点が未訪問
    order.clear();   // トポロジカルソート順
    for (int v = 0; v<N; ++v) {
        if (seen[v]) continue;  // すでに訪問済みならば探索しない
        Topological_Sort(G,v);
    }
    reverse(order.begin(), order.end());  // 逆順に

    // 出力
    for (auto v : order) cout << v << "->";
    cout << endl;
}