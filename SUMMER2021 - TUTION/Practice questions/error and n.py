import math as mt
import matplotlib.pyplot as mpl
import numpy as np

function = lambda n: 1*(0.5**(n-1))
function2 = lambda n: ((3*n**2)-1)/(10*n+5*n**2)
function3 = lambda n: 1/(n**2)
function4 = lambda n: (1+1/n)**n


print(function(3))


def nvaluepartialsum(function, error, limit):
    sum = 0
    i = 1
    looplimit = 1000000
    while abs(sum-limit)>=error and i<looplimit:
        sum+=function(i)
        i+=1
    return i, sum

def sequencetester(function, error, limit):
    looplimit = 100000
    for i in range(1, looplimit):

        if abs(function(i)-limit)<error:
            return i, function(i)


def visualize(errors, nvalues):
    #mpl.scatter(errors, nvalues)
    mpl.plot(errors, nvalues)
    mpl.show()

def runner():
    # print(nvaluepartialsum(function3, 0.00002, (mt.pi**2)/6))
    # print(sequencetester(function4, 0.0001, mt.e))
    errors = list(np.arange(0.0001, 1, 0.0001))

    nvalues = []
    for i in range(0, len(errors)):
        if sequencetester(function4, errors[i], mt.e) is not None:
            nvalues.append(sequencetester(function4, errors[i], mt.e)[0])
    print(len(errors))
    print(len(nvalues))
    visualize(errors, nvalues)


runner()