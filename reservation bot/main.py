# Based on tutorial from https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim

# TODO
# get the right info that oven's father wants to input
# make an UI to select for a particular time 
# Generalize for ability to plan for multiple days

# NOTE Someti

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Probably browser specific, so works on Google Chrome

from selenium.webdriver.common.by import By # Select HTML element
from selenium.webdriver.common.keys import Keys # input a specific key stroke
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select
import time

# Oven's website 
# https://loisirs.montreal.ca/IC3/#/U6510/search/?searchParam=%7B"filter":%7B"isCollapsed":false,"value":%7B"startTime":"2024-02-27T19:00:46.800-05:00","dates":%5B"2024-05-03T00:00:00.000-04:00"%5D,"siteId":694,"facilityTypeIds":"178","boroughIds":"17"%7D%7D,"sortable":%7B"isOrderAsc":true,"column":"facility.name"%7D%7D&bids=20,25

# I believe the default search site
# https://loisirs.montreal.ca/IC3/#/U5200/search/


#date = input("Which day? YYYYMMDD : ") # Day of the event
#time = input("Hour of the event? HH : ")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
# We have to download a chrome driver that is dependant of the version we have

URL = """https://loisirs.montreal.ca/IC3/#/U6510/search/?searchParam=%7B"filter":%7B"isCollapsed":false,"value":%7B"dates":%5B"2024-06-16T00:00:00.000-04:00"%5D%7D%7D,"search":"badminton","sortable":%7B"isOrderAsc":true,"column":"facility.name"%7D%7D"""
# previous URL was https://loisirs.montreal.ca/IC3/#/U5200/search/

# Go to the website
driver.get(URL)
# id = u5200_btnButtonRegisterXS0
def wait_el(time, id):
    '''Wait for a HTML element for a period of time. (Using ID)'''
    WebDriverWait(driver, time).until(
        EC.element_to_be_clickable((By.ID, id)) # presence_of_element_located before
    )

def click_btn(id):
    '''Using the HTML id of a button, click it.'''
    btn = driver.find_element(By.ID, id)
    driver.execute_script("arguments[0].click();", btn)
    #btn.click()

def select_id(time, id):
    wait_el(time, id)
    click_btn(id)


# Select Saint-Laurent

select_id(15,"u6510_btnTreeBorough") # Arrondissment ; u6510_btnTreeBorough

select_id(10, "u2000_chkValue10") # Saint-Laurent
# cooking? roller ben
click_btn("u2000_btnTreeSelectConfirm") # Confirm.

# Select plateau (Badminton default)

select_id(10, "u6510_btnTreeFacilityType") # Type de Plateau.

select_id(4, "u2000_chkValue13") # Badmintion

click_btn("u2000_btnTreeSelectConfirm") # Confirm.

# Site (Academie - first option)

#select_id(10, "u6510_selectFacilityReservationSearchSite")
select = Select(driver.find_element(By.ID, 'u6510_selectFacilityReservationSearchSite'))

select.select_by_visible_text('Académie LaurenHill Junior campus')

# Reservation date (option not available)
'''
date_inp = driver.find_element(By.ID, "u6510_edFacilityReservationSearchReserveDate")
date_inp.send_keys(date)
'''

# Click first reservation option 

select_id(5, "u6510_btnButtonReservation0")


time.sleep(20)

driver.quit()