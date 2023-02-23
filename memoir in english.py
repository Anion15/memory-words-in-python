# 영어 암기장

import time
from random import randint

영어 = []
영어뜻 = []
쓴단어 = []
맞은단어 = []
틀린단어 = []
틀린단어입력 = []
number_list = []
new_number = 0

영어개수 = int(input("몇 개의 단어를 외울 것인가요? : "))
넘버 = 1
대답 = 0
동작 = 0
선택 = 0
랜덤값 = 0
번호 = 0
번째 = 0
프린트번호 = 0
수정뜻 = 0
수정단어 = 0

def blank (a) :
    for i in range(a):
        print()

def line ():
    print("--------------------")

def choose():
    time.sleep(1)
    선택 = 0
    blank(3)
    print("어떤 동작을 할 것인지 선택해 주세요.")
    blank(1)
    line()
    blank(1)
    print("1. 단어 외우기")
    print("2. 단어 수정하기")
    blank(1)
    line()
    blank(1)
    동작 = int(input("번호로 선택해 주세요. : "))
    blank(1)

    if 동작 == 1:
        print("단어 외우기를 선택하셨습니다.")
        선택 = 1
    else:
        if 동작 == 2:
            print("단어 수정하기를 선택하셨습니다.")
            선택 = 2
        else:
            print("다시 입력해 주세요.")
            선택 = choose()  # 선택을 리턴받아서 다시 choose()를 호출해야 함
    return(선택)

def repeat():
    if choose() == 1 :
        blank(100)
        print("지금부터 단어 외우기를 시작 합니다.")
        blank(1)
        print("(단어 출력 -> 뜻 입력)")
        랜덤값 = 0
        번호 = 1
        new_number = 0
        프린트번호 = 0
        쓴단어 = []
        맞은단어 = []
        틀린단어 = []
        틀린단어입력 = []
        number_list = []
        blank(1)
        line()
        blank(1)
        time.sleep(1)

        for i in range(int(영어개수)):
        
            while True:
                new_number = randint(0, 영어개수 - 1)  # 0부터 (영어개수 - 1)까지의 범위에서 정수를 선택
                if new_number not in number_list:
                    number_list.append(new_number)
                    break

            print( str(번호) + ". " + str( 영어[new_number] ))  # 수정된 부분
            대답 = input( str(번호) + ". (뜻): ")
            if str(영어뜻[new_number]) == str(대답):
                맞은단어.append(str(번호))
            else:
                틀린단어.append(str(번호))
                틀린단어입력.append(str(대답))
    
            번호 = 번호 + 1
            blank(1)

        blank(1)
        line()
        blank(2)
        print("단어 외우기가 완료 되었습니다.")
        time.sleep(1)
        blank(19)
        line()
        blank(1)
        print("결과")
        blank(3)
        print( str(영어개수) + "개의 단어 중")
        blank(1)
        print( str(len(맞은단어)) + "개 정답")
        print( str(len(틀린단어)) + "개 오답")
        blank(1)
        line()
        blank(8)
        line()
        blank(1)
        index = 0
        print("틀린이유")
        blank(3)
        for i in range(len(틀린단어)):
            index = int(틀린단어[i]) - 1
            if index >= len(영어뜻):
                print("잘못된 인덱스: " + str(index))
            else:
                print("(" + str(틀린단어[i]) + "번 틀림, 문제: " + str(영어[number_list[index]]) + "), 정답 -> " + str(영어뜻[number_list[index]]) + ", 입력 -> " + str(틀린단어입력[i]) + ")")
            blank(1)
        line()

        time.sleep(5)











        blank(100)
        print("이어서 단어 외우기를 시작 합니다.")
        blank(1)
        print("(뜻 출력 -> 단어 입력)")
        랜덤값 = 0
        번호 = 1
        new_number = 0
        프린트번호 = 0
        쓴단어 = []
        맞은단어 = []
        틀린단어 = []
        틀린단어입력 = []
        number_list = []
        blank(1)
        line()
        blank(1)
        time.sleep(1)

        for i in range(int(영어개수)):
        
            while True:
                new_number = randint(0, 영어개수 - 1)  # 0부터 (영어개수 - 1)까지의 범위에서 정수를 선택
                if new_number not in number_list:
                    number_list.append(new_number)
                    break

            print( str(번호) + ". " + str( 영어뜻[new_number] ))  # 수정된 부분
            대답 = input( str(번호) + ". (단어): ")
            if str(영어[new_number]) == str(대답):
                맞은단어.append(str(번호))
            else:
                틀린단어.append(str(번호))
                틀린단어입력.append(str(대답))
    
            번호 = 번호 + 1
            blank(1)

        blank(1)
        line()
        blank(2)
        print("단어 외우기가 완료 되었습니다.")
        time.sleep(1)
        blank(19)
        line()
        blank(1)
        print("결과")
        blank(3)
        print( str(영어개수) + "개의 단어 중")
        blank(1)
        print( str(len(맞은단어)) + "개 정답")
        print( str(len(틀린단어)) + "개 오답")
        blank(1)
        line()
        blank(8)
        line()
        blank(1)
        index = 0
        print("틀린이유")
        blank(3)
        for i in range(len(틀린단어)):
            index = int(틀린단어[i]) - 1
            if index >= len(영어뜻):
               print("잘못된 인덱스: " + str(index))
            else:
                print("(" + str(틀린단어[i]) + "번 틀림, 문제: " + str(영어뜻[number_list[index]]) + "), 정답 -> " + str(영어[number_list[index]]) + ", 입력 -> " + str(틀린단어입력[i]) + ")")
            blank(1)
        line()

        time.sleep(10)

    
    else:
        blank(100)
        print("지금부터 단어 수정하기를 시작 합니다.")
        blank(1)
        line()
        blank(1)
        time.sleep(1)
        print("단어 수정하기")
        blank(2)
        프린트번호 = 1
        for i in range(len(영어뜻)):
            print( str(프린트번호) + "번, (단어): " + str(영어[i]))
            print( str(프린트번호) + "번, (뜻): " + str(영어뜻[i]))
            blank(1)
            프린트번호 = 프린트번호 + 1
        blank(2)
        line()
        blank(1)
        대답 = int(input("수정할 번호를 입력해주세요. : "))
        blank(1)
        수정단어 = input("교체할  단어를 입력해주세요. : ")
        blank(1)
        수정뜻 = input("교체할 뜻을 입력해주세요. : ")
        blank(2)
        영어.insert(int(대답 - 1), str(수정단어))
        영어뜻.insert(int(대답 -1), str(수정단어))
        print("수정이 완료되었습니다.")
    choose()


blank(3)
print("지금부터 영어 단어 저장을 시작 합니다.")
blank(1)
line()
blank(1)
time.sleep(1)

for i in range(영어개수):
    영어.append(input( str(넘버) + ".  영어 : "))
    영어뜻.append(input( str(넘버) +".  영어 뜻: "))
    넘버 = 넘버 + 1
    blank(1)

blank(1)
line()
blank(2)
print("단어 저장이 완료 되었습니다.")
time.sleep(1)
repeat()

