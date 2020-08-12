from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
import schedule
import datetime
class clockBot():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def login(self):
        self.driver.get('https://accessuh.uh.edu/login.php')
        cougarnet_in=self.driver.find_element_by_xpath('//*[@id="param1"]')
        pass_in=self.driver.find_element_by_xpath('//*[@id="param2"]')
        login_btn=self.driver.find_element_by_xpath('//*[@id="cougarnet-login"]/i/input')
        cougarnet_in.send_keys('username')
        pass_in.send_keys('password')
        login_btn.click()
    def get_to_punching_site(self):
        #wait for page to load 
        sleep(3)
        hr_icon=self.driver.find_element_by_xpath('//*[@id="portal_area"]/div[2]/div/div[2]/div[4]/a/div[1]/img')
        window_before=self.driver.window_handles[0]
        hr_icon.click()
        #because there is a new window pop up after clicking the HR icon
        #you need to switch window before search for the time icon
        window_after=self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        #Click on time icon
        time_icon=self.driver.find_element_by_xpath('//*[@id="win0divPTNUI_LAND_REC_GROUPLET$0"]')
        time_icon.click()

    def punch_in(self):
        sleep(3)
        #encounter dropdown value, need to use Selenium Select class 
        #Find the dropdown element using Select class 
        select=Select(self.driver.find_element_by_xpath('//*[@id="TL_RPTD_TIME_PUNCH_TYPE$0"]'))
        #Punch "In" 
        select.select_by_visible_text('In')
        #Click submit 
        submit_btn=self.driver.find_element_by_xpath('//*[@id="TL_WEB_CLOCK_WK_TL_SAVE_PB"]')
        submit_btn.click()
    def punch_out(self):
        sleep(3)
        select=Select(self.driver.find_element_by_xpath('//*[@id="TL_RPTD_TIME_PUNCH_TYPE$0"]'))
        #Punch "Out"
        select.select_by_visible_text('Out')
        #Click submit -- need to test this 
        submit_btn=self.driver.find_element_by_xpath('//*[@id="TL_WEB_CLOCK_WK_TL_SAVE_PB"]')
        submit_btn.click()
    def close_window(self):
        sleep(3)
        self.driver.quit()
#array of weekend in the form of datetime.weekday()
weekend=[5,6]
#To clock In: login -> get_to_punching_site -> clock in -> close site
def clock_in():
    #If it's the weekend, return None
    if datetime.datetime.today().weekday() in weekend :
        return None

    bot_in = clockBot()
    bot_in.login()
    bot_in.get_to_punching_site()
    bot_in.punch_in()
    bot_in.close_window()
#To Clock Out: login -> get_to_punching_site -> clock out -> close site
def clock_out():
    #If it's the weekend, return None
    if datetime.datetime.today().weekday() in weekend :
        return None

    bot_out=clockBot()
    bot_out.login()
    bot_out.get_to_punching_site()
    bot_out.punch_out()
    bot_out.close_window()
#Schedule to clock In every day (except the weekend) at 10:00 AM
schedule.every().day.at("09:59").do(clock_in)
#Schedule to clock Out every day at 2:00 PM 
schedule.every().day.at("14:00").do(clock_out)
while True:
    schedule.run_pending()
    sleep(1)
