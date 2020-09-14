import pandas as pd

#pandas 기본 - Series 객체
data = ['2016','2017','2018','2019']
result = pd.Series(data) #인덱스 미지정 시 0부터 시작되는 인덱스 적용
print(result)

result.name = 'Year' #Series 객체의 이름 지정
print(result)

result.index.name = 'No' #Series 객체의 인덱스명 지정
print(result)

result = pd.Series(data, index = ['a','b','c','d']) #Series 객체의 인덱스 지정
print(result)

#dict를 이용한 Series 객체 생성
score = {
    'Kim':85,
    'Hwang':100,
    'Lee':99,
    'Choi':80
    } #key 부분은 index, values 부분은 values
result = pd.Series(score)
print(result)

#Series 객체의 연산
data = pd.Series([1,-1,3,5])
print(data)
data+100 #요소별로 연산이 진행된 결과를 출력함

#next - DataFrame 
