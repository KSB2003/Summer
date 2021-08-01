import numpy as np




class Regress():
    def __init__(self, a, b, c, epsilon, alpha, h):
        self.a = a
        self.b = b
        self.c = c
        self.epsilon = epsilon
        self.alpha = alpha
        self.h = h

    def fitter(self):
        x = 20


    def __slopefinder(self, x):
        slope = (self.__function(x+self.h)-self.__function(x))/self.h
        return slope


    def __function(self, x):
        answer = self.a*x**2 + self.b*x + self.c
        return answer

def runner():
    pass




"""
linear algebra:
 - matrix operations
 - finding determinants of matrix
 - transpose of matrix
 - inverse of matrix
 - eigenvalues and eigen vector of matrix
 - eigenvalue decomposition
 - support vector decomposition
 - kramer's rule

"""