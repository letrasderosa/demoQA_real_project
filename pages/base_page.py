from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

import time

# url = ""

class Base_Page:
    """
    Base Page setup and methods.
    """
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.wait = WebDriverWait(browser, timeout=timeout, poll_frequency=0.2,
                     ignored_exceptions=[ElementNotVisibleException,
                                         NoSuchElementException,
                                         TimeoutException, WebDriverException,
                                         StaleElementReferenceException]) # wait for page to load
    def open(self):
        self.browser.get(self.url)
        time.sleep(self.timeout) # wait for page to load

    def is_element_visible(self, locator):
        # return self.browser.find_element(locator)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def are_elements_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def is_element_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def are_elements_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_element_not_visible(self,locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def is_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element) # scroll to element on page




