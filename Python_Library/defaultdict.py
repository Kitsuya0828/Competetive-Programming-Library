from collections import defaultdict

N = int(input())
dict = defaultdict(int)
ans = 0
for i in range(N):
    s = ''.join(sorted(input()))
    ans += dict[s]
    dict[s] += 1
print(ans)
