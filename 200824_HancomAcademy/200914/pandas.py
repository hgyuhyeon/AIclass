import pandas as pd
import numpy as np

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


#dict를 이용하여 DataFrame 객체 생성
data = {
    'name': ['Lee', 'Hwang', 'Kim', 'Choi'],
    'score': [100, 95, 90, 85],
    'grade': ['A', 'A', 'B', 'B']
      }
df = pd.DataFrame(data)
#df.index  #index 정보
#df.columns #index라고 출력되지만, columns를 출력함.
#df.values #데이터 값들이 출력됨
df.index.name = 'No' #인덱스 이름 지정
df.columns.name = 'Info' #columns 이름 지정
c = ['name','grade','score','etc']

#각 column을 따로 지정하여 객체 생성
df2 = pd.DataFrame(data, columns = c) #NaN = NULL
print(df.info()) #DataFrame의 정보를 담음

df.head(2) #위에서부터 인수의 개수만큼의 데이터를 읽음

print(df['name']) #인덱싱, 여러 개 column 접근 시 반점으로 구분
print(df.name) #윗줄과 동일한 결과

df['etc'] = np.zeros(4) #numpy를 이용해 DataFrame 데이터 변경

#Series 객체를 이용하여 column에 데이터 추가
points = pd.Series([1.5,1.7,2.4], index = [0, 1, 2])
df['points'] = points #새로운 points column 데이터 추가
df['high_score'] = df['score']>90 #연산을 통해 column 데이터 추가
df.loc[4, :] = ['Su', 70, 'C', 0.0, 1.1, False] #row 데이터 추가
del df['etc'] #del 명령어: column 데이터 삭제(완전히 삭제)
df.drop(4) #해당 row 데이터 제외하고 출력(기존 데이터는 남아있음)
df.drop(4, inplace = True) #row 데이터 삭제(완전히 삭제)

#DataFrame 데이터 조회
df.set_index('name') #name이 index위치로 감(inplace 사용 시 원본 데이터도 변경)

#특정 row 데이터 조회
df[1:3] #1이상 3미만: 1 2번 인덱스 데이터 출력
df[:2] #2미만: 0 1번 인덱스 데이터 출력

df.loc[1] #(인자: index), 특정 row의 데이터를 Series 방식으로 출력
df.loc[[0, 2]] #지정한 여러 row의 데이터 출력
df.loc[:2] #2까지: 0 1 2번 인덱스 데이터 출력
df.loc[df['grade'] == 'A',:] #(행 조건, 열 조건) 예: 성적이 A인 데이터만 출력
