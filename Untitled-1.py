import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("kc_train.csv")
cols=[i for i in data.columns if i!='销售价格']
x=data[cols]
y=data['销售价格']
# print(x)
# print(y)

t=data

t.loc[t['修复年份']==0,'修复年份']=t['建筑年份']

t['修复年份-建筑年份']=t['修复年份']-t['建筑年份']

test="修复年份-建筑年份"

temp=data
d=dict(data[test].value_counts())

df = pd.DataFrame({})

for i in d:
    d[i]=0

p1=[]
p2=[]

for i in d:
    p1.append(i)
    d[i]=temp.loc[temp[test]==i]['销售价格'].mean()
    p2.append(d[i])

df[test]=p1
df['销售价格']=p2
print(df)
print(d)
sns.set(font='SimHei',font_scale=0.8)  # 解决Seaborn中文显示问题并调整字体大小
sns.barplot(y="销售价格", x=test, data=df)
plt.show()