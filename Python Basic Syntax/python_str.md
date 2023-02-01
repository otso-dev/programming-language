# 문자열

```python
#문자열
#a = 'abcdef'
s = "abcdefg" # 문자열
print(s)

print(s[3])
print(s[2:5])
print(s[2:7:2])

a = 10
b = 'def'

s = "head {} tail {}".format(b,a) # {} 이자리에 변수값을 넣음 매개변수 순서대로 넣어짐
print(s)

help(str)

s = '....x......abc'
s2 = ' abc'
print(s.lstrip('.')) # lstrip은 왼쪽부터 특정한 문자를 제거하고 뒤에는 안자름


s = ' Return a list of the substrings in the string, using sep as the separator string.'
print(s.split(','))
```
