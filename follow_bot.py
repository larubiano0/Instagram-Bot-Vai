from config import *
from functions import *

import pandas as pd
from time import sleep
from random import (randint,sample,choices)
import json

from instagrapi import Client
from instagrapi.types import UserShort

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
    
    def update(self, datasets):
        """
        Chooses first user_id from random dataset,
        Checks if active (more than MINFOLLOWERS followers, otherwise continues)
        Follows user
        Prints username
        Removes user_id from list
        Removes user from csv
        follow_track.json updates ratio and followed_by_VAI
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
        followercount = accountinfo['followercount']

        if followercount < MINFOLLOWERS:
            return datasets

        username = self._cl.username_from_user_id(userID)

        if self.follow_by_userid(userID):

            print(f'{username} followed with success')

        else:

            print(f'There has been a problem while trying to follow {username}')




if __name__ == '__main__':
    bot = Bot()

    while True:
        """
        Infnit loop
        """
        datasets = bot.update(datasets)

        secs = choices([randint(600,1200),5000],weights=[0.925,0.075])[0] 

        print(f'Waiting {secs} seconds')

        sleep(secs) #In seconds

        #TODO: fix end 