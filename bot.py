from config import *
from functions import *

import csv
import pandas as pd

from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag


cl = Client()
cl.login('', '')

lista = cl.user_followers(52293392775,use_cache=True,amount=967)

for i in lista:
    print(i)

with open(prueba, 'w', newline='\n') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(lista)


