num = 0
count = 0

while True:
    while True:
        inputVal = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        if not inputVal.isdigit():
            print("정수를 입력하세요")
            continue
        elif int(inputVal) > 3 or int(inputVal) < 1:
            print("1,2,3 중 하나를 입력하세요")
            continue
        else:
            count = int(inputVal)
            break

    for _ in range(count):
        num+=1
        print(f"playerA : {num}")
        if num == 31:
            print("playerB win!")
            exit()

    while True:
        inputVal = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        if not inputVal.isdigit():
            print("정수를 입력하세요")
            continue
        elif int(inputVal) > 3 or int(inputVal) < 1:
            print("1,2,3 중 하나를 입력하세요")
            continue
        else:
            count = int(inputVal)
            break

    for _ in range(count):
        num+=1
        print(f"playerB : {num}")
        if num == 31:
            print("playerA win!")
            exit()