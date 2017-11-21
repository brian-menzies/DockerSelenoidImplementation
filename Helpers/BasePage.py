import os
import time

from Helpers.FilePath import get_full_path

os.environ['PROJECTFOLDER'] = get_full_path('')
from time import sleep
from hotdog.BasePage import HotDogBasePage
from hotdog.Retry import Retry
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from hotdog.TestStep import TestStep
import builtins


class BasePage(HotDogBasePage):
    _loadingOverlay = (By.CLASS_NAME, 'loading')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    @TestStep("Check to see if Element Exists")
    def element_exists(self, element):
        try:
            displayed = element.is_displayed()
            return True if displayed else False
        except:
            return False


    def wait_for_ajax(self, timeout = 10):
        start = time.time()

        # bkd - a different way to wait, maybe useful
        # WebDriverWait(self.driver, timeout).until(lambda d: self.driver.execute_script("return jQuery.active == 0"),\
        #                                         'Timeout waiting for ajax to finish')
        while True:  # Handle timeout somewhere
            ajax_complete = self.driver.execute_script("return window.jQuery !=undefined && jQuery.active == 0")
            if ajax_complete:
                break
            if time.time() - start > timeout:
                break
                # raise Exception("Ajax did not finish before timeout.")
            else:
                sleep(1)


    def wait_for_loading_icon(self, timeout = 20):
        start = time.time()
        while True:
            try:
                if self.find('_loadingOverlay').is_not_displayed():
                    return
                if time.time() - start > timeout:
                    raise Exception("Loading Icon did not disappear before timeout.")
            except NoSuchElementException:
                return
            sleep(1)


    def sync(self, timeout=15):
        # if self.driver.name.lower() == 'internet explorer':
        #     sleep(5) # IE takes longer to load
        #     timeout = 30
        if hasattr(self, 'sync_element'):
            self.find('sync_element')
        else:
            sleep(5)

        self.wait_for_loading_icon(timeout=timeout)
        self.wait_for_ajax()
        super().sync(timeout=timeout)


    @Retry
    def assert_element_exists(self, element, name):
        assert self.element_exists(element), 'Element [%s] not found' % name


    @Retry
    def assert_in_url(self, string):
        assert string in self.driver.current_url, 'Did not load page with string [%s]' % string


    @TestStep('Scroll to the end of the page')
    def scroll_to_end_of_page(self, offset = 0, sleep_time = 1):
        '''Scrolls to the end of the page dynamically. It will keep scrolling to the end of the page until
        there aren't anymore elements loaded dynamically.
        '''
        page_height = self.driver.execute_script('return document.body.scrollHeight')
        new_page_height = 0

        while page_height is not new_page_height:
            self.driver.execute_script("window.scrollTo(0, (%s))" % (page_height - offset))
            sleep(sleep_time)
            new_page_height = self.driver.execute_script('return document.body.scrollHeight')
            if new_page_height > page_height:
                page_height = new_page_height
                new_page_height = 0
            else:
                page_height = new_page_height

    def scroll_to_top_of_page(self):
        self.driver.execute_script('window.scrollTo(0,0)')

    @TestStep('Check if Mobile Driver', True)
    def is_mobile(self):
        """ does the driver report running on Android or iOS
            :return: boolean: true of ios or android
        """
        # capabilities dictionary doesn't have platformName for all environments
        try:
            if 'mobileEmulation' in builtins.threadlocal.config['desiredCaps']['chromeOptions']:
                return True
        except KeyError:
            return False
