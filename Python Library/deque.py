#キュー（queue, FIFO）として使う
#キュー（queue）は先入れ先出し（FIFO: First In, First Out）のデータ構造。キューでは、データを入れることをエンキュー（enqueue）、取り出すことをデキュー（dequeue）呼ぶ。
#dequeをキューとして使うには、エンキューとしてappend()、デキューとしてpopleft()を使えばよい。
from collections import deque
d = deque(['a', 'b', 'c'])
print(d)
# deque(['a', 'b', 'c'])
d.append('d')
print(d)
# deque(['a', 'b', 'c', 'd'])
print(d.popleft())
# a
print(d)
# deque(['b', 'c', 'd'])

#スタック（stack, LIFO）として使う
#スタック（stack）は後入れ先出し（LIFO: Last In, First Out）のデータ構造。スタックでは、データを入れることをプッシュ（push）、取り出すことをポップ（pop）と呼ぶ。
#dequeをスタックとして使うには、プッシュとしてappend()、ポップとしてpop()を使えばよい。
from collections import deque
d = deque(['a', 'b', 'c'])
print(d)
# deque(['a', 'b', 'c'])
d.append('d')
print(d)
# deque(['a', 'b', 'c', 'd'])
print(d.pop())
# d
print(d)
# deque(['a', 'b', 'c'])

#デック（deque, 両端キュー）として使う
#デック（deque）は両端（先頭または末尾）で要素を追加・削除できるキューで、両端キューや双方向キューなどとも呼ばれる。
#これまでの例のように、dequeではappend(), appendleft(), pop(), popleft()で両端の要素の追加・削除が可能。

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#リストでは先頭の要素を削除して取り出すpop(0)、先頭に要素を追加するinsert(0, v)などの操作でO(n)のコストを必要とするが、dequeでは先頭・末尾の要素を追加・削除するappend(), appendleft(), pop(), popleft()がすべてO(1)で実行できる。
#Deque はどちらの側からも append と pop が可能で、スレッドセーフでメモリ効率がよく、どちらの方向からもおよそ O(1) のパフォーマンスで実行できます。
#list オブジェクトでも同様の操作を実現できますが、これは高速な固定長の操作に特化されており、内部のデータ表現形式のサイズと位置を両方変えるような pop(0) や insert(0, v) などの操作ではメモリ移動のために O(n) のコストを必要とします。
#一方、両端以外の要素に対する[]によるアクセス（取得）はリストのほうが有利。
#（dequeは）d[-1] などの添え字による参照をサポートしています。 両端への添字アクセスは O(1) ですが、中央部分へは O(n) と遅くなります。 高速なランダムアクセスが必要であればリストを使ってください。
#要素の追加・取り出し（削除）・アクセス（取得）が両端のみ → deque
#両端以外の要素に頻繁にアクセス → リスト
#明確にキューやスタック、デックとしてデータを扱いたい、という場合は dequeを使ったほうがよい。
#ただ、環境や条件にもよるが、要素数が数百個や数千個程度であれば、リストでもdequeでも体感できるほどの処理速度の差はない。ミリ秒オーダーで処理時間を切り詰めたいアプリケーションや競技プログラミングでもない限り、多くの場合はリストを使っておけば特に問題はないはず。
#とはいえ、適切なデータ構造を選択するという意識を持っておくことも大切なので、リストは先頭に要素を追加したり先頭の要素を削除したりするのが遅い、dequeは中央部分の要素へのアクセスが遅い、といったことは頭に入れておくといいだろう。
#環境や条件が固定された状態でどちらを使うか検討する場合はtimeitモジュールで処理時間を実測するとよい。

#collections.dequeの使い方
#dequeオブジェクトの生成
#コンストラクタdeque()でdequeオブジェクトを生成する。
#引数を省略すると空のdequeオブジェクト、引数にリストなどのイテラブルオブジェクトを指定するとその要素を要素とするdequeオブジェクトが生成される。
from collections import deque
d = deque()
print(d)
# deque([])
print(type(d))
# <class 'collections.deque'>
d = deque(['m', 'n'])
print(d)
# deque(['m', 'n'])
#第二引数maxlenで最大長（最大要素数）を制限することもできる。後述。

#要素の追加: append(), appendleft(), extend(), extendleft(), insert()
#append()は末尾（右側）、appendleft()は先頭（左側）に要素を追加する。
d.append('o')
print(d)
# deque(['m', 'n', 'o'])
d.appendleft('l')
print(d)
# deque(['l', 'm', 'n', 'o'])
#extend()は末尾、expandleft()は先頭にリストなどのイテラブルオブジェクトの要素をすべて追加する。expandleft()では引数に指定したイテラブルの要素の順番が逆転して連結されるので注意。dequeの先頭にイテラブルの要素を順番に追加していくイメージ。
d.extend(['p', 'q'])
print(d)
# deque(['l', 'm', 'n', 'o', 'p', 'q'])
d.extendleft(['k', 'j'])
print(d)
# deque(['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'])

#insert()で途中に要素を追加することもできる。第一引数に位置、第二引数に追加する要素を指定する。第一引数に負の値を指定すると末尾からの位置になる。また、存在しない位置（範囲外の位置）を指定した場合は先頭か末尾に追加される。
#insert()はバージョン3.5で追加。
d.insert(3, 'XXX')
print(d)
# deque(['j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'q'])
d.insert(-1, 'YYY')
print(d)
# deque(['j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'YYY', 'q'])
d.insert(100, 'ZZZ')
print(d)
# deque(['j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'YYY', 'q', 'ZZZ'])
d.insert(-100, 'XYZ')
print(d)
# deque(['XYZ', 'j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'YYY', 'q', 'ZZZ'])

