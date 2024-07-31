#   Created on 14 April

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

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
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    def __init__(self, email : str, username, password) -> None:
        self.email = email
        self.username = username
        self.password = password


    def login(self):

        driver = twitter_bot.driver
        wait = twitter_bot.wait

        url = "https://www.twitter.com/login"         #   class attribute
        email_input_selector = "[autocomplete=\"username\"]" 
        username_input_selector = "[autocapitalize=\"none\"]"
        password_input_selector = "[autocomplete=\"current-password\"]"

        email_button_xpath = "//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]"
        username_button_selector = "[data-testid=\"ocfEnterTextNextButton\"]"
        password_button_selector = "[data-testid=\"LoginForm_Login_Button\"]"

        driver.get(url)

        #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, email_input_selector)))
        time.sleep(2)
        email_input = driver.find_element(By.CSS_SELECTOR, email_input_selector)
        email_input.send_keys(self.email)

        email_button = wait.until(EC.presence_of_element_located((By.XPATH, email_button_xpath)))
        email_button.click()

        #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, email_input_selector)))
        time.sleep(2)

        username_input = driver.find_element(By.CSS_SELECTOR, username_input_selector)
        username_input.send_keys(self.username)

        username_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, username_button_selector)))
        username_button.click()

        time.sleep(2)

        password_input = driver.find_element(By.CSS_SELECTOR, password_input_selector)
        password_input.send_keys(self.password)

        password_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, password_button_selector)))
        password_button.click()

        time.sleep()

