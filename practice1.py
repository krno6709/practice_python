# 1.평균 구하기
a=80
b=75
c=55

average = (a + b+c)/3
print(average)

#자연수 13이 홀수 인지 짝수인지 판별하기
a= 13
if a%2==0:
    print("짝수입니다.")

else:  print("홀수입니다.")


#3.주민등록번호 연월윌부분과 그 뒤 숫자 나누어 출력하기
pin="881120-1068234"
yyyymmdd="19"+pin[:6]
num=pin[7:]
print(yyyymmdd)
print(num)

#4. 주민등록번호에서 성별 추출하기
pin = "881120-1068234"
print(pin[7])

#5. replace함수 이용하기
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#6. 정렬하기와 뒤집기
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7.문자열 만들기
a=['Life','is','too','short']
result=" ".join(a)
print(result)
