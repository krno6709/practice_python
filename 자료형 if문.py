#money,True형
money=True
if money :
    print("택시를 타고 가라")

else :
    print("걸어 가라")

#money 구간 정하기
money=2000
if money>=3000:
    print("택시를 타고 가라")

else :
    print("걸어가라")

#or구문(|) 둘중 하나라도 true가 있으면 true가 됨
money=2000
card =1
if False|False :
    print("택시를 타고 가라")

else :
    print("걸어가라")

#and구문(&) 둘다 True여야 True가 됨
money=2000
card =1
if True & True :
    print("택시를 타고 가라")

else :
    print("걸어가라")

# in 리스트
money=2000
card=1
if 1 in [1,2,3]: #not in은 in의 반대
    print("택시를 타고 가라")
else :
    print("걸어가라")

# 다중 조건 판단 elif
pocket =['paper','cellphone']
card = False
a = True
if 'money' in pocket:
    pass
elif card:
    print("택시를 타고가라")
elif a:
    print("택시를 타고가라")
else : 
    print("걸어가라")


#조건부 표현식
score=70
if score>=60:
    message ="success"
else:
    message = "failure"

message ="success" if score >=60 else "failure" #(조건문이 참인 경우) if (조건문) else (조건문이 거짓인 경우)
print(message)