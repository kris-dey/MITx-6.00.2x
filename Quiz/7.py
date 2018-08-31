# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:23:41 2018

@author: KrishanuDey
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    i = 0
    while True:
        if test(i):
            break
        i+=1
    return i

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    i = 0
    loop = True
    while loop:
        if test(i):
            loop = False
        elif i == 100:
            i = -100
        else:
            i+=1
    if i < 0:
        i=i*(-1)
    return i