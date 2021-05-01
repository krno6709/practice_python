#1번
def sum(a,b):
    result = a+b
    return result

print(sum(1,2))

#2번
def sum(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))

print(sum(1,2))

#오류문제
myList=[1,2,3]
print(myList.append(4)) #append는 추가는 해주는데 return값이 없기때문에 none이 출력됨

#pop(빼내기)함수
myList=[1,2,3]
print(myList.pop())#pop는 return값이 있음

def sum_many(*args): #*을 매개변수 이름 앞에 붙이면 입력값ㅇ르 전부 모아서 튜플로 만들어준다.
    sum=0
    for i in args:
        sum=sum+i
    return sum

print(sum_many(1,2,3))

#한번에 값을 받아서 튜플 값으로 두는것.
def sum_and_mul(a,b):
    return a+b,a*b

print(sum_and_mul(1,2)[0])

#매개변수에 초기값 미리 설정하기
def say_myself(name,old,man=True): #man이라는 값을 true로 고정값을 둔 것
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살입니다."%old)
    if man:
        print("남자입니다.")
    else :
        print("여자입니다.")
say_myself("라이유튜브",20,False) #맨 마지막에 값ㅇ르 안써면 True로 저장되고, False를 넣으면 여자로 인식
say_myself(old=25,name="카르노",man=false) #순서가 다르더라도 이처럼 명칭을 입력하고 값을 넣어주면 구현됨.


#변수
a=1
def vartest(a):
    a=a+1
    return a #return의 중요성!

vartest(a)
print(a)

#global 전역함수
a=1
def vartest():
    global a
    a=a+1

vartest()
print(a)

#lambda함수
#def add(a,b):
#    return a+b


#add = lambda a,b:a+b #lambda는 위에 def함수의 축약본 간단하게 한줄로 표현
myList =[lambda a,b:a+b, lambda a, b:a*b]
print(myList[0](1,2))

