import time
from pandas import read_csv, np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import os

filebase = 'data-'
extension = ''

mean_acc_test = 0.0
train_timer = 0.0
test_timer = 0.0

paths = []

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
paths = [d for d in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, d)) and d != os.path.basename(__file__)]

for path in paths:
    filebase1 = path + '-'
    for ifile in range(5):
        train_filename = '{}/{}tr{}{}'.format(path, filebase1, ifile + 1, extension)
        test_filename = '{}/{}ts{}{}'.format(path, filebase, ifile + 1, extension)

        data = read_csv(train_filename, sep='\s+').values
        ttrain = data[:, -1]
        xtrain = data[:, 0:-1]

        data = read_csv(test_filename, sep='\s+').values
        ttest = data[:, -1]
        xtest = data[:, 0:-1]

        start_time = time.process_time()
        model = KNeighborsClassifier(n_neighbors=1, metric = "euclidean")
        model.fit(xtrain, ttrain)

        train_timer += time.process_time() - start_time
        start_time = time.process_time()
        ytest = model.predict(xtest)
        test_timer += time.process_time() - start_time

        acc_tree_test = np.sum(ytest == ttest) / len(ttest)
        mean_acc_test += acc_tree_test

        print('DT: Test file {} : Test accuracy={}'.format(ifile + 1, acc_tree_test))

    print('\nMean train time = {}'.format(train_timer / 5))
    print('Mean test time = {}'.format(test_timer / 5))
    print('Mean Test Accuracy  = {}'.format(mean_acc_test / 5))
