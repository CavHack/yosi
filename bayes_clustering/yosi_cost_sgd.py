from mpl_toolkits.mplot3d  import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import sys

def load_data(input_file):
    """                                                                                         
    Loads the dataset. It assumes a *.csv file without header, and the output variable          
    in the last column                                                                          
    """
    dataset = np.genfromtxt(input_file, delimiter=',', skip_header=0, names=None)
    
    X  = 
    y  = 
    

return(X, y)

def preprocess_data(X):
    """                                                                                         
    Creates a copy of training samples, preprocess it (centering and scaling) and               
    inserts a columns of ones (intercept)                                                       
    """

    Xtmp = np.copy(X)
    mu = np.mean(Xtmp, axis=0)



