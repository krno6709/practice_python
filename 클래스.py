#반복되는 변수 & 함수
result=0
def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2


#더하기 클래스 만들기
class Calculator : #클래스 명칭은 맨 처음에 대문자를 쓰는게 보통
    def __init__(self): #처음 설정
        self.result=0
    
    
    def add(self,num):
        self.result += num
        return self.result

    

cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#사칙연산 클래스 만들기(+,=,*,/)
class FourCal : 
    def __init__(self, first, second): #예약어// 이런 기능을 써라 이걸 선언할때 무조건 이게 먼저 선언한다.
        self.first = first
        self.second = second #생성자
    def setdata(self,first, second):
        self.first = first
        self.second = second
    def add(self):
        result=self.first+self.second
        return result
    
    
a=FourCal(1,2)
#a.setdata(4,2) #a의 변수를 self에 4가 first에 2가 second에 나온다.
print(a.add())

