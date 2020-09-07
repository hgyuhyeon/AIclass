#사칙연산 계산기
if __name__ == "__main__":
    while(True):
        x, y, axe = map(int, input("x y (+(1), -(2), *(3), /(4)): ").split())
        if (axe == 1):
            result = x + y
            print("= ", result)
        elif (axe == 2):
            result = x - y
            print("= ", result)
        elif (axe == 3):
            result = x * y
            print("= ", result)
        elif (axe == 4):
            result = x / y
            print("= ", result)
        else:
            print("Wrong input\n\n")
        command = input("command: ")
        if (command == 'quit'):
            break
            
##함수 특: 중복 리턴 가능(튜플 형태, 결과값 변경 불가능)
