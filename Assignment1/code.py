# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 01:06:11 2021

@author: singh
"""

import numpy as np
import matplotlib.pyplot as plt

A=np.array([2,3])
B=np.array([-4,5])

X=np.array([-4,2])
Y=np.array([5,3])

A= A.reshape(2,1)
B=B.reshape(2,1)
#computing points which divides the line in the ratio 3:2 and 2:3 externally
A1=3*B-2*A
A2=3*A-2*B
plt.plot(A[0],A[1],'o')
plt.text(A[0],A[1]*1.05,"A")
plt.plot(B[0],B[1],'o')
plt.text(B[0],B[1]*1.05,"B")
plt.plot(A1[0],A1[1],'o')
plt.text(A1[0],A1[1]*1.05,'A1')
plt.plot(A2[0],A2[1],'o')
plt.text(A2[0],A2[1]*1.05,'A2')
plt.grid()
plt.axis([-20,20,-5,15])
plt.plot(X,Y)

a1=np.linalg.norm(A1-A)/np.linalg.norm(A1-B)
print(a1)
a2=np.linalg.norm(A2-A)/np.linalg.norm(A2-B)
print(a2)
#hence we get the required ratio


plt.show()
