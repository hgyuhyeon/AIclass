## Data Visualization ##
import pandas_datareader as pdr
data = pdr.get_data_yahoo('005930.KS', start='2020-01-01', end='2020-08-31')
data['Close'].plot()


#Matplotlib
import matplotlib.pyplot as plt
#plt.plot((x축 데이터), y축 데이터, format string) #기본 선 그래프 그리기
#format string ex) r--(red dashes), bs(blue squares), g^(green triangles), ro(red circles), etc.
#plt.show() #시각화 명령을 화면에 렌더링 하기
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') #(1,1), (2,4), ...
plt.ylabel('some numbers')
plt.axis([0, 6, 0, 20])
plt.show()


#Matplotlib를 이용한 Multiple Graphs (다중 그래프)
import numpy as np
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', label = 'a')
plt.plot(t, t**2, 'bs', label = 'b') #t**2 = t^2
plt.plot(t, t**3, 'g^', label = 'c') #label = 범례

plt.title('Plot Test') #제목
plt.xlabel('x_data') #x축
plt.ylabel('y_data') #y축

plt.legend() #범례 보이는 함수
plt.show()
plt.saveflg('test.png', dpi = 100, bbox_inches = 'tight') #파일로 저장하기
