#%%
#(1) 데이터의 중심 지표를 구하기
#데이터의 중심 지표 - 데이터를 대표하는 하나의 값
#ex) 평균, 최빈값, 중앙값

numList = [1,2,3,1,2,1,1,3,3,3,100]
#1) 평균
avg = sum(numList) / len(numList)
print(avg) # 평균 10.9

#2) 최빈값
#max_num = max(numList.values()) 
#for n in numList.values() :
    #if n == max_num :
        #print(n)
        
num_set = set(numList)
num_dict = dict()
for f in num_set:
    num_dict[f] = numList.count(f)
print(num_dict)

max_num = max(num_dict.values())
modes = []
for k, v in num_dict.items() :
    if v == max_num :
        print('최빈값', k, v)
        #mode = k
        modes.append(k)
        #break
print(modes)

#3) 중앙값
#리스트를 오름차순으로 정렬한 후,
#리스트의 크기를 N이라고 할 때, 다음의 인덱스 값이 중앙값.
#N이 홀수인 경우 : N//2 인덱스 값
#N이 짝수인 경우 : (N//2, N//2-1) 인덱스 값들의 평균
numList.sort() #기존 리스트를 변경해서 정렬해주는 것.
#sorted(numList) #정렬된 리스트를 반환, 기존 리스트를 변경 안함.

size = len(numList)

if size % 2 == 1 :
    midVal = numList[size//2]
else :
    midVal = (numList[size//2] + numList[size//2-1])/2
print('중앙값:', midVal)

# %%
#2) set 예제
dateList = ['09/10', '09/11', '09/12', '10/01', '10/13', '11/20' ]
# 위의 헬스장 이용 횟수 데이터에서 달별 이용 횟수를 출력하시오.
#2-1) 유니크한 달 값 구하기(달만 있는 list 만들기. set 활용)
monList = []
for d in dateList :
    monList.append(d[:2])
monList = [d[:2] for d in dateList]
monList = [d.split('/')[0] for d in dateList]

monSet = set(monList)
print(monList)

#2-2) 달별 이용 횟수 구하기(dict 및 count()함수 활용)
monCount = list()
for m in monSet :
    monCount.append((m, monList.count(m)))
print(monCount)


#빈도수 구하는 모듈
from collections import Counter
#collection 라이브러리에서 counter 클래스를 사용.
monCount = Counter(monList)
print(monCount)
print(monCount.most_common(1)) #가장 빈도수 높은 것 1개
print(monCount.most_common(3)) #가장 빈도수 높은 것 3개

Counter1 = Counter(['사과', '사과', '딸기'])
Counter2 = Counter(['포도', '포도', '딸기'])
print(Counter1, Counter2)
#집합 연산 가능
print(Counter1 + Counter2) #합집합
print(Counter1 - Counter2) #차집합
print(Counter2 - Counter1)
print(Counter1 & Counter2) #교집합


# %%
