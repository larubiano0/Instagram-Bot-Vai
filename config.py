import os

IGACCOUNTS = ['confesandes',
              'confesionescesa',
              'glucloudstop',
              'sinfonia_uniandes',
              'coinkapp']

DIRECTORY = 'csvdata'
MAXRATIO = 0.2 #Maximum ratio of user to follow per account (20% default)

IG_CREDENTIAL_PATH = './ig_settings.json'

DATA = {}

for file in os.listdir(DIRECTORY): #For each filename in the directory
    path = os.path.join(DIRECTORY, file) #corpus/python.txt
    file = file[:-4] #Removes .csv
    DATA[file] = path            

IGLOGIN = {}

with open('iglogin.env') as f:

    for line in f:

        if line.startswith('#') or not line.strip():
            continue
        key, value = line.strip().split('=', 1)

        IGLOGIN[key] = value