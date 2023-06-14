import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import graphviz
import csv

from sklearn import tree

# retrieve data
data = pd.read_csv('fukushima-dataset/example.csv')

# output two files, depending on time
file = open('fukushima-dataset/tree.csv', 'w', newline="")
writer = csv.writer(file)

# get feature, target
y = list(map(float, data['y']))
x = list()

for i in range(1, 20):
    x.append([i])

y_mean = sum(y) / len(y)
predict_y = [y_mean] * 19

M = 50
l = 0.1

functions = list()

for m in range(1, M + 1):
    residual_y = list()

    for i, now_y in enumerate(y):
        residual_y.append(now_y - predict_y[i])

    clf = tree.DecisionTreeRegressor(criterion='squared_error', max_depth=2)
    clf = clf.fit(x, residual_y)

    dot_data = tree.export_graphviz(clf, out_file=None, 
        filled=False, rounded=True,  
        special_characters=False)  
    graph = graphviz.Source(dot_data)

    graph.format = 'png'
    graph.render(filename=f'decision_tree #{m}', directory='./', cleanup=True)

    for i, now_y in enumerate(predict_y):
        predict_y[i] = now_y + l * clf.predict([[i + 1]])[0]

    functions.append(tuple(predict_y))

for data in zip(*functions):
    print(data)

    writer.writerow(data)

file.close()