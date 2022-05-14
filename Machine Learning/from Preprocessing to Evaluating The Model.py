import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
# ensemble means model family (眾多選擇模型的地方)
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib

#red wine quality data from Kaggle
data_url = '/Users/marylin/文件/程式語言/Python/ML Tutorial/wineQualityReds.csv'
data = pd.read_csv(data_url)
print(data.head())
data.head()
data.shape
data.describe()
#如果打 data.describe 會輸出全部的 row data
#但打 data.describe() 會輸出 data 的統計值總覽
print(data.describe())
#如果打 data.describe 會輸出全部的 row data
#但打 data.describe() 會輸出 data 的統計值總覽

y = data.quality
X = data.drop('quality', axis = 1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state = 123, #若為整數時，每次生成的數據都相同
    stratify = y #劃分出來的測試集或訓練集中，其類標籤的比例同輸入的數組中類標籤的比例相同，可以用於處理不均衡的數據集
)

X_train_scaled = preprocessing.scale(X_train)
print(X_train_scaled.mean(axis = 0))
print(X_train_scaled.std(axis = 0))
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
print(X_train_scaled.mean())
print(X_train_scaled.std(axis = 0))
pipeline = make_pipeline(preprocessing.StandardScaler(),
												RandomForestRegressor(n_estimators=100))
pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))
print(pipeline.get_params())
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
										'randomforestregressor__max_depth': [None, 5, 3, 1]}

clf = GridSearchCV(pipeline, hyperparameters, cv=10)
# fit 用來訓練＆校正模型
clf.fit(X_train, y_train)
clf.best_params_

print clf.refit

y_pred = clf.pred(X_test)
y_pred
print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))
