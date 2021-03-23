def solve(X, Y, M):
    """ X^K ≡ Y (mod M) となるような K を求める
    計算量　O(√M)
    """
    D = {1:0}
    sq = int(M**0.5)+1

    # Baby-step
    Z = 1
    for i in range(sq):
        Z = Z * X % M
        D[Z] = i+1
    
    if Y in D:
        return D[Y]
    

    # Giant-step
    R = pow(Z,M-2,M)  # R = X^(-sq)

    for i in range(1,sq+1):
        Y = Y * R % M
        if Y in D:
            return D[Y] + i*sq
        return -1

