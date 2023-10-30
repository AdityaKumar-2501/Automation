# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
from random import randint

import time
from time import sleep
import json
#from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Bot():

    links = []
    comments = [
        'Hi', 'Hello'
    ]

    def __init__(self):
        self.login('rohansaxena632','Lord@123')
        self.like_comment_by_hashtag('programming')

    def login(self, username, password):
        #self.driver = webdriver.Chrome()

        chrome_options = Options()
        chrome_options.add_argument("--window-size=930,820")
        # chrome_options.add_argument("--start-maximized")  # Maximize the Chrome window
        # Use webdriver_manager to automatically download and manage the ChromeDriver
        # add undetected_chromedriver here 
        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        self.driver.get('https://instagram.com/')
        sleep(5)
        username_input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)
        self.driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click() # clicking 'not now btn'
        sleep(2)
        self.driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click() # clicking 'not now btn'

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            # like
            sleep(3)
            self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(5)

            # comment
            self.driver.find_element(By.CLASS_NAME,'RxpZH').click() 
            sleep(1)
            self.driver.find_element(By.XPATH,"//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
            sleep(1)
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

def main():
    while True:
        my_bot = Bot()
        sleep(60) # one hour

if __name__ == '__main__':
    main()