from config import *
from functions import *

import os
import pandas as pd
from time import sleep
from typing import Dict, List
from random import (randint,sample,choice)

from instagrapi import Client
from instagrapi.types import UserShort

IG_USERNAME = iglogin['IGUSERNAME']
IG_PASSWORD = iglogin['IGPASSWORD']
IG_CREDENTIAL_PATH = './ig_settings.json'

nf = pd.read_csv(data['not_followers'])
not_followers = nf['USER'].tolist()

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
        userid = self._cl.user_id_from_username(username)
        return self._cl.user_follow(userid)

    def unfollow_by_username(self, username) -> bool:
        """
        Unfollow a user
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
        return self._cl.user_unfollow(userid)
    
    def get_followers(self, amount: int = 0) -> Dict[int, UserShort]:
        """
        Get bot's followers
        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf
        Returns
        -------
        Dict[int, UserShort]
            Dict of user_id and User object
        """
        return self._cl.user_followers(self._cl.user_id, amount=amount)
    
    def get_followers_usernames(self, amount: int = 0) -> List[str]:
        """
        Get bot's followers usernames
        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf
        Returns
        -------
        List[str]
            List of usernames
        """
        followers = self._cl.user_followers(self._cl.user_id, amount=amount)
        return [user.username for user in followers.values()]

    def get_following(self, amount: int = 0) -> Dict[int, UserShort]:
        """
        Get bot's followed users
        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf
        Returns
        -------
        Dict[int, UserShort]
            Dict of user_id and User object
        """
        return self._cl.user_following(self._cl.user_id, amount=amount)
    
    def get_following_usernames(self, amount: int = 0) -> List[str]:
        """
        Get bot's followed usernames
        Parameters
        ----------
        amount: int, optional
            Maximum number of media to return, default is 0 - Inf
        Returns
        -------
        List[str]
            List of usernames
        """
        following = self._cl.user_following(self._cl.user_id, amount=amount)
        return [user.username for user in following.values()]
    
    def update(self, not_followers):
        """
        Do something
        """
        usuario = not_followers[0]

        if self.follow_by_username(usuario):

            print(f'{usuario} followed with success')

        else: 

            print(f'There has been a problem while trying to follow {usuario}')

        not_followers = not_followers[1:] #Removes from the list the first one

        '''
        TODO
        Ampliar la lista de followers_users y followers_ids
        '''


if __name__ == '__main__':
    bot = Bot()

    while True:
        """
        Infnit loop
        """
        not_followers = bot.update(not_followers)

        secs = randint(120,1200)

        print(f'Waiting {secs} seconds')

        sleep(secs) #In seconds

        if len(not_followers) == 0:

            print('Everyone was followed')

            break

            