import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

class Browser:
    browser, service = None, None
    amzn_user, amzn_pass = '', ''

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()
    
    def set_amazon_details(self, file_name: str):
        amzn_details = open(file_name, 'r')
        info = amzn_details.readlines()
        self.amzn_user = info[0]
        self.amzn_pass = info[1]
        # print(amzn_user)
        # print(amzn_pass)


if __name__ == '__main__':
        browser = Browser('drivers\chromedriver_win32\chromedriver.exe')
        browser.set_amazon_details('logins.txt')
        browser.open_page('https://www.amazon.com/registries/gl/owner-view/QLTIXIO3O0Y7?share=false')
        
        print("username: %s" % browser.amzn_user)
        print("password: %s" % browser.amzn_pass)

        time.sleep(1)

        # Logging in to Amazon, this step can fail easily if amazon requests user to input captcha, seems to happen every so often

        # Need to add "captcha alert system" to let user/manager know they need to manually log in

        element_nav_sign_in = browser.browser.find_element(By.CLASS_NAME, 'nav-action-button')

        signin_link = element_nav_sign_in.get_attribute('href')

        browser.open_page(signin_link)

        time.sleep(1)

        email_element = browser.browser.find_element(By.NAME, 'email')
        email_element.send_keys(browser.amzn_user)

        time.sleep(1)

        password_element = browser.browser.find_element(By.NAME, 'password')
        password_element.send_keys(browser.amzn_pass)

        time.sleep(1)

        signin_element = browser.browser.find_element(By.ID, 'signInSubmit')
        signin_element.click()

        time.sleep(1)

        # Open registry after signin in
        browser.open_page('https://www.amazon.com/registries/gl/owner-view/QLTIXIO3O0Y7?share=false')

        time.sleep(10)

        # Get all home page items listed on registry

        food_items = browser.browser.find_elements(By.CLASS_NAME, 'gr-product-tile')
        file_name = 'food_data_' + str(datetime.date.today()) + '.txt' 
        food_database = open(file_name, 'w')
        food_database.write('Item, Price')
        for item in food_items:
             # Go to product's amazon page
            #  browser.open_page(str(item.get_attribute('href')))
             time.sleep(1)
             product = item.find_element(By.CLASS_NAME, 'gr-product-title').text
             price = item.find_element(By.CLASS_NAME, 'gr-price-container').find_element(By.CLASS_NAME,'gr-product-tile-price-strikethrough').text
             entry = str(product) + ', ' + str(price) + '\n'
             print(entry)
             food_database.write(entry)
             

        food_database.close()

        browser.open_page('https://www.amazon.com/registries/gl/owner-view/QLTIXIO3O0Y7?share=false')
        time.sleep(20)

        # Get all users who've donated to registry

        # It's suggested to sign out of account to lower captcha frequencies, the less we sign in to the account, the less captchas we will encounter.

        browser.close_browser()


