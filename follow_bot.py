from config import *
from functions import *

from instagrapi import Client
import pandas as pd
from time import sleep
from random import (randint,choices)
import json
import shutil
from traceback import print_exc


IG_USERNAME = IGLOGIN['IGUSERNAME']
IG_PASSWORD = IGLOGIN['IGPASSWORD']


datasets = {} # account:[followers_ids] 


try: 
    with open('follow_track.json','r') as json_file:
        jsondata = json.load(json_file)
except:
    with open('follow_track.json', 'w') as json_file:
        print("follow_track.json created with success")
    jsondata = {}


for account in IGACCOUNTS:
    csvdata = pd.read_csv(DATA[account],index_col=False)
    datasets[account] = csvdata['User ID'].tolist()
    
    if account not in jsondata:

        accountdata = IgAccount(account,len(csvdata),0,0)

        jsondata[account] = {'name':accountdata.name,'followers':accountdata.followers,
                             'followed_by_VAI': accountdata.followed_by_VAI, 'ratio':accountdata.ratio}


with open('follow_track.json', 'w') as f:
    json.dump(jsondata, f)


class Bot:
    _cl = None

    def __init__(self):
        self._cl = Client()
        if os.path.exists(IG_CREDENTIAL_PATH):
            self._cl.load_settings(IG_CREDENTIAL_PATH)
            self._cl.login(IG_USERNAME, IG_PASSWORD)
        else:
            self._cl.set_proxy(PROXYSTR) 
            self._cl.set_locale(PROXYLOCALE)
            self._cl.set_timezone_offset(TIMEZONE_OFFSET)
            self._cl.set_device(DEVICE)
            self._cl.set_user_agent(USER_AGENT)
            self._cl.set_country(COUNTRY)
            self._cl.set_country_code(COUNTRY_CODE)

            self._cl.login(IG_USERNAME, IG_PASSWORD)
            self._cl.dump_settings(IG_CREDENTIAL_PATH)
    
    def follow_by_username(self, username) -> bool:
        """
        Follow a username
        Parameters
        ----------
        username: str
            Username for an Instagram account
        Returns
        -------
        bool
            A boolean value
        """
        
        userid = self._cl.user_id_from_username(username)
        return self._cl.user_follow(userid)

    def follow_by_userid(self, userid) -> bool:
        """
        Follow a user
        Parameters
        ----------
        username: str
            Username for an Instagram account
        Returns
        -------
        bool
            A boolean value
        """
        
        return self._cl.user_follow(userid)
    
    def update(self, datasets, jsondata):
        """
        Chooses first user_id from random dataset,
        Checks if active (more than MINFOLLOWERS followers, otherwise continues)
        Follows user
        Prints username
        Removes user_id from list
        Removes user from csv
        updates follow_track.json (ratio and followed_by_VAI)
        returns datasets

        Parameters
        ----------
        datasets: dict
            account:[followers_ids] 

        Returns
        -------
        datasets: dict
            account:[followers_ids] 
        """
        account = choices(list(datasets.keys()))[0]
        userID = datasets[account][0]
        accountinfo = self._cl.user_info(userID).dict()
        followercount = accountinfo['follower_count']

        sleep(randint(7,23)) #Sleeps random time between 7 and 23 seconds between getting account's info and following user

        if jsondata[account]['ratio'] > MAXRATIO:

            del datasets[account] #Deletes the account from datasets, therefore it can't be chosen anymore

            return datasets, jsondata

        if followercount < MINFOLLOWERS: 

            pass

        else:

            username = self._cl.username_from_user_id(userID)

            try:

                if self.follow_by_userid(userID):
                    
                    sleep(randint(7,23))
                    print(f'{username} followed with success')

                else:

                    print(f'There has been a problem while trying to follow {username}')
                    print('Probably the account is private or already followed')

            except Exception: 

                print_exc()

                print('Something went wrong')

        datasets[account] = datasets[account][1:]

        with open(DATA[account],'r') as f: # DELETES ROW FROM CSV
            with open('temp.csv','w') as f1:

                c = 0 
                for line in f:

                    if c == 1: # SKIPS USER
                        c +=1 
                        continue

                    f1.write(line)
                    c+=1
            
        shutil.copyfile('temp.csv', DATA[account]) #Overwirtes DATA[account]


        accountdata = IgAccount(account,jsondata[account]['followers'],jsondata[account]['followed_by_VAI'],jsondata[account]['ratio']) #Update json data and follow_track.json

        accountdata.addFollowed()

        jsondata[account] = {'name':accountdata.name,'followers':accountdata.followers,
                             'followed_by_VAI': accountdata.followed_by_VAI, 'ratio':accountdata.ratio}

        with open('follow_track.json', 'w') as f:
            json.dump(jsondata, f)

        return datasets, jsondata


if __name__ == '__main__':
    bot = Bot()

    while True:
        """
        Infnit loop
        """
        datasets, jsondata = bot.update(datasets, jsondata)

        secs = randint(564,1164) #Expected value: 864. 100 users per day

        print(f'Waiting {secs} seconds')

        sleep(secs) #In seconds

        if datasets == {}: #RATIO has been followed for all csv's

            break
