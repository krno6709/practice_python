#for문의 기본 구조
#for 변수 in 리스트(또는 튜플, 문자열):
 #수행할 문자


test_list=['one','two','three']
for i in test_list:
    print(i)


a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
    print(first)
    print(last)

(a,b)=(1,2)


#if문과 연결하기
marks = [90,25,67,45,80]
number=0
for mark in marks: #리스트에서 순서대로 빼오는 거
    number = number +1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)
    
    else:
        print("%d번 학생은 불합격입니다." % number)

#continue
marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

#sum
sum=0
for i in range(1,11): #1<=x<11
    sum=sum+i
print(sum)

#구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ") #end는 print라는 함수의 옵션, 엔터를 안하고 그냥 쭉 이어서 출력해줌
    print('')

#구구단의 모든 결과를 리스트에 담아서 구현
result=[x*y for x in range(2,10) for y in range(1,10)]
print(result)