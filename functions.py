def isNaN(num):
    return num != num


class IgAccount:

    def __init__(self, followers, followed_by_VAI=0,ratio=0):
        self.followers = followers
        self.followed_by_VAI = followed_by_VAI
        self.ratio = ratio
    
    def followedOne(self):
        self.followed_by_VAI = self.followed_by_VAI + 1
        self.ratio = round(self.followed_by_VAI / self.followers,2)
        
    def __str__(self):
        return f'followers:{self.followers}, followed_by_VAI:{self.followed_by_VAI}, ratio:{self.ratio}'