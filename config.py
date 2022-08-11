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

PROXYSTR = "HTTP://14af0a20657db:69d329f469@187.17.214.238:12323"
PROXYLOCALE = 'es_BR'
TIMEZONE_OFFSET = -3 * 3600
DEVICE = {"app_version": "244.1.0.19.110",
          "android_version": 31,
           "android_release": "12.0.0",
            "dpi": "480dpi",
             "resolution": "1080x2280",
              "manufacturer": "samsung",
               "device": "SM-G998B",
                "model": "p3s",
                 "cpu":"exynos2100",
                  "version_code":"384108453"}
USER_AGENT = 'Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 Instagram 244.1.0.19.110 Android (31/12; 480dpi; 1080x2280; samsung; SM-G998B; p3s; exynos2100; es_BR; 384108453)'
COUNTRY = 'BR'
COUNTRY_CODE = 55
#Country changed from useragent https://user-agents.net/s/DHkwD1EwLj