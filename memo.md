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