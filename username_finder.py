from config import *
from functions import *

import pandas as pd
import numpy as np
import csv

'''

Este código se usó para limpiar los datos de los usuarios en possible_followers. Personas en la encuesta,
que posiblemente no nos siguen. Posteriormente se encontró haciendo uso de followers_uwers, todos los usuarios
que participaron en la encuesta (y descargarían VAI) pero no siguen a VAI

df = pd.read_csv(encuesta)

df = df.drop(df[df['Descargarías VAI para usar una aplicación en vez de los grupos de Whatsapp?']=='No'].index) #Removes people not interested in VAI

df = df.reset_index(drop=True)

igusers = df['Cuál es tu usuario en Instagram? (Siguenos para poder participar en la rifa.)'].tolist()

realIGgusers = []

for i in igusers:

    if isNaN(i):

        continue

    if ' ' in i: #Removes cases as 'I don't have one'

        continue

    if '-' in i: #ilegal char

        continue

    if any(x == i for x in ['NA','N.A.','.','N.A','...']):

        continue

    if i[0] == '@': #Removes @ from users

        i = i[1:]

    realIGgusers.append(i)

vcf = pd.read_csv(vaicommunityfollowers)
followerslist = set(vcf['userName'].tolist()) #Hashed data type to find followers in O(1)

final_list = []

for i in realIGgusers:

    if i not in followerslist:

        final_list.append(i)

with open(notfollowers, 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(final_list)

with open(followers, 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(list(followerslist))

print(f'IG users:{len(realIGgusers)}')
print(f'Posible people to follow:{len(final_list)}')
print(f'AlreadyFollowed:{len(followerslist)}')

pd.read_csv('followers.csv', header=None).T.to_csv('followers.csv', header=False, index=False)
pd.read_csv('notfollowers.csv', header=None).T.to_csv('notfollowers.csv', header=False, index=False)

'''


pf = pd.read_csv(data['possible_followers'])
possible_followers = set(pf['USER'].tolist())

print(len(possible_followers))

fu = pd.read_csv(data['followers_users'])
followers_users = set(fu['USER'].tolist())

not_followers = []

for user in possible_followers:

    if user not in followers_users:

        not_followers.append(user)

print(not_followers)

print(len(not_followers))

print(len(followers_users))

print(len(possible_followers))

with open(data['not_followers'], 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(list(not_followers))

pd.read_csv(data['not_followers'], header=None).T.to_csv(data['not_followers'], header=False, index=False) #Transposes the Matrix
