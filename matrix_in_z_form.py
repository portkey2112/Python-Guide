# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:50:28 2019

@author: spoorthi m
"""
import numpy as np

arr = [[0,1,2,21],[3,4,5,22],[6,7,8,23],[9,10,11,24]]

x = np.array(arr)

m = x.shape[0]
n = x.shape[1]

if(m != n):
    print("given matrix is not a square matrix")
    exit()
    
print("Output: ")
i = 0
for j in range(n):
    print(x[i][j], end = " ")
    
k=1
for i in range (1,m):
    for j in range(n-1,-1,-1):
        if(j == n-1-k):
            print(x[i][j], end = " ")
            k+=1
            break

i = m-1
for j in range(1,n):
       print(x[i][j], end =" ")     