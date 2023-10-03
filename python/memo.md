##数値と文字列の結合
```
s=a+str(b)
s='{:.5f}{}.format(a,b)'
s=f'{a}と{b}'
```
##文字列のリスト（配列）を連結・結合
```
'間に挿入する文字列'.join([連結したい文字列のリスト])
```
##呪文
```
list(map(int, input().split()))
```
##各桁抽出
```
a=int(input())
a_str=str(abs(a))
for i in range(len(a_str)):
    print(a_str[i])
一桁の時の処理を忘れずに
```
```
a=86411
8
6
4
1
1
```
##辞書
```
mydict = {"apple":1, "orange":2, "banana":3}
val = mydict["apple"]
print(val)
```
##インデックスを取得
```
list_1 = ["Apple", "Banana", "Orange", "Bana", "Banana"]

print(list_1.index("Banana"))
```
##sort
```
l = [3, 1, 4, 5, 2]

l.sort()
print(l)
# [1, 2, 3, 4, 5]

l.sort(reverse=True)
print(l)
# [5, 4, 3, 2, 1]
```
##sorted
```
l = [3, 1, 4, 5, 2]

l_sorted = sorted(l)
print(l_sorted)
# [1, 2, 3, 4, 5]

print(l)
# [3, 1, 4, 5, 2]
```
##import re
```
import re

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.match(r'([a-z]+)@([a-z]+)\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(re.sub(r'([a-z]+)@([a-z]+)\.com', 'NEW_ADDRESS', s))
# NEW_ADDRESS bbb@yyy.net ccc@zzz.org
```
```
この例の正規表現パターンの[a-z]はaからzまでのいずれかの文字（＝アルファベットの小文字）、+は直前のパターン（ここでは[a-z]）を1回以上繰り返す、という意味。[a-z]+は小文字のアルファベットが1文字以上繰り返される文字列にマッチする。
```
##正規表現

|文字|説明|同様|例|マッチする|マッチしない|
|-|-|-|-|-|-|
|\d|任意の数字|[0-9]||||
|\D|任意の数字以外|[^0-9]|||
|\s|任意の空白文字|[\t\n\r\f\v]|||
|\S|任意の空白文字以外|[^\t\n\r\f\v]|||
|\w|任意の英数字|[a-zA-Z0-9]|||
|\W|任意の英数字以外|[\a-zA-Z0-9]|||
|\A|文字列の先頭|^|||
|\Z|文字列の末尾|$|||
|.|任意の一文字||a.c|abc,acc,aac|abbc,accc|
|^|文字列の先頭||^abc|abcdef|defabc|
|$|文字列の末尾||abc$|defabc|abcdef|
|* |０回以上の繰り返し||ab*|a,ab,abb,abbb,abbbb|aa,bb|
|+|１回以上の繰り返し||ab+|ab,abb,abbb,abbbb|a,aa,bb|
|?|０回または１回||ab?|a,ab|abb|
|{m}|ｍ回の繰り返し||a{3}|aaa|a,aa,aaaa|
|{m,n}|ｍ～ｎ回の繰り返し||a{2-4}|aa,aaa,aaaa|a,aaaaa|
|[]|集合| |[a-c]|a,b,c|d,e,f|
|ｌ|和集合(または)||aｌb|a,b|c,d|
|()|グループ化||(abc)+|abc, abcabc|a, ab, abcd|


