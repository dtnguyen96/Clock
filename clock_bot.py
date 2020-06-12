from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
class clockBot():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def login(self):
        self.driver.get('https://accessuh.uh.edu/login.php')
        cougarnet_in=self.driver.find_element_by_xpath('//*[@id="param1"]')
        pass_in=self.driver.find_element_by_xpath('//*[@id="param2"]')
        login_btn=self.driver.find_element_by_xpath('//*[@id="cougarnet-login"]/i/input')
        cougarnet_in.send_keys('dtngu212')
        pass_in.send_keys('Dethuong11@')
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

    def clock_in(self):
        sleep(3)
        #encounter dropdown value, need to use Selenium Select class 
        #Find the dropdown element using Select class 
        select=Select(self.driver.find_element_by_xpath('//*[@id="TL_RPTD_TIME_PUNCH_TYPE$0"]'))
        #Punch In value
        select.select_by_visible_text('In')
        #Click submit -- need to test this 
        submit_btn=self.driver.find_element_by_xpath('//*[@id="TL_WEB_CLOCK_WK_TL_SAVE_PB"]')
        submit_btn.click()

        
    def clock_out(self):
        sleep(3)
        select=Select(bot.driver.find_element_by_xpath('//*[@id="TL_RPTD_TIME_PUNCH_TYPE$0"]'))
        select.select_by_visible_text('Out')
        #Click submit -- need to test this 
        submit_btn=self.driver.find_element_by_xpath('//*[@id="TL_WEB_CLOCK_WK_TL_SAVE_PB"]')
        submit_btn.click()

        
bot = clockBot()
bot.login()
bot.get_to_punching_site()
bot.clock_in()
bot.clock_out()
#Now that the interations are finished, need to set up a schedule for the bot to run