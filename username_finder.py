from config import *
from functions import *

import pandas as pd
import numpy as np
import csv


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

    if i[0] == '@': #Removes @ from users

        i = i[1:]

    realIGgusers.append(i)

with open(notfollowed, 'w', newline='\n') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(realIGgusers)