import os

################################################################ Ig accounts 

IGACCOUNTS = ['confesandes',
              'confesionescesa',
              'glucloudstop',
              'sinfonia_uniandes',
              'coinkapp'] #Add encuesta

DIRECTORY = 'csvdata'
MAXRATIO = 0.2 #Maximum ratio of user to follow per account (20% default)
MINFOLLOWERS = 50 #Minimum number of followers to follow an account

################################################################ Credential path

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

################################################################ Proxy configuration


PROXYSTR = 'SOCKS4://bogota:proxy@200.106.216.64:63253'
PROXYLOCALE = 'es_CO'
TIMEZONE_OFFSET = -5 * 3600