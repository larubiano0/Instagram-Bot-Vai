from random import (randint,sample,choices)
import matplotlib.pyplot as plt

seconds = []

for _ in range(10000):
    for j in range(100000):
        s = []
        s.append(choices([randint(600,1200),5000],weights=[0.925,0.075])[0])
    seconds.append(sum(s)/len(s))  
    
    if _%500 == 0: 
        print(_)

plt.hist(seconds, bins=50)

plt.savefig('delay.png')

plt.clf()

plt.hist([86400/i for i in seconds], bins=50)

plt.savefig('followersperday.png')

