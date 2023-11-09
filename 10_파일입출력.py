#%%
#(1) 텍스트 파일 읽기
file_path = '.\data\회원정보.txt'
f = open(file_path, 'r', encoding='utf-8')
text = f.read() #파일의 모든 내용 읽어 문자열로 반환
print(text)
f.close() #파일 닫기

#with 키워드를 통해 파일 열기
#파일 닫기를 안해도 된다.
#%%
with open(file_path, 'r', encoding='utf-8') as f :
    text = f.read()
#with를 벗어나면 자동으로 파일 닫기가 됨 
print(text)

#%%
#한 줄씩 읽어서 리스트로 반환
#readlines()
with open(file_path, 'r', encoding='utf-8') as f :
    text = f.readlines()
print(text)

#한사람의 정보 딕셔너리 저장
# key: ID,PW,Name,Phone,Address
# value: id01,1234,김동현,010-1234-1234,수원시 권선구 권선동
#사람의 정보(딕셔너리)를 리스트에 저장.
#%%
memberList = []
with open(file_path, 'r', encoding='utf-8') as f :
    lines = f.readlines()
    keyList = lines[0].strip('\n').split(',')
    print(keyList)
    
    for line in lines[1:] :
        valList = line.strip('\n').split(',')
        memberDic = dict()
        for key, val in zip(keyList, valList) :
            memberDic[key] = val
        print(memberDic)
        memberList.append(memberDic)
print(memberList)
#텍스트를 우리가 사용하기 쉽게 자료 구조화한 것.

#수원시에 거주하는 사람 정보를 출력
#반복문을 통해 각 자료를 조회
search_region = '수원시'
for mem in memberList :
    if search_region in mem['Address'] :
        print(mem)
        
#이름이 강동원인 사람의 정보를 조회
search_name = '강동원'
for mem in memberList :
    if search_name == mem['Name'] :
        print(mem)
        
#ID가 id02인 사람의 주소를 '부산광역시 해운대구' 로 변경.
search_id = 'id02'
for i, mem in enumerate(memberList) :
    if search_id == mem['ID'] :
        memberList[i]['Address'] = '부산광역시 해운대구'
        
print(mem)
        
# %%
#파일 쓰기
with open('./data/파일쓰기실습1.txt', 'w', encoding='utf-8') as f :
    for i in range(1, 11) :
        f.write(f'{i}번째 줄입니다.\n')
print("파일쓰기가 완료되었습니다.")

#수정된 memberList를 텍스트로 다시 저장.
with open('./data/memberAlter.txt', 'w', encoding='utf-8') as f :
    keyList = memberList[0].keys()
    #print(keyList)
    text = ','.join(keyList) + '\n'
    #print(text)
    f.write(text)
    
    for mem in memberList :
        valList = mem.values()
        text = ','.join(valList) + '\n'
        f.write(text)
print("파일쓰기가 완료되었습니다.")

#a모드 (append 모드) : 파일 끝에 내용을 추가하여 파일을 쓴다.
#w모드 (write 모드) : 기존 파일 내용을 다 지우고 새롭게 쓰기.
# f = open('./data/memberAlter.txt', 'w', encoding='utf-8')
# f.close

#새로운 멤버 추가
new_mamber = 'id06,0000,유재석,010-0000-0000, 서울시 방배동'
with open('./data/memberAlter.txt', 'a', encoding='utf-8') as f :
    f.write(new_mamber + '\n')
print("파일쓰기가 완료되었습니다.")

# %%
#대전광역시 행정구역 폴더 만들기
import os 
#os.makedirs : 폴더 만드는 함수
#os : 
path = './data'
region = '대전'

folderPath = os.path.join(path, region) #경로 생성
#folderPath = path + "/" +region 이와 같은 코드 경로가 있기도 하다.
print(folderPath)
if not os.path.isdir(folderPath) :
    os.makedirs(folderPath)
    
with open(os.path.join(path, '대전.csv'), 'r', encoding='euc-kr') as f :
    lines = f.readlines()
    guList = lines[0].strip('\n').split(',')
    #print(guList)

    for line in lines[1:] : #동 정보
                    #ㄴ> [1:] 라고 쓴 이유는 1 부터 끝까지 불러오기 위해.
                    #ㄴ> 0은 위에 gulist에서 썼기 때문. 0은 동 정보가 아니기 때문에 1부터 시작.
        dongList = line.strip('\n').split(',')
        for gu, dong in zip(guList, dongList) :
            dongPath = os.path.join(path, region, gu, dong)
            if not os.path.isdir(dongPath) and dong != '':
                os.makedirs(dongPath)
                
            #각 동별로 한글 파일 생성
            file_name = f'{dong}.hwp'
            file_path = os.path.join(dongPath, file_name)
            if not os.path.isfile(file_path) and dong != '' :
                f = open(file_path, 'wb') #'w'는 텍스트 파일, 'wb'는 응용파일.
                f.close()
                
