from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def function1():
    browser = webdriver.Chrome()
    browser.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    browser.find_element_by_xpath('//*[@id="identifierId"]').clear()
    browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys('YourEmail')		# Enter Your Email Here.....
    browser.find_element_by_xpath('//*[@id="identifierNext"]').send_keys(Keys.ENTER)
    time.sleep(2)

    brow = browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]')
    brow.find_element_by_tag_name('input').send_keys("YourPassword")                    	# Enter Your Password Here.....
    browser.find_element_by_id('passwordNext').send_keys(Keys.ENTER)
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div/div[2]/div/a/span').click()
    time.sleep(1)
    browser.find_element_by_id('gb_71').click()
    time.sleep(3)
    browser.close()

function1()

