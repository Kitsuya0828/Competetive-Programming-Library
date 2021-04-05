from math import sqrt
def is_prime(x):
    """素数かどうかを判定して True, False を返す
    計算量　O(√x)
    """
    if x == 1:
        return False
    for k in range(2, int(sqrt(x)) + 1):
        if x % k == 0:
            return False
    return True


from math import sqrt
def eratos(n):
    """エラトステネスの篩（The Sieve of Eratosthenes）
    長さ(n+1)のbool型１次元リストpを返す（Trueなら素数、Falseなら合成数）
    計算量　O(nloglogn)
    """
    p = [True]*(n+1)
    p[0] = p[1] = False
    for x in range(2, int(sqrt(n))+1):
        if p[x]:
            for y in range(x*x,n+1,x):
                p[y] = False
    return p