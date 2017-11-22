import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
#using decision tree at each node the question tree ask a question
#e.g is pedal width < 1.5 or is pedal width > 2 or is pedal length > 3
#Thus in each yes or no it goes left or right
#each question is about a feature

iris = load_iris()


#feature name of iris
#print(iris.feature_names)
#types of iris (label)
#print(iris.target_names)


#feature of iris (measurements or feature)
#print(iris.data[0])
#corresponding label name
#print(iris.target[0])

#split data into TEST and TRAINING
#we will leave some data in test to test our classifier

test_index = [0,50,100]

#training data
train_target = np.delete(iris.target,test_index)
train_data = np.delete(iris.data,test_index, axis=0)
#print(train_target)
#print(train_data)

#testing
#you can pass an array(test_index) in the accessing field of an array
test_target = iris.target[test_index]
test_data = iris.data[test_index]

#classifier
clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

print(test_target)
print(clf.predict(test_data))