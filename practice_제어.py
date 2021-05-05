#1.결과값
a="Life is oo short, you need python"
if "wife" in a : print("wife")
elif "python" in a and "you" not in a:print("python")
elif "shirt" not in a:print("shirt")
elif "need" in a : print("need")
else : print("none")


#2. while문을 이용한 1부터 1000까지의 자연수 중 3의 배수의 합을 구하라
result=0
i=1
while i <=100:
    if i%3==0:
        result +=i
    i+=1
print(result)

#3. while문을 사용하여 별을 표시하는 프로그램 작성
i=0
while True:
    i+=1
    if i>5:break
    print(i*"*")


#4.for문을 사용해 1부터 100까지의 숫자를 출력해보자.
for i in range(1,101):
    print(i)


#5. A학급에 총 10명의 학생이 있다. for문을 사용하여 A학급의 평균점수구하기
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total +=score
average=total/10
print(average)


#6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드
numbers=[1,2,3,4,5]
result=[]
for n in numbers:
    if n%2==1:
        result.append(n*2)

#위 코드를 리스트 내포(list comprehension)를 사용하여 표현하자.
numbers=[1,2,3,4,5]
result= [n*2 for n in numbers]
print(result)