#짝수, 홀수 판별 할 수 있는 프로그램 작성
#임의의 수를 2로 나눠서 나머지가 0이면 짝수, 아니면 홀수
# : 주석을 의미, 코드를 설명

num=17
if num % 2== 0 :
    print("짝수")
else :
    print("홀수")

    
#숫자를 입력 받아서 짝수/홀수 판별
#print("숫자를 입력하세요")
while num != 0 : # '==' 같은지 비교, '!=' 다른지 비교
    num = int(input("숫자를 입력하세요")) #"30" 키보드로 부터 문자열을 입력 받음
    if (num % 2 == 0) :
        print("짝수")
    else :
        print("홀수")

    if num == 0 :
        print("프로그램이 종료됩니다.")