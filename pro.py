import itertools
import random
l = [1,2,3, 4,5,6,7,8,9]
##  問題データ
pro=[[1,4,7,2,5,8,3,6,9],
    [2,5,8,3,6,9,4,6,1],
    [3,6,9,4,7,1,5,8,2],
    [4,7,1,5,8,2,6,9,3],
    [5,8,2,6,9,3,7,1,4],
    [6,9,3,7,1,4,8,2,5],
    [7,1,4,8,2,5,9,3,6],
    [8,2,5,9,3,6,1,4,7],
    [9,3,6,1,4,7,2,5,8]]
a=random.randint(0,3)
b=random.randint(0,3)
if a==1:
    pro[0:3],pro[3:6]=pro[3:6],pro[0:3]
elif a==2:
    pro[0:3],pro[6:9]=pro[6:9],pro[0:3]
elif a==3:
    pro[3:6],pro[6:9]=pro[6:9],pro[3:6]
if b==1:
    pro[0:9][0:3],pro[0:9][3:6]=pro[0:9][3:6],pro[0:9][0:3]
elif b==2:
    pro[0:9][0:3],pro[0:9][6:9]=pro[0:9][6:9],pro[0:9][0:3]
elif b==3:
    pro[0:9][3:6],pro[0:9][6:9]=pro[0:9][6:9],pro[0:9][3:6]
c=random.randint(10,15)

for i  in range(c):
    a=random.randint(0,3)
    b=random.randint(0,3)
    if i%2==0:
        if b==1:
            if a==1:
                pro[0],pro[2]=pro[2],pro[0]
            elif a==2:
                pro[1],pro[2]=pro[2],pro[1]
            elif a==3:
                pro[0],pro[1]=pro[1],pro[0]
        elif b==2:
            if a==1:
                pro[3],pro[5]=pro[5],pro[3]
            elif a==2:
                pro[4],pro[5]=pro[5],pro[4]
            elif a==3:
                pro[3],pro[4]=pro[4],pro[3]
        else:
            if a==1:
                pro[6],pro[8]=pro[8],pro[6]
            elif a==2:
                pro[7],pro[8]=pro[8],pro[7]
            elif a==3:
                pro[6],pro[7]=pro[7],pro[6]
    else:    
        if b==1:
            if a==1:
                pro[0:9][0],pro[0:9][2]=pro[0:9][2],pro[0:9][0]
            elif a==2:
                pro[0:9][1],pro[0:9][2]=pro[0:9][2],pro[0:9][1]
            elif a==3:
                pro[0:9][0],pro[0:9][1]=pro[0:9][1],pro[0:9][0]
        elif b==2:
            if a==1:
                pro[0:9][3],pro[0:9][5]=pro[0:9][5],pro[0:9][3]
            elif a==2:
                pro[0:9][4],pro[0:9][5]=pro[0:9][5],pro[0:9][4]
            elif a==3:
                pro[0:9][3],pro[0:9][4]=pro[0:9][4],pro[0:9][3]
        elif b==3:
            if a==1:
                pro[0:9][6],pro[0:9][8]=pro[0:9][8],pro[0:9][6]
            elif a==2:
                pro[0:9][7],pro[0:9][8]=pro[0:9][8],pro[0:9][7]
            elif a==3:
                pro[0:9][6],pro[0:9][7]=pro[0:9][7],pro[0:9][6]
print(pro)