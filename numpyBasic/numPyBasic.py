from __future__ import division
#now 1/2 gives 0.5 instead of 0(python 3 floating point division is default)
import numpy as np

def tryArray():
    a = np.array([0,2,3,4])
    b = np.array([2,3,4,5])
    #numpy array has no comma
    #using array function passing in array
    print(a)
    print(b)
    #you can do operations on all the elements of array without iteration
    print(a+b)
    print(a*b)
    print(a*5)
    #dot multiplication(matrix multiplication)
    print(a@b)
    print(a.dot(b))
    #can do sin on array in radian
    print(sin(a))


