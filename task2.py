import logging

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver

from pages.ContactPage import ContactPage
from pages.SbisPage import SbisPage


logging.basicConfig(filename="C:/Folder/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


def test_(driver):
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    sbis_page = SbisPage(driver)
    contact_page = ContactPage(driver)
    try:
        logger.info('Начало теста')
        sbis_page.open()
        sbis_page.click_contact()
        contact_page.check_region()
        spb_partners = contact_page.region_partners()
        assert contact_page.check_region().text == 'г. Санкт-Петербург'
        contact_page.click_change_kamchatka_region()
        wait.until(EC.url_contains('41-kamchatskij-kraj'))
        partners_kamchatka = contact_page.region_partners()
        assert EC.url_contains('41-kamchatskij-kraj')
        assert driver.title == 'СБИС Контакты — Камчатский край'
        assert spb_partners != partners_kamchatka
    finally:
        logger.debug("Конец теста")
        driver.quit()