#1. 학습을 위한 데이터 준비
import pandas as pd
import sklearn
from sklearn.datasets import load_iris

#데이터 로딩
iris = load_iris()
iris_data = iris.data
iris_label = iris.target
print(iris_data.shape)
print(iris_label.shape)
print('iris target value:\n',iris_label)
print('iris target name:\n',iris.target_names)
#로딩한 데이터를 기반으로 DataFrame 생성
df_iris = pd.DataFrame(data = iris_data, columns = iris.feature_names)
df_iris['label'] = iris_label
print(df_iris.shape)
df_iris.head(3)

#학습을 위한 요소 생성
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(iris_data,
                                                    iris_label,
                                                    test_size = 0.2,
                                                    random_state = 11)
#x_train -> x: feature, train: 학습용
#x_test -> x: feature, test: 검증용
#y_train -> y: 정답(라벨), train: 학습용
#y_test -> y: 정답, test: 검증용
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


#2. 사용할 모델 객체 생성
from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier() #객체 생성자: dt_clf 모델 생성.


#3. 모델 객체에 학습 데이터 매핑 후 학습
dt_clf.fit(X=x_train, y=y_train) #학습 진행


#4. 테스트 데이터를 이용하여 모델의 성능 검증
pred = dt_clf.predict(X=x_test) #예측값
print(pred[:]) 
print(y_test[:]) #검증용 정답값
#데이터 정확도
from sklearn.metrics import accuracy_score
print('predict accuracy: {}'.format(accuracy_score(y_test, pred))) #예측값 정답값 비교, 성능 검증
