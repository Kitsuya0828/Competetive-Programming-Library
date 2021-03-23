from itertools import accumulate
N, K = map(int, input().split())
a = [0] + list(map(int, input().split()))
acc = list(accumulate(a))
ans = 0
l = 0
for r in range(1, N+1):
    while acc[r] - acc[l] >= K:
        ans += N + 1 - r
        l += 1
print(ans)


from itertools import accumulate
n,m,k = map(int, input().split())
a = list(map(int,input().split()))[::-1]
b = list(map(int,input().split()))

l = [0] + a + b
acc = list(accumulate(l))

# print(acc)

ans = 0
l = 0
for r in range(1, n+m+1):
    while acc[r] - acc[l] > k:
        l += 1
    # print(l,r)
    if l <= n and r >= n:
        ans = max(ans,r-l)
    # print(ans)
print(ans)