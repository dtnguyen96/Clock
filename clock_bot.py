from selenium import webdriver
from time import sleep
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
    def clockIn(self):
        #wait for page to load 
        sleep(3)
        hr_icon=self.driver.find_element_by_xpath('//*[@id="portal_area"]/div[2]/div/div[2]/div[4]/a/div[1]/img')
        hr_icon.click()
        
bot = clockBot()
bot.login()
bot.clockIn()
