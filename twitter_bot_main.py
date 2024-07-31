from twitter_bot import twitter_bot
if __name__=='__main__':

    account = twitter_bot("email", "username", "password")
    if account.login() == True:
        account.Post(url)
