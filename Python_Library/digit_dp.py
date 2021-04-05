# 分かりやすい → https://torus711.hatenablog.com/entry/20150423/1429794075

# ---------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

s = str(input().strip())
K = int(input())
len_N = len(s)

# dp[ i ][ smaller ][ k ] := i 桁目までで 0 以外の数を使用したのが k 個である数の個数。
# i 桁目までの部分について、 smaller が true なら N より小さく、false なら N と等しい数であるとする。
 
dp = [[[0 for k in range(5)] for j in range(2)] for i in range(110)]
dp[0][0][0] = 1

for i in range(len_N):
  for k in range(K+1):
    # i桁目まででNより小さいならi+1桁目は何でも良い
    dp[i+1][1][k+1] += dp[i][1][k]*9  # i+1桁目が0以外
    dp[i+1][1][k] += dp[i][1][k]  # i+1桁目が0
    
    ni = int(s[i])

    # i桁目までNと同じで、i+1桁目はNより小さい数の時
    if ni > 0:
      dp[i+1][1][k+1] += dp[i][0][k] * (ni-1)  # i+1桁目が0以外
      dp[i+1][1][k] += dp[i][0][k]  # i+1桁目が0
    # i桁目までNと同じで、i+1桁目もNと同じ数の時
    if ni > 0:
      dp[i+1][0][k+1] = dp[i][0][k]  # i+1桁目が0以外
    else:
      dp[i+1][0][k] = dp[i][0][k]  # i+1桁目が0

print(dp[len_N][0][K]+dp[len_N][1][K])

# ---------------------------------------------------------------------

mod = 10**9 + 7
d = int(input())
n = input()
ln = len(n)

# dp[i][j][m]:i桁目までを見て、今作成している数字の桁和をDで割った余りがj
# mは今作成している数字がN未満であることが確定しているかどうか
dp = [[[0 for m in range(2)] for j in range(105)] for i in range(10005)]
dp[0][0][0] = 1

for i in range(ln):
    for j in range(d):
        ni = int(n[i])
        for k in range(10):
            if k < ni:
                dp[i+1][(j+k)%d][1] = (dp[i+1][(j+k)%d][1]+dp[i][j][1]+dp[i][j][0])%mod
            elif k == ni:
                dp[i+1][(j+k)%d][1] = (dp[i+1][(j+k)%d][1]+dp[i][j][1])%mod
                dp[i+1][(j+k)%d][0] = (dp[i+1][(j+k)%d][0]+dp[i][j][0])%mod
            else:
                dp[i+1][(j+k)%d][1] = (dp[i+1][(j+k)%d][1]+dp[i][j][1])%mod
print(dp[ln][0][1]+dp[ln][0][0]-1)