import os
import time

import pytest
from selenium import webdriver
from seleniumwire import webdriver

from pages.SbisDownloadPage import SbisDownloadPage
from pages.SbisPage import SbisPage


@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


def test(driver):
    sbis_page = SbisPage(driver)
    sbis_download_page = SbisDownloadPage(driver)
    try:
        sbis_page.open()
        download_button = sbis_page.click_download()
        driver.execute_script('arguments[0].click()', download_button)
        plagin_button = sbis_download_page.find_plugin_button()
        driver.execute_script('arguments[0].click()', plagin_button)
        sbis_download_page.click_download_button()
        assert sbis_download_page.download_button == '8.16'
    finally:
        driver.quit()

