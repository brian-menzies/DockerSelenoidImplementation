from appium.webdriver.common.mobileby import MobileBy as By
from Helpers.BasePage import BasePage


class BasicPageObjects(BasePage):
    page_title = (By.CSS_SELECTOR, '.cell.light h2')
    first_image = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div > div.col-md-3 > img')
    first_link = (By.CSS_SELECTOR, 'div:nth-child(1) > div > div > div.col-md-9 a')