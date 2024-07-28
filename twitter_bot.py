#   Created on 14 April

class twitter_bot:
    """
    This class provides features of:

        - Login to Twitter Account
        - Search for Keyword or Hachtag
        - Scrape posts ( Descriprtion, Reactions, Num_of_comments, Posted_by, Post_date)
        - Post reply or Post
        - Like tweets

        ...............
    
    Attributes:

        . String email: user email account
        . String password: Account password
        . String username: Account username
        . WebDriver bot: does automation tasks
        . boolean is_logged: check Account logging

    Methods:

        . login()
            initialize user account

        . searcher( string q )
            search for keyword or hachtag
        
        . gather( String url )
            gathering posts from provided url
        
        . scraper()
            scrape post information
        
        i_like_you()
            NOT YOU! liking posts

    """