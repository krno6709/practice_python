#부모 클래스를 활용하여 다른 클래스를 만드는 것 class 클래스이름(상속할 클래스 이름)

class FourCal : 
    def __init__(self, first, second): 
        self.first = first
        self.second = second 
    def setdata(self,first, second):
        self.first = first
        self.second = second
    def add(self):
        result=self.first+self.second
        return result

    def mul(self) :
        result = self.first *self.second
        return result

    def sub(self) :
        result = self.first - self.second
        return result

    def div(self) :
        result= self.first / self.second
        return result


class MoreFourCal(FourCal):
   def div(self) : #한번더 입력해주면 여기선 여기에 입력되는 것이 우선된다. -> 매서드 오버라이딩
       if self.seocnd ==0:
           return 0
        else:
            return self.first / self.second

a=MoreFourCal(4,2)
print(a.add())

