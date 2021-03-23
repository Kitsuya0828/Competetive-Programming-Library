#include <bits/stdc++.h>
using namespace std;
 
int main() {
// コメント
/* コメ
　　ント*/

double d = 0.5; //小数（実数）

int x;
bool a = true;
bool b = x < 10; // xが10未満のときtrue そうでないときfalseになる
bool c = false;

int i = 5; 
while (i >= 0) {       // 逆順ループ
    cout << i << endl;
    i--;
}

for (int i = 0; ; i++) {  //無限ループ
  cout << i << endl;
}

string str = "Hello";       
cout << str.size() << endl; //文字列の長さ

str.at(0) = 'M'; // char型の'M' //文字列の書き換え
cout << str << endl; // Mello
 
if (str.at(1) == 'e') {      //文字列の比較
   cout << "AtCoder" << endl;
}

string s1 = "ABC";
string s2 = "ABC";
string s3 = "XY";
if (s1 == s2)   //2つの文字列が完全に一致している
   cout << "ABC == ABC" << endl;
if (s1 < s3)    //辞書順による比較
   cout << "ABC < XY" << endl;

cout << "こんにちは\nAtCoder"; // 改行\n  (エスケープシーケンス)

string s,t;
getline(cin, s); // 変数sで入力を一行受け取る
getline(cin, t); // 変数tで入力を一行受け取る

vector<int> vec(3); //vector<int> vec = {0, 0, 0}とほとんど同じ意味です。(配列の初期化)
vector<string> vec(3); //空の文字列の配列{"", "", ""}で初期化されます。
vector<int> vec(3, 5); //配列変数vecは{5, 5, 5}で初期化されます。

vec.push_back(10); // 末尾に10を追加
cout << vec[0] << endl; // .at(0)と同じ

int a = 10, b = 5;
int answer = min(a, b); // min関数
int answer = max(a, b); // max関数
swap(a, b); //swap関数(2つの引数の値を交換)

vector<int> vec = {1, 5, 3};
reverse(vec.begin(), vec.end()); // {3, 5, 1}
sort(vec.begin(), vec.end()); // {1, 3, 5}

/* 関数を定義する
返り値の型 関数名(引数1の型 引数1の名前, 引数2の型 引数2の名前, ...) {
  処理
}
関数の返り値はreturn文を使ってreturn 返り値;で指定する
関数の返り値が無い場合は返り値の型にvoidを指定し、return文はreturn;と書く
関数の引数が不要な場合は定義と呼び出しで()だけを書く
*/

vector<int> e = {1, 3, 2, 5}; //範囲for文(配列)
for (int x : e) {
    cout << x << endl;
}
string str = "hello"; // 範囲for文(文字列型(string型))
  for (char c : str) {
    if (c == 'l') {
      c = 'L';
    }
    cout << c;
  }

/*多重ループを抜けるとき
ループを抜けるかどうかを持つ変数(フラグ変数)を用意して、フラグ変数の値に応じて
ループを抜けるように書きます。多重ループの部分を関数化し、関数の内部で使える
returnを使って一気に抜けるという方法もあります。*/

/*2次元配列の宣言
vector<vector<要素の型>> 変数名(要素数1, vector<要素の型>(要素数2, 初期値));
vector<vector<要素の型>> 変数名(要素数1, vector<要素の型>(要素数2));  // 初期値を省略
(表のようなデータを扱う場合、一般的に)
vector<vector<要素の型>> 変数名(縦の要素数, vector<要素の型>(横の要素数));
*/

/*アクセス
変数名.at(添字1).at(添字2)
変数名.at(上から何番目か).at(左から何番目か) //より具体的に
*/

vector<vector<int>> data(3, vector<int>(4));   // 大きさの取得
data.size();  // 3 (縦の要素数) (12ではないことに注意!)
data.at(0).size();  // 4 (横の要素数)　　→　縦の要素数 * 横の要素数

/*N×0の二次元配列(後から配列に要素を追加して使う場合)
vector<vector<型>> 変数名(N);  // 「要素数0の配列」の配列
外側のvectorの初期値を省略することで、N個の配列の要素数はそれぞれ0になります。
*/

/*長方形にならない二次元配列(ジャグ配列)
N×0の二次元配列に後から要素を追加していく場合などに「行毎に要素数の違う
二次元配列」ができることがあります。*/
vector<vector<int>> data(2);  // 2×0の配列
data.at(0).push_back(1);  // data.at(0)は3要素の配列
data.at(0).push_back(2);
data.at(0).push_back(3);
data.at(1).push_back(4);  // data.at(1)は4要素の配列
data.at(1).push_back(5);
data.at(1).push_back(6);
data.at(1).push_back(7);

/*3次元配列の場合の宣言方法
vector<vector<vector<要素の型>>> 変数名(要素数1, vector<vector<要素の型>>(要素数2, vector<要素の型>(要素数3, 初期値)));
vector<vector<vector<要素の型>>> 変数名(要素数1, vector<vector<要素の型>>(要素数2, vector<要素の型>(要素数3)));  // 初期値を省略
*/

/*参照の宣言
参照先の型 &参照の名前 = 参照先;　*/
int f = 123;
int &g = f;  // int型変数fへの参照
}

// 配列の先頭100要素の値の合計を計算する (参照渡し)
int sum100(vector<int> &a) {
  int result = 0;
  for (int i = 0; i < 100; i++) {
    result += a.at(i);
  }
  return result;
} 
int main() {
  vector<int> vec(10000000, 1);  // すべての要素が1の配列
  // sum100 を500回呼び出す
  for (int i = 0; i < 500; i++) {
    cout << sum100(vec) << endl;  // 参照渡しなので配列のコピーは生じない
  }
}