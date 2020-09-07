# 호텔에 방이 3개 있고, 각 방마다 램프가 있음
# 모두 램프가 켜져있으면 전부 끔
# 1개라도 켜져있으면 모두 켬

#input
lamp_a, lamp_b, lamp_c = map(int,input("1 또는 0 입력: ").split())

#exception
if ((lamp_a < 0 or lamp_a > 1)
        or (lamp_b < 0 or lamp_b > 1)
        or (lamp_c < 0 or lamp_c > 1)):
    print("ERROR")
else:
    #AND, OR
    if(lamp_a and lamp_b and lamp_c == 1):
        lamp_a = lamp_b = lamp_c = 0
        print("OFF")
    else:
        if(lamp_a or lamp_b or lamp_c == 1):
            lamp_a = lamp_b = lamp_c = 1
            print("ON")

    print("lamp A: {} lamp B: {} lamp C: {}".format(lamp_a,lamp_b,lamp_c))
