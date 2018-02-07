import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import gaussian_kde
import random

def linear_congruence(seed,A,C,M,steps):
    X = []
    next_element = seed
    for i in range(steps):
        X += [next_element/M]
        next_element = (next_element*A+C) % M
        
    emp_mean = sum(X)/steps
    emp_var = 0
    for j in X:
        emp_var += (j - emp_mean)**2
    emp_var /= steps
    print("Moyenne empirique: ", emp_mean)
    print("Variance empirique: ", emp_var)
    print("\n")

    return X

#Python random function
def random_generator_computer(steps):
    Y = []
    for i in range(steps):
        Y += [random.random()]
    emp_mean_comp = np.mean(Y)
    emp_var_comp = np.var(Y,dtype=np.float64)
    print("Moyenne empirique par ordinateur: ", emp_mean_comp)
    print("Variance empirique par ordinateur: ", emp_var_comp)

    return Y
    
data1 = linear_congruence(3,158348089,0,2**31-1,300000)
data2 = random_generator_computer(300000)

sns.set_style('whitegrid')
sns.kdeplot(np.array(data1),bw=0.1)
sns.kdeplot(np.array(data2),bw=0.1)
plt.show()



