#튜플 연습하기
a=(1,2,3)
b=(4,)
print(a+b)#a와 b 튜플들을 합해줌
print(a*3)#a를 3번 반복

#딕셔너리 예제
dic={'name':'Eric','age':15}

print(dic['name'])

#딕셔너리 쌍 추가하기 순서가 아니라 key를 넣는게 핵심
a={1:'a'}
a['name']="익명"
del a[1] #1을 입력하면 1이라는 value가 삭제, 여기엔 순서가 없고 key가 있을 뿐
#키는 중복되면 안된다.
print(a)

#key리스트 만들기
a={1:'파랑구름', 2:'이현준',  3:'민준'}

print(a.keys())#키만 출력
print(a.values())# values만 뽑기
print(a.items()) #이거 전체를 새로운 배열안에 튜플 형태로 쌍을 담을 수 있다.

for k in a.keys():
    print(k)


for v in a.values():
    print(v)

for k,v in a.items():
    print("키는 : "+str(k))
    print("벨류는 : "+v) 


a.clear()# 모두 비우기
print(a)

a={1:'파랑구름', 2:'이현준',  3:'민준'}

print(a.get(4)) #print(a[4])를 치면 오류가 뜨는데 이것을 쓰면 none으로 표시해줌
print(a.get(4,'없음')) #none대신 '없음'이라는 문자로 표현

#in함수 사용하기
print(4 in a) #4가 a에 있는지 확인하기. false/true로 표현해줌


#집합 자료형 - 중복을 허용하지 않는다, 순서가 없다, 중복을 제거할때 사용하는 경우가 많다.
s1=set([1,2,3]) #set이 집합표시
#s1={1,2,3} #중괄호로 집합을 표시하기도 한다.

print(s1)

#교집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1&s2)

#합집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
print(s1|s2)
print(s1.union(s2))#위에랑 같은 함수

#차집합
print(s1-s2)

#값 1개 추가하기
print(s1.add(7))

#값 여러개 추가하기
s1=set([1,2,3,4,5,6])
s1. update([7,8,9,10])
print(s1)

#특정 값 제거하기
s1=set([1,2,3,4,5,6])
s1.remove(1)
print(s1)