#9_라이브러리.py
#pickle 라이브러리로 객체 저장
#%%
import pickle
#객체의 형태를 그대로 유지하면서 파일로 저장 및 불러오기 가능
members = {'id1':['강호동', 52], 'id2':['유재석', '48']}

f = open('members.pickle', 'wb') #파일 쓰기모드로 열기
pickle.dump(members, f)
f.close() #파일 닫기

# %%
import pickle
f = open('members.pickle', 'rb')
data = pickle.load(f)
print(data)

# %%
#time 라이브러리
import time
print(time.time()) 
#1970년 1월 1일 0시 0분 0초부터 현재까지 지난시간

print(time.localtime(time.time()))
print(time.localtime(time.time()).tm_wday)
#0:월요일 ~ 6:일요일

#날짜/시간 출력형식 지정
#print(time.strftime('출력 포맷', time.localtime(time.time())))
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %p %H:%M:%S', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %p %I:%M:%S', time.localtime(time.time())))

#sleep함수 대기
for i in range(10) :
    print(i)
    time.sleep(1) #1초 대기
    
for i in range(10) :
    print(i)
    time.sleep(0.5) #0.5초 대기

# %%
#날짜 관련 라이브러리
from datetime import datetime, timedelta
time1 = datetime(2020,1,1,18,0,0)
#               년, 월,일,시간,분,초
time2 = datetime.now() #현재 날짜 및 시간
print(time1, time2)

#날짜 계산이 가능
print(time2-time1) #날짜 차이

#특정 날짜로부터 시간 계산
print(time2+timedelta(days=30)) #오늘로부터 30일뒤 몇일인지
print(time2+timedelta(days=-3, hours=-4)) #오늘로부터 3일 및 4시간 전 날짜

#숙제 1)
#여러분들의 탄생일로부터 오늘까지 몇일이 지났는지 출력
#(time2-time1).days * 24

from datetime import datetime, timedelta
time1 = datetime(1990,5,14)
time2 = datetime.now()
print(time1, time2)
print(time2-time1)

# %%
#random 라이브러리
#난수를 발생시키는 모듈
#1) 0.0~1.0사이의 실수타입 난수 생성
import random
print(random.random())

#2) 시작값 ~ 마지막값까지의 정수형 난수 생성
print(random.randint(1, 10)) #1~10까지

#3) 리스트를 무작위로 섞는 함수
numList = [1,2,3,4,5]
random.shuffle(numList) #입력 리스트를 변화시킴
print(numList)

#4) 리스트의 항목중 무작위로 하나의 값을 얻을 때
print(random.choice(numList))


# %%
import random
randNum = random.randint(1, 100)
game_on = True
count = 0
while game_on :
    #사용자가 맞출 때까지 반복
    try :
        user_num = int(input("1~100사이의 숫자를 입력하세요 >"))

        if user_num < 0 or user_num > 100 :
            print('숫자 범위를 벗어났습니다. 다시 입력하세요.')
            continue
    except :
        print('잘못입력했습니다. 다시 입력하세요.')
        continue
    count +=1
    if randNum == user_num :
        game_on = False
    elif randNum > user_num :
        print('Up~!')
    else :
        print('Down~!')
print(f'{count}횟수로 숫자를 맞췄습니다.')

# %%
#가위,바위,보 게임 만들기
#컴퓨터로부터 랜덤하게 '가위(0)', '바위(1)', '보(2)'를 얻은 후,
#사용자 입력을 받아 승부 결과를 출력한다.
#이긴 경우, 진 경우, 비긴 경우 출력
import random
game_on = True
rcp_list = ['가위', '바위', '보']
while game_on :
    comSel = random.choice(['가위', '바위', '보'])
    userSel = input("가위, 바위, 보를 입력하세요 >")
    if not(userSel in rcp_list) : #not은 조건의 반전. True는 False로, False는 True로.
        print('잘못 입력했습니다. 다시 입력하세요.')
        continue
    
    print(f'com:{comSel}, user:{userSel}')
    #비긴 경우.
    if userSel == comSel :
        print("비겼습니다.")
        continue
    #유저가 이긴 경우.
    elif (userSel=='가위' and comSel=='보') or \
        (userSel=='바위' and comSel=='가위') or \
        (userSel=='보' and comSel=='바위') :
        print("이겼습니다.")
        game_on = False
    #유저가 진 경우.
    else :
        print("졌습니다.")
        game_on = False


#%%
from statics import getMode
from statics import getAvg
numList = [1,1,1,2,2,3]
#numList = ['사과', '사과', '포도']
print(getMode(numList))
print(getAvg(numList))

