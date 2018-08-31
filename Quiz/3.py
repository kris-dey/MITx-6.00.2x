# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:29:00 2018

@author: KrishanuDey
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    if L == []:
        return "no solution"
    
    M = []
    for i in L:
        M.append(0)
        
    found = False
    indexIncrement = 0
    loop = True
    
    while loop:    
        
        index = 0
        total = 0
        for i in L:
            total += (i*M[index])
            index+=1
            
        if total==s:
            found = True
            loop = False
        elif total<s:
            M[indexIncrement] += 1
        elif total>s:
            if indexIncrement < len(L)-1:
                M[indexIncrement] -= 1
                indexIncrement+=1
            else:
                loop = False
    
    if found:
        sumM = 0
        for i in M:
            sumM += i
        return sumM
    else:
        return "no solution"
    
L = [3,2,1]
s = 5
print(greedySum([], 19))