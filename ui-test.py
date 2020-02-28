"""
A simple selenium test example demonstrating docker container usage.
Thanks to @joyzoursky for the test script https://github.com/joyzoursky/docker-python-chromedriver
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

import os.path
import subprocess
from subprocess import PIPE

import time

class TestTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """Start web driver and start the docker container"""
        p = subprocess.Popen(['docker-compose', '-p ui_test', 'up', '-d'])
        time.sleep(5)
        p.wait()
        chrome_options =  webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-setuid-sandbox")
        """uncomment below for running in headless mode"""
        """chrome_options.add_argument('--headless')"""
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--disable-extensions")
        """selenium docker container is set to run on port 1111"""
        self.driver = webdriver.Remote(desired_capabilities=chrome_options.to_capabilities(), command_executor='http://localhost:1111/wd/hub')
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(self):
        """Stop web driver and remove the docker container"""
        self.driver.quit()
        p = subprocess.Popen(['sh', './clean.sh'])
        time.sleep(5)
        p.wait()

    def test_case_1(self):
        """Find and click top-right button"""
        try:
            self.driver.get('https://www.oursky.com/')
            el = self.driver.find_element_by_class_name('btn-header')
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_2(self):
        """Find and click Learn more button"""
        try:
            self.driver.get('https://www.oursky.com/')
            el = self.driver.find_element_by_xpath(".//*[@id='tag-line-wrap']/span/a")
            el.click()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
