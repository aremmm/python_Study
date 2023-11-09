treehit=0 #나무를 찍은 횟수
while treehit < 10 :
    #나무를 찍은 횟수가 10미만이면 반복
    #treehit = treehit +1 #횟수 1 증가
    treehit += 1
    print(f'나무를 {treehit}번 찍었습니다.')

    if treehit == 10 :
        print("나무가 넘어갑니다.")