import pygame as pg, sys
import random
import itertools
from sqlalchemy import false
from sympy import re
import numpy as np
##  問題データ
pro=np.array([[1,4,7,2,5,8,3,6,9],
    [2,5,8,3,6,9,4,7,1],
    [3,6,9,4,7,1,5,8,2],
    [4,7,1,5,8,2,6,9,3],
    [5,8,2,6,9,3,7,1,4],
    [6,9,3,7,1,4,8,2,5],
    [7,1,4,8,2,5,9,3,6],
    [8,2,5,9,3,6,1,4,7],
    [9,3,6,1,4,7,2,5,8]])
isvar=[ True for i in range(81)]
a=random.randint(0,3)
b=random.randint(0,3)
if a==1:
    pro[0:2],pro[3:5]=pro[3:5],pro[0:2].copy()
elif a==2:
    pro[0:2],pro[6:8]=pro[6:8],pro[0:2].copy()
elif a==3:
    pro[3:5],pro[6:8]=pro[6:8],pro[3:5].copy()
if b==1:
    pro[:,0:2],pro[:,3:5]=pro[:,3:5],pro[:,0:2].copy()
elif b==2:
    pro[:,0:2],pro[:,6:8]=pro[:,6:8],pro[:,0:2].copy()
elif b==3:
    pro[:,3:5],pro[:,6:8]=pro[:,6:8],pro[:,3:5].copy()

c=random.randint(10,15)

for i  in range(c):
    a=random.randint(0,3)
    b=random.randint(0,3)
    if i%2==0:
        if b==1:
            if a==1:
                pro[0],pro[2]=pro[2],pro[0].copy()
            elif a==2:
                pro[1],pro[2]=pro[2],pro[1].copy()
            elif a==3:
                pro[0],pro[1]=pro[1],pro[0].copy()
        elif b==2:
            if a==1:
                pro[3],pro[5]=pro[5],pro[3].copy()
            elif a==2:
                pro[4],pro[5]=pro[5],pro[4].copy()
            elif a==3:
                pro[3],pro[4]=pro[4],pro[3].copy()
        else:
            if a==1:
                pro[6],pro[8]=pro[8],pro[6].copy()
            elif a==2:
                pro[7],pro[8]=pro[8],pro[7].copy()
            elif a==3:
                pro[6],pro[7]=pro[7],pro[6].copy()
    else:    
        if b==1:
            if a==1:
                pro[:,0],pro[:,2]=pro[:,2],pro[:,0].copy()
            elif a==2:
                pro[:,1],pro[:,2]=pro[:,2],pro[:,1].copy()
            elif a==3:
                pro[:,0],pro[:,1]=pro[:,1],pro[:,0].copy()
        elif b==2:
            if a==1:
                pro[:,3],pro[:,5]=pro[:,5],pro[:,3].copy()
            elif a==2:
                pro[:,4],pro[:,5]=pro[:,5],pro[:,4].copy()
            elif a==3:
                pro[:,3],pro[:,4]=pro[:,4],pro[:,3].copy()
        elif b==3:
            if a==1:
                pro[:,6],pro[:,8]=pro[:,8],pro[:,6].copy()
            elif a==2:
                pro[:,7],pro[:,8]=pro[:,8],pro[:,7].copy()
            elif a==3:
                pro[:,6],pro[:,7]=pro[:,7],pro[:,6].copy()