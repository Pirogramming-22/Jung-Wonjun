import random

num = 0
count = 0
turn = "computer"

def brGame(turn, num):
    if turn == "player":    # 플레이어는 정상적인 입력까지 무한 반복
        while True:
            inputVal = input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ")
            if not inputVal.isdigit():
                print("정수를 입력하세요")
                continue
            elif int(inputVal) > 3 or int(inputVal) < 1:
                print("1,2,3 중 하나를 입력하세요")
                continue
            else:
                count = int(inputVal)
                break
    else:
        count = random.randint(1,3)

    for _ in range(count):  # 숫자 말하기 이벤트
        num+=1
        print(f"{turn} {num}")
        if num == 31:
            break
    return(num)

while True:
    num = brGame(turn, num)
    if turn == "computer":
            turn = "player"
    else:
        turn = "computer"

    if num == 31:   # 게임이 종료된 경우
        break

print(f"{turn} win!")