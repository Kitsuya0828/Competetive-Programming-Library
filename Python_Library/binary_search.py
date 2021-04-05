a,b,x = map(int,input().split())
def f(n):
    if a*n + b*len(str(n)) <= x:
        return True
    else:
        return False
left = 0 # 必ず「買える」所
right = 10**9+1 # 必ず「買えない」所
while right - left > 1:
    middle = (left + right)//2
    if f(middle):
        left = middle
    else:
        right = middle
print(left) # 二分探索が終わった時に出力するのは、left