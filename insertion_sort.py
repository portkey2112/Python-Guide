# -*- coding: utf-8 -*-
"""
Insertion sort
"""

import numpy as np

arr = [5,0,4,1,3,3,2,1]

x=np.array(arr)
print("Input array:")
print(x)
m = x.shape[0]

for i in range(m):
    if(i == 0):
        continue
    num = x[i]
    for j in range(i-1,-1,-1):
        if(x[j] > num):
            x[j+1] = x[j]
        else:
            x[j+1]=num
            break
    if(j == 0 and x[j]>num):
        x[j]=num
print("Sorted array:")  
print(x)