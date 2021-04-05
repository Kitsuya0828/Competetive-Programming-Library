#各要素の出現回数を一括で取得したい場合は次のcollections.Counterが便利。
#collections.Counterの使い方
#Python標準ライブラリcollectionsにCounterクラスがある。
#コンストラクタcollections.Counter()にリストやタプルを渡すと、Counterオブジェクトが生成される。
#Counterは辞書型dictのサブクラスで、キーに要素、値に出現回数という形のデータを持つ。

import collections
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})
print(type(c))
# <class 'collections.Counter'>
print(issubclass(type(c), dict))
# True

#キーとして要素を指定するとその個数を取得できる。要素として存在しない値を指定すると0を返す。
print(c['a'])
# 4
print(c['d'])
# 0

#辞書型のメソッドも使える。キーのリスト（keys()メソッド）、値のリスト（values()）、キーと値のペアのタプルのリスト（items()メソッド）を取得したりできる。
print(c.keys())
# dict_keys(['a', 'b', 'c'])
print(c.values())
# dict_values([4, 1, 2])
print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])
#これらのメソッドはdict_keys型などのオブジェクトを返す。for文で回したりする場合はそのまま使用できる。リストに変換したい場合はlist()を使えばよい。

#出現回数順に要素を取得: most_common()メソッド
#Counterにはmost_common()メソッドがあり、(要素, 出現回数)という形のタプルを出現回数順に並べたリストを返す。
print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]
#出現回数が最も多いものは[0]、最も少ないものは[-1]のようにインデックスを指定して取得できる。要素だけ、出現回数だけを取得したい場合はさらにインデックスを指定すればOK。
print(c.most_common()[0])
# ('a', 4)
print(c.most_common()[-1])
# ('b', 1)
print(c.most_common()[0][0])
# a
print(c.most_common()[0][1])
# 4

#出現回数の少ない順に並べ替えたい場合は増分を-1としたスライスを使う。
print(c.most_common()[::-1])
# [('b', 1), ('c', 2), ('a', 4)]

#most_common()メソッドに引数nを指定すると、出現回数の多いn要素のみを返す。省略するとすべての要素。
print(c.most_common(2))
# [('a', 4), ('c', 2)]

#(要素, 出現回数)のタプルではなく、出現回数順に並べた要素・出現回数のリストが個別に欲しい場合は、以下のようにして分解できる。
values, counts = zip(*c.most_common())
print(values)
# ('a', 'c', 'b')
print(counts)
# (4, 2, 1)
#組み込み関数zip()を利用して二次元配列（ここではタプルのリスト）を転置して、アンパックして取り出している。詳しくは以下の記事を参照。
 
#重複しない要素（一意な要素）の個数（種類）をカウント
#リストやタプルに重複しない要素（一意な要素）が何個あるか（何種類あるか）をカウントする場合、上述のCounterかset()を使う。
#Counterオブジェクトの要素数が元のリストの重複しない要素の個数に等しい。Counterオブジェクトの要素数はlen()で取得できる。
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)
print(len(c))
# 3

#集合型setのコンストラクタset()も使える、
#set型は重複した要素をもたないデータ型で、コンストラクタset()にリストを渡すと、重複する値は無視されて一意な値のみが要素となるset型のオブジェクトを返す。これの要素数を同じくlen()で取得する。
print(set(l))
# {'b', 'a', 'c'}
print(len(set(l)))
# 3

#条件を満たす要素の個数をカウント
#リストやタプルに特定の条件を満たす要素が何個あるかカウントするには、条件を満たす要素のリストをリスト内包表記で生成して、その個数をlen()で取得する。
#数値のリストに対して「0以下」や「奇数」の要素の数を取得する例。
l = list(range(-5, 6))
print(l)
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print([i for i in l if i < 0])
# [-5, -4, -3, -2, -1]
print(len([i for i in l if i < 0]))
# 5
print([i for i in l if i % 2 == 1])
# [-5, -3, -1, 1, 3, 5]
print(len([i for i in l if i % 2 == 1]))
# 6

#文字列のリストに対する条件の例。
l = ['apple', 'orange', 'banana']
print([s for s in l if s.endswith('e')])
# ['apple', 'orange']
print(len([s for s in l if s.endswith('e')]))
# 2

#出現回数の条件でカウントする場合、目的によってcount()メソッドとcollections.Counterを使い分ける。出現回数が条件を満たす要素の種類をカウントする場合はcollections.Counterを使う。
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
print([i for i in l if l.count(i) >= 2])
# ['a', 'a', 'a', 'a', 'c', 'c']
print(len([i for i in l if l.count(i) >= 2]))
# 6

c = collections.Counter(l)
print([i[0] for i in c.items() if i[1] >= 2])
# ['a', 'c']
print(len([i[0] for i in c.items() if i[1] >= 2]))
# 2

#文字列の単語の出現個数をカウント
#具体的な例として、文字列に登場する単語の出現個数を数えてみる。
#まず、不必要なカンマ,や.をreplace()メソッドで空文字列と置換し、削除する。さらにsplit()メソッドで空白で区切ってリスト化する。
s = 'government of the people, by the people, for the people.'
s_remove = s.replace(',', '').replace('.', '')
print(s_remove)
# government of the people by the people for the people
word_list = s_remove.split()
print(word_list)
# ['government', 'of', 'the', 'people', 'by', 'the', 'people', 'for', 'the', 'people']

#リスト化できれば、各単語の出現回数や出現する単語の種類を取得したり、collections.Counterのmost_common()で最も出現回数の多い単語を取得したりできる。
print(word_list.count('people'))
# 3
print(len(set(word_list)))
# 6
c = collections.Counter(word_list)
print(c)
# Counter({'the': 3, 'people': 3, 'government': 1, 'of': 1, 'by': 1, 'for': 1})
print(c.most_common()[0][0])
# the


#文字列の文字の出現個数をカウント
#文字列もシーケンス型なので、count()メソッドを使ったり、collections.Counter()のコンストラクタの引数に渡したりすることができる。
s = 'supercalifragilisticexpialidocious'
print(s.count('p'))
# 2
c = collections.Counter(s)
print(c)
# Counter({'i': 7, 's': 3, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'o': 2, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})

#出現回数の多い文字トップ5を取得する例。
print(c.most_common(5))
# [('i', 7), ('s', 3), ('c', 3), ('a', 3), ('l', 3)]
values, counts = zip(*c.most_common(5))
print(values)
# ('i', 's', 'c', 'a', 'l')