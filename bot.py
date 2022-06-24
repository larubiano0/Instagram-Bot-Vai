from config import *
from functions import *

import csv
import pandas as pd
import random

from instagrapi import Client

cl = Client()

#cl.load_settings('/tmp/dump.json') # Second run


cl.login(iglogin['IGUSERNAME'], iglogin['IGPASSWORD'])
cl.dump_settings('/tmp/dump.json') #### First run

#cl.get_timeline_feed() #Second run

ids = pd.read_csv(data['followers_ids'])
followers_ids = set(ids['ID'].tolist()) #Hashed data type to find followers in O(1)

followers_users = ['USER']

k = 0

for i in followers_ids:

    if k%50 == 0:
        print(k)

    user = cl.username_from_user_id(i)

    followers_users.append(user)

    k +=1

with open(data['followers_users'], 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(followers_users)

'''
lista = cl.user_followers(52293392775,use_cache=True,amount=967)

for i in lista:
    print(i)

with open(prueba, 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(lista)
'''