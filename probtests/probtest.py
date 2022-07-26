from random import (randint,sample,choices)
import matplotlib.pyplot as plt

seconds = []

for _ in range(10000):
    for j in range(100000):
        s = []
        s.append(randint(564,1164))
    seconds.append(sum(s)/len(s))  
    
    if _%500 == 0: 
        print(_)

plt.hist(seconds, bins=50)

plt.savefig('delay.png')

plt.clf()

plt.hist([86400/i for i in seconds], bins=50)

plt.savefig('followersperday.png')

