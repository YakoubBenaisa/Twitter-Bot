from twitter_bot import twitter_bot
if __name__=='__main__':

    account = twitter_bot("yakoubbenaissa7@hotmail.com", "yakoubdev", "aLnmftOM@123")
    if account.login() == True:
        account.Post("https://x.com/Upwork/status/1818361168215322654")