import sys
import numpy as np

def load_data(input_file, is_int=False):
    """                   
  Loads the dataset. It assumes a *.csv file without header, and the output variable in the last column                                                                                                 
    """

    if is_int:
        data = np.genfromtxt(input_file, delimiter=',', skip_header=0, names=None, dtype=int)
    else:
        data = np.genfromtxt(input_file, delimiter=',', skip_header=0, names=None)
    return data

def gauss(mu, cov, x):
 """                                                                                                                
    Computes gaussian parametrized by mu and cov, given x. Make sure                                                   
    x dimensions are of correct size                                                                                   
    """

d = len(X)
den = np.sqrt(np.linalg.det(cov))*(2*np.pi)
