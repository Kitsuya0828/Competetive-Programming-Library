# 最長共通部分列
s = input()
t = input()
slen = len(s)
tlen = len(t)

dp = [[0]*(tlen+1) for _ in range(slen+1)]

for i in range(slen):
    for j in range(tlen):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

length = dp[slen][tlen]

ans = ''
i,j = slen,tlen
while length>0:
    if s[i-1] == t[j-1]:
        ans += s[i-1]
        i -= 1
        j -= 1
        length -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        i -= 1
print(ans[::-1])