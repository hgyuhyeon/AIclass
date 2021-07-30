#데이터 결측치 처리 (NaN값)

#결측치? : 
#1. 누락된 값이 포함된 데이터셋 사용
#2. 데이터를 잘못 입력하는 경우(DataFrame에 없는 행과 열 데이터 입력 등)
#3. 범위를 지정하여 데이터 추출 시, 존재하지 않는 데이터일 경우

#처리법:
#레코드 전체 삭제(신중해야 함, 모델을 왜곡할 확률 높음)
#특정 대표값으로 대체
#예측 모델 기반으로 도출한 예측값으로 대체

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(18).reshape(6,3), index = ['a','b','c','d','e','f'], columns = ['x','y','z'])

df['data1'] = pd.Series([1.7, 1.2, 2.4], index = ['a','e','c'])
df.loc['c'] = np.nan

df.isnull().sum() #DataFrame 내 NaN데이터를 찾아 변환, sum()을 이용하여 그 데이터 개수 도출
df.dropna() #NaN값이 하나라도 있는 행 데이터는 제외
df.dropna(how = 'all') #모든 행 데이터값이 NaN인 데이터 제외
#원본 데이터 제외 시 inplace = True 옵션 추가
df.dropna(axis = 1) #column(열) 기준으로 데이터 조회 및 제거 시 axis = 1 옵션 사용

#dataset 수정
df.iloc[:2, 0] = np.nan
df.iloc[:4, 1] = np.nan

df.dropna(thresh = 3) #저장된 데이터가 특정 개수 이상인 데이터만 출력하는 옵션
df.fillna({'x':1, 'y':2}, inplace = True) #누락 값을 인자의 값으로 대체하는 함수(inplace 옵션 적용 가능)


#DataFrame 정렬
df = pd.DataFrame(np.arange(18).reshape(6,3), index = ['a','e','h','d','c','f'], columns = ['x','y','z'])
df.loc['c'] = np.nan
#index 값 기준으로 정렬함(default = 오름차순)
df.sort_index() 
df.sort_index(ascending = False) #내림차순 정렬 옵션
df.sort_index(axis = 1, ascending = False) #column 인덱스 기분으로 정렬함, 내림차순 옵션 적용 가능)
#value 값 기준으로 정렬함
df.sort_values(by = 'x', ascending = False) #by 옵션으로 컬럼명 지정


#Aggregation(집계) 함수 적용
#dataset = values가 전부 random values
dates = pd.date_range('20200801', periods = 6)
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = ['A', 'B', 'C', 'D'])

df.mean() #축 정보를기준으로 데이터의 평균 값 계산(기본옵션: axis = 0)
#그룹연산
#Split -> Apply -> Combine
df = pd.DataFrame({
                   'product':['a','b','a','b','a','b','a','a'],
                   'sensor':['one','one','two','three','two','two','one','three'],
                  'x':np.random.randn(8),
                  'y':np.random.randn(8)})
grouped = df.groupby('product') #SQL groupby 명령어와 동일
#product별로 group화된 상태로 split된 상태임

df.groupby('product').sum() #그룹화한 상태의 값을 모두 더해서 한번에 출력
df.groupby(['product','sensor']).sum() #여러 columns를 기준으로 그룹화. product가 sensor 값 기준으로 세분된 그룹이 만들어짐
df.groupby(['product','sensor'])['x'].sum() #x 데이터만 출력하고 싶을 때(y를 제외함)
df.groupby(['product','sensor']).agg({'x':'max','y':'min'}) #column별 다른 집계함수(max, min)적용
