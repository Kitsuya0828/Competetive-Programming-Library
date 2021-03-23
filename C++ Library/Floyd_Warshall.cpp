#include <iostream>
#include <vector>
using namespace std;

// 無限大を表す値
const long long INF = 1LL << 60;

int main() {
    // 頂点数、辺数
    int N, M;
    cin >> N >> M;

    // dp 配列（ INF で初期化する）
    vector<vector<long long>> dp(N, vector<long long>(N, INF));

    // dp 初期条件
    for (int e=0; e<M; ++e) {
        int a, b;
        long long w;
        cin >> a >> b >> w;
        dp[a][b] = w;
    }
    for (int v=0; v<N; ++v) dp[v][v] = 0;

    // dp 遷移（フロイド・ワーシャル法）
    // 配列 dp は 3 次元にする必要はなく、k から k+1 への更新を in-place に実現する
    for (int k=0; k<N; ++k) {
        for (int i=0; i<N; ++i) {
            for (int j=0; j<N; ++j) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
            }
        }
    }

    // 結果出力
    // もし dp[v][v] < 0 なら負経路が存在する
    bool exist_negative_cycle = false;
    for (int v=0; v<N; ++v) {
        if (dp[v][v] < 0) exist_negative_cycle = true;
    }
    if (exist_negative_cycle) {
        cout << "NEGATIVE CYCLE" << endl;
    }
    else {
        for (int i=0; i<N; ++i) {
            for (int j=0; j<N; ++j){
                if (j) cout << " ";
                if (dp[i][j] < INF/2) cout << dp[i][j];
                else cout << "INF";
            }
            cout << endl;
        }
    }
}


// dp[k][i][j] := 頂点 0,1,...,k-1 のみを中継頂点として通ってよいとした場合の、頂点 i から頂点 j への最短路長
// 新たに使用できる頂点 k を使用しない場合：dp[k][i][j]
// 新たに使用できる頂点 k を使用する場合：dp[k][i][k]+dp[k][k][j]
// この 2 通りの選択肢のうち、値が小さい方を採用
// dp[k+1][i][j] = min(dp[k][i][j], dp[k][i][k] + dp[k][k][j])