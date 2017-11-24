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
    print(np.sin(a))

    ar = np.array([[1,2,3],
                   [4,5,6]])
    ss = np.array([[[1,2],[1,2]],[[1,2],[1,2]],[[1,2],[1,2]]])
    #type of a is numpy array
    print(type(ar))
    #type of every element in the numpy array
    #all item in numpy array must be SAME type(int64) 64 bit int
    print(ar.dtype)
    #number of bytes of each item (8bytes = 64 bit)
    print(ar.itemsize)
    #size gives total number of item in array(ignoring dimensions)
    #len will only tell you the number items in first dimension
    print(ar.size)
    print(len(ar))
    # shape return number of items in every dimension
    #for multi dimension array : number outter array and into inner ones
    print(ar.shape)
    print(a.shape)
    print(ss.shape)

    #show how many bytes data part of the numpy array takes
    #itemsize * size
    print(ar.nbytes)
    print(ss.nbytes)

def trySettingArray():
    a = np.array([0, 2, 3, 4])
    b = np.array([2, 3, 4, 5])
    c = [1,2,3]
    #change specific element to 10
    a[0] = 10
    print(a)
    #change all element to 2
    a.fill(2)
    print(a)
    #fill is faster
    a[:] = 200
    print(a)

trySettingArray()

#youtube numpy beginner tutorial 1:24:08