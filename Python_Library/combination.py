import itertools
#(a, b, c, d, e)の並べ方を考えてみます。
seq = ('a', 'b', 'c', 'd', 'e')

#組み合わせ
#並べる際の順序を無視する場合は組み合わせとなります。
#例えば、(a, b, c)と(a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)は全て同じとみなします。

#(a, b, c, d, e)から5つ順序を無視して並べる方法、すなわち組み合わせは1通りです。
#組み合わせを求める際はcombinationsを使います。 第2引数が必須なことに注意です。
list(itertools.combinations(seq,5))
#[('a', 'b', 'c', 'd', 'e')]

#(a, b, c, d, e)から3つ選ぶ組み合わせを考えます。
#組み合わせは、5C3=5P33!=105C3=5P33!=10 通りです 。
list(itertools.combinations(seq,3))
'''[('a', 'b', 'c'),
 ('a', 'b', 'd'),
 ('a', 'b', 'e'),
 ('a', 'c', 'd'),
 ('a', 'c', 'e'),
 ('a', 'd', 'e'),
 ('b', 'c', 'd'),
 ('b', 'c', 'e'),
 ('b', 'd', 'e'),
 ('c', 'd', 'e')]'''

#直積
#最後に直積を考えます。
#直積とは A={a, b, c}, B={d, e}のような2つの集合が与えられたとすると
#A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}
#を返すような操作のことです。Aから一つ、Bから一つ要素を取り、組としています。
#直積はproductを使用します。

A = ('a', 'b', 'c')
B = ('d', 'e')
C = ('f')
list(itertools.product(A, B))
#[('a', 'd'), ('a', 'e'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e')]

list(itertools.product(A, B, C))
'''[('a', 'd', 'f'),
 ('a', 'e', 'f'),
 ('b', 'd', 'f'),
 ('b', 'e', 'f'),
 ('c', 'd', 'f'),
 ('c', 'e', 'f')]'''
#何が嬉しいのかというと、直積を使うとfor文のネストを減らせます。

for i in A:
     for j in B:
         print(i, j)

'''a d
   a e
   b d
   b e
   c d
   c e'''

for i, j in itertools.product(A, B):
     print(i ,j)
'''a d
   a e
   b d
   b e
   c d
   c e'''
#n個のAの直積、An=A×A×⋯×AAn=A×A×⋯×Aを求めるときは、キーワード引数repeatで指定します。

#n = 3のときは次の通りになります。
#いわゆる重複順列というやつと同じことです。
for i in itertools.product(A, repeat=3):
     print(i)
'''('a', 'a', 'a')
   ('a', 'a', 'b')
   ('a', 'a', 'c')
   ('a', 'b', 'a')
   ('a', 'b', 'b')
   ('a', 'b', 'c')
   ('a', 'c', 'a')'''
    #以下略


#おまけ 重複組み合わせ
#重複順列をやったので、重複組合せもついでにやっときます。
#重複組合せはcombinations_with_replacementを使います
list(itertools.combinations_with_replacement(A, 3))
'''[('a', 'a', 'a'),
    ('a', 'a', 'b'),
    ('a', 'a', 'c'),
    ('a', 'b', 'b'),
    ('a', 'b', 'c'),
    ('a', 'c', 'c'),
    ('b', 'b', 'b'),
    ('b', 'b', 'c'),
    ('b', 'c', 'c'),
    ('c', 'c', 'c')]'''