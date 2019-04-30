import sys
import os
from pylab import *
import numpy as np

ext = "State0"

data = ["direct","cluster","cluster2Layer"]

Direct = []
Leach = []
Modified = []
x_axis = []
#change directory to your directory which can be found out using pwd command on terminal of linux OS
DIR = "D:/Studies/Sem-4/FCOMM/Project/My proj/"
for name in data:
    for file in os.listdir(DIR):
        if file.find(name + ext) >= 0 and file.endswith(".txt"):
            fname = DIR + '/' + file
            for line in open(fname).readlines():
                x = float(line.split()[0])
                y = float(line.split()[1])
                dead = float(line.split()[2])
                if name == "direct":
                    Direct.append([x,y,dead])
                if name == "cluster":
                    Leach.append([x,y,dead])
                if name == "cluster2Layer":
                    Modified.append([x,y,dead])



size = max(len(Direct), len(Leach))
size = max(len(Modified), size)

#print size

#size = len(Modified) + 100000
for i in range(0,size):
	x_axis.append(i)


zero = size - len(Direct)
for i in range(0,zero):
	Direct.append(0)

if len(Leach) < len(Modified):
	zero = size - len(Leach)
	for i in range(0,zero):
		Leach.append(0)

if len(Leach) > len(Modified):
        zero = size - len(Modified)
        for i in range(0,zero):
                Modified.append(0)

plot(x_axis, Direct, '-r', label='direct')
plot(x_axis, Leach, '-b', label='cluster head')
plot(x_axis, Modified, '-g', label='cluster with 2 Layers')


xlabel('rounds')
ylabel('avg_energy_ntwk')	
legend()
show()


