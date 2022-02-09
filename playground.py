from ctypes import sizeof
from fileinput import filename
import numpy as np
from classificationV2 import PostPrunedDecisionTreeClassifier
import read_data as rd

# read data from file
file_name = "data/toy.txt"
(x, y, classes) = rd.read_dataset(file_name)
# create y_letters, an array of strings of size (N, )
y_letters = []
for i in y:
    y_letters.append(classes[i])
y_letters = np.array(y_letters)

tree =  PostPrunedDecisionTreeClassifier()

tree.fit(x, y_letters)
x_test = np.array([[1,6,0],[0,5,5],[2,1,2]])
print(classes[tree.predict(x_test)])
print(tree.DecisionTree.right_child.depth)