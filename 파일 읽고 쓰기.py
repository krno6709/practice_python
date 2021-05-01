#파일 생성하기
f=open("새파일.txt",'w') #파일객체=open(파일 이름, 파일 열기 모드) 
#파일 열기모드에는 r-읽기모드(파일을 읽기만 할 때), w-쓰기모드(파일에 내용을 쓸 때), a-추가모드(파일의 마지막에 내용을 추가)가 있다.
f.close()

#파일을 쓰기모드로 열어 출력값 적기
f=open("새파일.txt", 'w',encoding="UTF-8") #utf-8을 작성하면 한글이 안깨지고 잘 작성됨
#절대주소 : 처음부터(c:/) 주소를 써주는것
#상대주소 : 현재 실행하는 파일을 기준으로 상대적인 경로를 써주는 것
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

#파일을 읽는 여러가지 방법
#1. readline함수 사용하기
f=open("새파일.txt",'r',encoding="UTF-8")
line=f.readline()
print(line)
f.close()

#모든 줄 읽기
f=open("새파일.txt",'r',encoding="UTF-8")
while True:
    line=f.readline()
    if not line:break
    print(line)
f.close

#readlines함수 사용하기 : 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려주는 함수
f=open("새파일.txt",'r',encoding="UTF-8")
lines=f.readlines()
for line in lines:
    print(line, end="")#end대신 strip("\n")을 넣어서 없애버리면 똑같이 출력된다.
f.close()

#read함수 이용하기 : 파일의 내용 전체를 문자열로 돌려준다.
f=open("새파일.txt",'r',encoding="UTF-8")
data=f.read()
print(data)
f.close()

#파일에 새로운 내용 추가하기.
f=open("새파일.txt",'a',encoding="UTF-8")
for i in range(11,20):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close

#with문 사용하기 : 파일을 자동으로 열고 닫기
with open("foo.txt",'w') as f:
    f.write("Life is too short, you need python") # 이함수는 따로 close를 해줄 필요가 없음. with블록을 벗어나는 순간 파일객체 f가 자동으로 close되어 편리하다.
