from random import (randint,sample,choices)
import matplotlib.pyplot as plt

seconds = []

for _ in range(10000):
    for j in range(100000):
        s = []
        s.append(choices([randint(180,540),7200],weights=[0.925,0.075])[0])
    seconds.append(sum(s)/len(s))  
    
    if _%500 == 0:
        print(_)

plt.hist(seconds, bins=50)

plt.savefig('prob.png')