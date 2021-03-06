from __future__ import division
import sympy as sy
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

def trySlicing():
    a = np.array([0, 2, 3, 4,5,6,7,8,9,10])
    print(a[1:-1])
    print(a[-6:8])
    #omited indicies are assumed to e start or end of lists
    print(a[:3])
    print(a[::2])
    print(a[-2:])



def multTuple(str, mul):
    array = []
    for i in str:
        array.append(sy.Rational(i))
    result = np.array(array) * mul
    return result

def AddTwoTuple(npArray,str):
    array = []
    for i in str:
        array.append(sy.Rational(i))
    result = np.array(array) + npArray
    return result

def MinusTwoTuple(npArray,str):
    array = []
    for i in str:
        array.append(sy.Rational(i))
    result = np.array(array) - npArray
    return result

def simplexRowOperation():
    tuple1 = np.array([sy.Rational('0'),sy.Rational('-1/3'),sy.Rational('0')])
    tuple2 = np.array([sy.Rational('1/3'),sy.Rational('1/3')])
    #piv = ['0','0','-1/4','0','-1/8','1','0','3/4','0','0','5/8','0','0','1/4']
    #varRow = ['0' ,'0' ,'-5/4' ,'0' ,'-1/8' ,'0' ,'0' ,'3/4' ,'1' ,'0', '13/8', '0', '0' , '1/4']

    piv = ['0','4/5','1','0','1/10','0','0','-3/5','0','0','-13/10','0','0','3/5']
    varRow = ['0' ,'1' ,'0' ,'0' ,'0' ,'0' ,'0' ,'0' ,'1' ,'0', '0', '0', '0' , '1']
    #pivotRow = multTuple(piv,sy.Rational('8/5'))
    pivotRow = multTuple(piv,sy.Rational('5/4'))
    print(pivotRow)

    #calRow = pivotRow * sy.Rational('-13/8')
    calRow = pivotRow * sy.Rational('-1')
    print(calRow)
    print('\n\n')
    print(AddTwoTuple(calRow, multTuple(varRow,1)))

def tryReshape():
    r = np.arange(1,20,2)
    r = r.reshape(5,2)
    print(r)
    r = r.reshape(2,5)
    print(r)
    print(r[-1][-2])
    #numpy array trick to get multi dimension array element
    print(r[-1,-1])
    #get the first array and slice it
    print(r[0,1:])
    #everytime you index you drop a dimention
    #when you slice you keep the dimention

def dropFirstLast(grades):
    first,*middle,last = grades
    print(first)
    print(middle)
    print(last)

def tryVariableArguments(*args):
    print(args)
    for i in args:
        print(i)


def tryNPArraySliceByReference():
    a = np.array([1,2,3,4,5])
    #assign copy only
    b = a[-2:].copy()
    #assign part of reference of a to c
    #if we change elements of c it will affect a
    c = a[-2:]

    print(a)
    print(b)
    print(c)
    c[0] = 100
    print(a)
    print(b)
    print(c)

def tryMask():
    ar = np.array([1,2,3,4,5,6,7,8,9,10])
    mask2 = ar % 3 == 0
    print(mask2)
    y = ar[mask2]
    print(y)
    x = ar.reshape(2,5)
    print(x)
    print(np.where(x%3 ==0))

def tryNumpymethod():
    a = np.array([[5,2,3,4,5,6],[1,2,4,5,6,7]])

    print(a.min())
    #index of min
    print(a.argmin())
    #position of min with taking into account dimension of array
    print(np.unravel_index(a.argmin(),a.shape))
    #other operations
    print(a.prod())
    print(a.sum())
    print(a)
    # operations on each column
    print(a.sum(axis=0))
    #operations on each row
    print(a.sum(axis=1))
    #whcih ever axis = the dimension with go away

class A():
    def __init__(self,number):
        print("A")
        print(number)
class B():
    def __init__(self,number):
        print("B")
        print(number)

class C(A,B):
    def __init__(self,number):
        B.__init__(self,number)
        print("C")
        print(number)


def tryKwargs(**kwargs):
    print(kwargs)



