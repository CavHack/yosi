import matplotlib.pylot as plt
import numpy as np
import sys
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def loadRaw(input_file):
"""
    Loads the dataset. It assumes a *.csv file without header, and the output variable
    in the last column 
    """
 data = np.genfromtxt(input_file, delimiter=',', skip_header=1, names=None)

X = data[:, :-1]
y = data[:, -1]
return (X, y)

X, y = loadRaw('input3.csv')

# Stratified split test-train data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42) 
terminator_svm = svm.SVC()

##############################
# yogi_genesis linear      #
##############################

#Parameter laden model search 
parameters = { 'kernel' : ('linear', ), 'C' : [0.1, 0.5, 1, 5, 10, 50, 100] }
clf = GridSearchCV(terminator_svm, parameters, cv=5 )
clf.fit(X_train, y_train)

print clf.best_estimator_
print clf.best_score_

#The chosen model
svc = clf.best_estimator_

#
