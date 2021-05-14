#WhatsApp Bot - Python Selenium
'''
Author      : Aravindhan.G
Date        : 15-05-2021
Platform    : Python
Git-hub url : https://github.com/Aravindhan-G

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"  # Path where your webdrive.exe is found
URL = "https://web.whatsapp.com" # URL of the whatsapp web

class WhatsApp_Bot():

    def __init__(self):
        global PATH
        self.driver = webdriver.Chrome(PATH)  # Creating a driver with chrome

    def instantiate(self):
        global URL
        self.driver.get(URL) # Loading the specified URL with the chrome driver
        self.driver.implicitly_wait(10) # Waits for 10 seconf to scan the QR-Code.

    def spam(self,username,message,count):
        search = self.driver.find_element_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"]') # Finds the search-tab 
        search.send_keys(username)
        search.send_keys(Keys.RETURN)
        path_finder = self.driver.find_element_by_xpath('//div[@class = "_3AUV4"]//footer[@class = "_3uxr9"]//div[@class = "_2_1wd copyable-text selectable-text"]') # Finds the message text box.
        for i in range(count):
            path_finder.send_keys(message)
            path_finder.send_keys(Keys.RETURN)


if __name__ == '__main__':
    USER_NAME = str(input("Recepient Name (same as your device): "))
    MESSAGE = str(input("Spam Message: "))
    COUNT = int(input("Spam Count : "))
    bot = WhatsApp_Bot()
    bot.instantiate()
    bot.spam(USER_NAME,MESSAGE,COUNT)


