n = input()
op_cnt = len(n) - 1  # すき間の個数
for i in range(2 ** op_cnt):
    op = ["-"] * op_cnt  # あらかじめ ["-", "-", "-"] というリストを作っておく
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"  # フラグが立っていた箇所を "+" で上書き

    formula = ""
    for p_n, p_o in zip(n, op + [""]):
        formula += (p_n + p_o)
    if eval(formula) == 7:
        print(formula + "=7")
        break

# ABC190C
import itertools
N, M = map(int, input().split())
cond = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
choice = [tuple(map(int, input().split())) for i in range(K)]
ans = 0
print(*choice)
for balls in itertools.product(*choice):  #問題によっては直積集合の方が使いやすい
    print(balls)
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in cond)
    if ans < cnt:
        ans = cnt
print(ans)