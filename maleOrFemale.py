from sklearn import tree
# figure out male on female based on height weight showsize

# [height, weight, shoe_size]
feature = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

label = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# classifier can have many model but always take same input and output
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(feature,label)

prediction = classifier.predict([190,70,43])

print(prediction)