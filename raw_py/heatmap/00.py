import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 불러오기
df = pd.read_csv('fukushima-dataset/after_measurements_diff_lal_long_1.csv')
#데이터의 위도, 경도 값 제한

df1 = df[(df['latitude']<=37.5)&(df['latitude']>=37.23)&(df['longitude']>=140.9)]
#데이터의 수 제한
df2 = df1.round(3)
#중복된 index 지우기
df3 = df2.drop_duplicates(subset='longitude',keep='first')

# heatmap 그리기
data=df3.pivot(index='longitude',columns='latitude',values='value')
sns.heatmap(data,cmap='RdYlGn_r',vmax=350,vmin=100)
plt.show()