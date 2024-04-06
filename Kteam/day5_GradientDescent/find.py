import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../day4_Jtheta_linearRegression')
from functions import *
from GDfunctions import *
raw = np.loadtxt('data.txt', delimiter = ',')
X = np.copy(raw)
X[:,1] = X[:,0]
X[:,0] = 1
y = raw[:,1]