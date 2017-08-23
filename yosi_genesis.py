import matplotlib.pylot as plt
import numpy as np
import sys
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

##############################
# yosi_genesis linear      #
##############################

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
