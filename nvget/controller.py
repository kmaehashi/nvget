# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals  # NOQA

import requests
import selenium
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AuthenticationError(Exception):
    pass


class Controller(object):

    def __init__(self, chrome_path, driver_path, timeout):
        self.logged_in = False
        self._chrome_path = chrome_path
        self._driver_path = driver_path
        self._timeout = timeout
        self._cookies = None

    def login(self, email, password, nvidia_account):
        options = selenium.webdriver.ChromeOptions()
        options.binary_location = self._chrome_path
        options.add_argument('headless')

        driver = selenium.webdriver.Chrome(
            executable_path=self._driver_path,
            chrome_options=options)

        try:
            driver.set_page_load_timeout(self._timeout)
            driver.set_script_timeout(self._timeout)

            # Go to top page.
            driver.get('https://developer.nvidia.com/')
            driver.find_element_by_link_text('Login').click()

            # Wait for the login form to be drawn.
            WebDriverWait(driver, self._timeout).until(
                EC.element_to_be_clickable(
                    (By.PARTIAL_LINK_TEXT,
                     'Log in with my NVIDIA Account'))
            )

            if nvidia_account:
                raise NotImplementedError('not supported yet')
            else:
                driver.find_element_by_partial_link_text(
                    'Use my older NVIDIA Developer credentials').click()

            # Fill in the form and submit.
            driver.find_element_by_id(
                'dz-auth-form-login-email').send_keys(email)
            driver.find_element_by_id(
                'dz-auth-form-login-password').send_keys(password)
            driver.find_element_by_id(
                'dz-auth-form-login-button-next').click()

            WebDriverWait(driver, self._timeout).until(
                login_response_is_ready()
            )

            # Login succeed.
            if len(driver.find_elements_by_xpath('//a[@href="/user/logout"]')):
                self._cookies = driver.get_cookies()
                self.logged_in = True
                return

            # Login failed.
            raise AuthenticationError(driver.find_element_by_id(
                'dz-auth-form-login-password-error-flag').text)

        finally:
            driver.quit()

    def _get_cookie_jar(self):
        assert self.logged_in
        jar = requests.cookies.RequestsCookieJar()
        for cookie in self._cookies:
            jar.set(**{
                key: cookie[key]
                for key in ['name', 'value', 'domain', 'path']
            })
        return jar

    def download(self, url):
        response = requests.get(
            url, cookies=self._get_cookie_jar(), stream=True)
        status = response.status_code
        if status != 200:
            raise RuntimeError(
                'download failed with HTTP status {}'.format(status))
        return response

    def download_to(self, url, path):
        with open(path, 'wb') as f:
            for chunk in self.download(url):
                f.write(chunk)


class login_response_is_ready(object):
    def __call__(self, driver):
        # Login succeed if logout link is available.
        if 0 < len(driver.find_elements_by_xpath('//a[@href="/user/logout"]')):
            return True

        # Login failed if error flag is available.
        try:
            return 0 < len(driver.find_elements_by_id(
                'dz-auth-form-login-password-error-flag'))
        except StaleElementReferenceException:
            return False

        return False
