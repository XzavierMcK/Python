from datetime import date
import datetime
import time
import calendar
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

url = "https://campusrecshop.usf.edu/booking"

username = 'mckenzie225'
email = 'mckenzie225@usf.edu'
password = 'Sch001SUX!'


#Troubleshooter
def highlight(element, effect_time, color, border):
    #Highlights (blinks) a Selenium Webdriver element
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)

def dateTester():
    #See what day  output word
    dateAll = date.today()
    dayPLZ = calendar.day_name[dateAll.weekday()]

    '''
    #See what day of week output number 0-6 0 = Moday 
    dayPLZ = datetime.datetime.today().weekday()
    '''

    #print(dateAll)
    print(dayPLZ)

    if dayPLZ == 'Saturday' or dayPLZ == 'Wednesday':
        gDay = True
    else: 
        gDay = False

    print(gDay)
    return gDay

def check_exists_by_id(id):
    try:
        browser.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True


'''
def reservationBtns():
    browser = webdriver.Chrome(ChromeDriverManager().install())

    allBtns = browser.find_elements_by_xpath("//div[@class='btn btn-primary']")

    for btn in allBtns:
        print(btn)

    return allBtns
'''

if __name__ == "__main__":

    gDay = dateTester()

    if gDay == True:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        btnDiv = 'flex-center margin-top-24'

        browser.get(url)
        browser.maximize_window()

        browser.find_element_by_id('loginLink').click()

        time.sleep(1)
        
        browser.find_element_by_class_name("loginOption").click()
        
        time.sleep(5)
        
        if browser.find_element_by_id("i0116"):
            
            browser.find_element_by_id("i0116").send_keys(email)
            browser.find_element_by_id("idSIButton9").click()

            time.sleep(5)
            browser.find_element_by_id("i0118").send_keys(password)
            browser.find_element_by_id("idSIButton9").click()

            time.sleep(5)
            browser.find_element_by_id("idSIButton9").click()

        elif browser.find_element_by_id("username"):
            #Log in sequence
            browser.find_element_by_id("username").send_keys(username)
            browser.find_element_by_id("password").send_keys(password)
            browser.find_element_by_id("btn-submit").click()
            

        #Click Rec link
        browser.find_element_by_class_name("container-image-link-item").click()

        time.sleep(1)
    
        browser.find_element_by_css_selector(".btn.btn-default.single-date-select-button.single-date-select-one-click").click()

        time.sleep(1)

        tester = browser.find_element_by_css_selector(".booking-slot-item-right.booking-slot-action-item")

        #highlight(tester, 5, "yellow", 15)

        #tester.click()
        '''
        #Highlights the Div containing the button
        btnDiv = browser.find_element_by_xpath("//div[@class='booking-slot-item'][@data-slot-number='2']")
        highlight(btnDiv, 2, "blue", 15)
        '''

        '''
        #Finds all Book Now buttons on the page
        btn = browser.find_elements_by_xpath("//button[@class='btn btn-primary']")
        for btns in btn:
            print(btns)
            highlight(btns, 5, "yellow", 15)
        '''
        
        browser.find_elements_by_xpath("//button[@class='btn btn-primary']")[1].click()

        #browser.close()

    else:
        print("No Gym Class tommorrow")
