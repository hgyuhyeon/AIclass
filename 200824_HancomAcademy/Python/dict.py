#Dict Database
#Database Viewer: http://jsonviewer.stack.hu


profiles = {
    "홍": { #key
        "국가":"대한민국", #values
        "성별":"남성",
        "나이":25
    },
    "이": {
        "국가": "대한민국",
        "성별": "여성",
        "나이": 22
    },
    "배": {
        "국가": "미국",
        "성별": "남성",
        "나이": 32
    }
}

print(profiles)

a = profiles["홍"] #리스트의 index처럼 활용
print(a)

a = profiles["홍"]["국가"]
print(a)
# ' : ' 으로 key와 value 구분

a = profiles["홍"]["국가"] = "미국" #edit value
print(profiles)

a = profiles.keys() #index
print(a)
a = profiles.values() #values
print(a)
a = profiles.items() #overall
print(a)

for i in profiles.keys():
    print("key: {}, value: {}\n".format(i, profiles[i]))
    #i가 index 역할, profiles[i]가 자연스럽게 리스트 형태를 띄게 됨
#-s가 붙는다: iterable 객체 -> for, while loop 사용 가능
