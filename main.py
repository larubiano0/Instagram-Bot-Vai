from config import *

import pandas as pd
import numpy as np


df = pd.read_csv(data_dir)

df = df.drop(df[df['Descargarías VAI para usar una aplicación en vez de los grupos de Whatsapp?']=='No'].index) #Remueve personas que no están interesadas en VAI

df = df.reset_index(drop=True)

usuariosig = df['Descargarías VAI para usar una aplicación en vez de los grupos de Whatsapp?'].tolist()

print(usuariosig)