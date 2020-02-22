import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

data=pd.read_csv("kc_train.csv")

def Data(IO):           
    X=IO
    Y = X['销售价格']
    X= X.drop(['销售价格'],axis = 1)
    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.3, random_state=0)
    return (X_train, X_test, y_train, y_test)

x_train, x_test, y_train, y_test=Data(data)

def RF(X_train, X_test, y_train, y_test):    #随机森林 
    from  sklearn.ensemble  import  RandomForestClassifier
    model= RandomForestClassifier(n_estimators=100)
    # 决策树的个数n_estimators
    model.fit(X_train, y_train)
    predicted= model.predict(X_test)
    score = accuracy_score(y_test, predicted)
    return (score)

print(RF(x_train, x_test, y_train, y_test))

def LOR(X_train, X_test, y_train, y_test):   #逻辑回归
    from sklearn.linear_model import LogisticRegression
    lor = LogisticRegression(penalty='l1',C=100,multi_class='ovr') 
    lor.fit(X_train, y_train)
    predicted= lor.predict(X_test)
    score = accuracy_score(y_test, predicted)
    return (score)

def Svm(X_train, X_test, y_train, y_test):   #支持向量机
    from sklearn import svm
    model = svm.SVC(kernel='rbf')
    model.fit(X_train, y_train)    
    predicted= model.predict(X_test)
    score = accuracy_score(y_test, predicted)
    return (score) 

def LR(X_train, X_test, y_train, y_test):    #线性回归
    from sklearn.linear_model import LinearRegression            
    LR = LinearRegression()
    LR.fit(X_train, y_train)
    predicted = LR.predict(X_test)
    score = accuracy_score(y_test, predicted)
    return ( score,LR.intercept_,LR.coef_)