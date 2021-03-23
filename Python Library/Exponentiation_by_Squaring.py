'''
pow(base, exp[, mod])
base の exp 乗を返します; 
mod があれば、base の exp 乗に対する mod の剰余を返します 
(pow(base, exp) % mod より効率よく計算されます)。
二引数の形式 pow(base, exp) は、冪乗演算子を使った base**exp と等価です。
'''

url = 'https://tane-no-blog.com/976/'

# pow を実装したコード
# def pow(x,n):
    # res = 1
    # while n > 0:
        # if n&1 == 1:
            # res *= x
        # x *= x
        # n >>= 1
    # return res

n,a,b = map(int,input().split())

# pow を用いた組み合わせ計算の高速化
mod = 10**9 + 7
def comb(N,x):
    numerator = 1
    for i in range(N-x+1,N+1):
        numerator = numerator * i % mod
    denominator = 1
    for j in range(1,x+1):
        denominator = denominator * j % mod
    d = pow(denominator,mod-2,mod)
    return numerator * d % mod

A = comb(n,a)
B = comb(n,b)

print((pow(2,n,mod)-1-A-B) % mod)