import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn import tree
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.preprocessing import StandardScaler

# retrieve data
data = pd.read_csv('fukushima-dataset/after_measurements_modified.csv')
data = data.drop_duplicates()

# data properties
data.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
    s=data["value"]/100, label="value", figsize=(10,7),
    c="value", cmap=plt.get_cmap("jet"), colorbar=True,
    sharex=False
)
plt.legend()

# get feature, target
y = list(map(float, data['value']))

scaler = StandardScaler()
x_columns = list(data.columns.difference(['value']))
# x = scaler.fit_transform(data[x_columns])
x = data[x_columns]

train_x, test_x, train_y, test_y = train_test_split(
    x, 
    y, 
    test_size = 0.2,
    random_state = 0
)

print(train_x[0:5])
print(train_y[0:5])

gradient_model = GradientBoostingRegressor(
    n_estimators=500,
    learning_rate=0.3,
    max_depth=5,
    random_state=0,
).fit(train_x, train_y)

predict_test_y = gradient_model.predict(test_x)
predict_train_y = gradient_model.predict(train_x)

print(r2_score(train_y, predict_train_y))
print(r2_score(test_y, predict_test_y))

print(f'model : {gradient_model.feature_importances_}')