#要素の削除: pop(), popleft(), remove(), clear()
#pop()は末尾（右側）、popleft()は先頭（左側）から要素をひとつ削除し、その要素を返す。リストのpop()と異なり、引数に位置を指定することはできない。
d = deque(['a', 'b', 'c', 'b', 'd'])
print(d)
# deque(['a', 'b', 'c', 'b', 'd'])
print(d.pop())
# d
print(d)
# deque(['a', 'b', 'c', 'b'])
print(d.popleft())
# a
print(d)
# deque(['b', 'c', 'b'])

#remove()は引数に指定した値と等しい最初の要素を削除する。該当する要素が複数あっても削除されるのは最初の要素のみ。該当する要素がない場合はエラーとなる。
d.remove('b')
print(d)
# deque(['c', 'b'])
# d.remove('X')
# ValueError: deque.remove(x): x not in deque

#clear()はすべての要素を削除する。空のdequeになる。
d.clear()
print(d)
# deque([])
#空のdequeの場合、pop(), popleft()はエラーとなる。clear()はエラーにならない。
# d.pop()
# IndexError: pop from an empty deque
# d.popleft()
# IndexError: pop from an empty deque
d.clear()
print(d)
# deque([])

#要素全体をローテート: rotate()
#リストにはないメソッドとしてrotate()がある。デフォルトでは右に1個ずつ要素がローテート（スクロール）する。
d = deque(['a', 'b', 'c', 'd', 'e'])
print(d)
# deque(['a', 'b', 'c', 'd', 'e'])
d.rotate()
print(d)
# deque(['e', 'a', 'b', 'c', 'd'])
#引数に整数値を指定すると、その個数ずつ要素が右にローテートする。負の値を指定すると左にローテート。要素数を超える値を指定してもOK。
d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(2)
print(d)
# deque(['d', 'e', 'a', 'b', 'c'])
d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(-1)
print(d)
# deque(['b', 'c', 'd', 'e', 'a'])
d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(6)
print(d)
# deque(['e', 'a', 'b', 'c', 'd'])

#要素・インデックスの取得: [], index()
#リストと同様、[]にインデックスを指定して要素を取得できる。負の値で末尾からの位置を指定することもできる。要素の変更も可能。
#スライス:は直接は使えないが、標準ライブラリitertoolsのislice()で代用することができる。
d = deque(['a', 'b', 'c', 'c', 'd'])
print(d[0])
# a
print(d[-1])
# d
d[2] = 'X'
print(d)
# deque(['a', 'b', 'X', 'c', 'd'])
# print(d[2:4])
# TypeError: sequence index must be integer, not 'slice'

#index()で引数に指定した値に一致する最初の要素のインデックスを取得できる。存在しない値を指定するとエラーとなる。
#index()はバージョン3.5で追加。
print(d.index('c'))
# 3
print(d.index('x'))
# ValueError: 'x' is not in deque
#そのほかの操作
#そのほか、リストと同様にもろもろの操作が可能。

#組み込み関数len()で要素数を取得。
d = deque(['a', 'a', 'b', 'c'])
print(len(d))
# 4

#count()で指定した値と等しい要素の数をカウント。
print(d.count('a'))
# 2
print(d.count('x'))
# 0

#in演算子で要素が存在するか判定。
print('b' in d)
# True
print('x' in d)
# False

#reverse()メソッド、または、組み込み関数reversed()で順番を反転。reverse()メソッドは元のオブジェクト自体が反転し、reversed()は反転したイテレータを返す。
d = deque(['a', 'b', 'c', 'd', 'e'])
d.reverse()
print(d)
# deque(['e', 'd', 'c', 'b', 'a'])
d = deque(['a', 'b', 'c', 'd', 'e'])
print(deque(reversed(d)))
# deque(['e', 'd', 'c', 'b', 'a'])

#forループでも使える。
d = deque(['a', 'b', 'c'])
for v in d:
    print(v)
# a
# b
# c

#list()やtuple()でリストやタプルに変換可能。
d = deque(['a', 'b', 'c'])
l = list(d)
print(l)
# ['a', 'b', 'c']
print(type(l))
# <class 'list'>

#maxlenで最大長（最大要素数）を制限
#コンストラクタdeque()の第二引数maxlenを指定すると、最大長（最大要素数）を制限できる。maxlenのデフォルトはNoneで長さ（要素数）に制限はない。
from collections import deque
d = deque(['l', 'm', 'n'], 3)
print(d)
deque(['l', 'm', 'n'], maxlen=3)
#maxlenを設定した場合、dequeが満杯（要素数とmaxlenが等しい状態）になると、要素を追加すると逆側の要素が捨てられる。
#append(), appendleft(), extend(), extendleft()での動作は以下の通り。
d.append('o')
print(d)
# deque(['m', 'n', 'o'], maxlen=3)
d.appendleft('l')
print(d)
# deque(['l', 'm', 'n'], maxlen=3)
d.extend(['o', 'p'])
print(d)
# deque(['n', 'o', 'p'], maxlen=3)
d.extendleft(['m', 'l'])
print(d)
# deque(['l', 'm', 'n'], maxlen=3)

#insert()だと先頭や末尾に追加する場合でもエラーとなる。
# d.insert(0, 'XXX')
# IndexError: deque already at its maximum size
#要素数がmaxlenに達していなければinsert()で追加することも可能。
print(d.pop())
# n
print(d)
# deque(['l', 'm'], maxlen=3)
d.insert(1, 'XXX')
print(d)
# deque(['l', 'XXX', 'm'], maxlen=3)

#maxlenは属性として取得できるが、読み出し専用なので変更することはできない。
print(d.maxlen)
# 3
d.maxlen = 5
# AttributeError: attribute 'maxlen' of 'collections.deque' objects is not writable

 
