# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:57:16 2018

@author: KrishanuDey
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    i = 0
    j = 0
    save = (i,j)
    maxI = 0
    
    while i in range(len(L)):
        j = 0
        k = 0
        sumL = 0
        while j+i<len(L):
            while k<=j:
                sumL += L[k+i]
                k+=1
            
            if sumL > maxI:
                maxI = sumL
                save = (i,j)
            
            j+=1
        i+=1
    
    sumK = 0            
#    while save[0] <= save[0]+save[1]:
#        sumK += L[i]
#        i+=1
    i = save[0]
    j = save[1]
    for p in range(j+1):
        sumK += L[i]
        i+=1
    
    return sumK

print(max_contig_sum([3, 4, -8, 15, -1, 2]))