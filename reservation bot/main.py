# Based on tutorial from https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim

# TODO
# replace the waiting with wait until element appears 
# get the right info that oven's father wants to input
# make an UI to select for a particular time 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Probably browser specific, so works on Google Chrome

from selenium.webdriver.common.by import By # Select HTML element
from selenium.webdriver.common.keys import Keys # input a specific key stroke
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time

# Oven's website 
# https://loisirs.montreal.ca/IC3/#/U6510/search/?searchParam=%7B"filter":%7B"isCollapsed":false,"value":%7B"startTime":"2024-02-27T19:00:46.800-05:00","dates":%5B"2024-05-03T00:00:00.000-04:00"%5D,"siteId":694,"facilityTypeIds":"178","boroughIds":"17"%7D%7D,"sortable":%7B"isOrderAsc":true,"column":"facility.name"%7D%7D&bids=20,25

# I believe the default search site
# https://loisirs.montreal.ca/IC3/#/U5200/search/

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
# We have to download a chrome driver that is dependant of the version we have

# Go to the website
driver.get("https://loisirs.montreal.ca/IC3/#/U5200/search/")

time.sleep(4)

def wait_el(time, id):
    '''Wait for a HTML element for a period of time.'''
    WebDriverWait(driver, time).until(
        EC.presence_of_element_located((By.ID, id))
    )

def click_btn(id):
    '''Using the HTML id of a button, click it.'''
    btn = driver.find_element(By.ID, id)
    btn.click()

# Select Saint-Laurent

click_btn("u5200_btnTreeBorough")
#Arr_btn = driver.find_element(By.ID, "u5200_btnTreeBorough")
#Arr_btn.click()

time.sleep(1)

click_btn("u2000_chkValue13")


time.sleep(10)

driver.quit()