def InputData(book, total):
    # menu 1
    data = list
    # Month Day Item Income Expenses
    data[0], data[1] = map(int, input("Month/Day: ").split())
    data[2] = input("Item: ")
    data[3], data[4] = map(int, input("In, Out: ").split())
    book.append(data)
    money = total + data[3] - data[4]
    return money


def CheckCurrent(book, total):
    # menu 2
    for i in book:
        print(book[i])
    print("잔액: ", total)


if __name__ == '__main__':
    book = list
    total = 0
    while True:
        print("1. 가계부 데이터 입력")
        print("2. 현황 조회")
        num = input("입력: ")
        if num == -1:
            break

        if num == 1:
            total = InputData(total)
        elif num == 2:
            CheckCurrent(book, total)
        else:
            print("Wrong Number\n")
