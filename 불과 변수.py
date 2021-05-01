#불 : 참 아니면 거짓을 가르는것

a = True #t를 대문자로 표기하기!!!
print(type(a))

#불에서는 없는 것을 false로 있는 것을 true로 표현한다.

a=[1,2,3,4]
if a:
    print(a)

while a:
    a.pop() #pop : 마지막 요소를 꺼내어 버린다.
    print(a)


#변수
a=[1,2,3]
b=a
a[1]=4

print(b)
print(a is b) #a와 b가 같은가

#슬라이싱
a=[1,2,3]
b=a[:]#슬라이싱 하면 새로운 주소를 찾은거.
a[1]=4

print(a)
print(b)
print(id(a))#a의 주소를 찾은거
print(id(b))#b의 주소를 찾은거

#copy 모듈 이용
from copy import copy
a = [1,2,3]
b = copy(a)
a[1] =4
print(id(a))
print(id(b))

#변수 만드는 여러가지 방법
a,b=('python','life')
print(a)
print(b)

(a,b)='python','life'
print(a)
print(b)

[a,b]=['python','life']
print(a)
print(b)

a=b='python'
print(a)
print(b)

#다른 언어에서 a와 b의 값을 바꾸는 법
a=3
b=5
tmp=b #tmp라는 임시변수에 b를 저장해두고
b=a 
a=tmp
print(a)
print(b)

#파이썬에서 a와 b의 값을 바꾸는 법
a=3
b=5
a,b=b,a
print(a)
print(b)
