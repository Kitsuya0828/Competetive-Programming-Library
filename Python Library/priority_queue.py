import sys
input = sys.stdin.readline
import heapq

n,m = map(int,input().split())
l = list(map(int,input().split()))
s = sum(l)
for i in range(n):
    l[i] *= (-1)

heapq.heapify(l)

discount = 0

for i in range(m):
    x = (-heapq.heappop(l))
    heapq.heappush(l,-(x//2))
    discount += (x-x//2)

print(s-discount)