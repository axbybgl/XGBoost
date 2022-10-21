import imp
from tkinter import E
from tkinter.tix import HList
import numpy as np
import math
import pandas as pd


yHatList = np.arange(0, 1, 0.001).tolist() + np.arange(0, 1, 0.001).tolist()
yList = [0]*1000 + [1]*1000
gList = []
HList = []

for i in range(len(yHatList)): 
    yiHat = yHatList[i]
    yi = yList[i]
    gi = -yi * (1 - 1 / (1 + math.pow(math.e, -yiHat))) + (1 - yi) / (1 + math.pow(math.e, -yiHat))
    hi =  math.pow(math.e, -yiHat) / math.pow(math.e, -yiHat) ** 2
    gList.append(gi)
    HList.append(hi)

print(yHatList)
print(len(yList))
print(len(HList))
print(len(gList))

frame = pd.DataFrame({'g_i':gList,'h_i':HList,'y_i':yList,'y_i^hat':yHatList})
 
frame.to_csv("Data.csv",index=False,sep=',')
