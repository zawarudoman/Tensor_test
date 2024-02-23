import logging

import pytest
from selenium import webdriver
from seleniumwire import webdriver

from pages.ContactPage import ContactPage
from pages.SbisPage import SbisPage
from pages.TensorPage import TensorPage


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


def test_follow_link_tensor_about(driver):
    sbis_page = SbisPage(driver)
    contact_page = ContactPage(driver)
    tensor_page = TensorPage(driver)
    try:
        logger.debug('Начало теста')
        sbis_page.open()
        sbis_page.click_contact()
        contact_page.find_element_tensor_link()
        contact_page.click_on_element()
        driver.switch_to.window(driver.window_handles[1])
        logger.info(f'Переход на новую вкладку {driver.current_url}')
        forse_people = tensor_page.find_force_people()
        assert forse_people.is_displayed()
        assert forse_people.text == 'Сила в людях'
        find_about_people = tensor_page.find_about_people()
        driver.execute_script('arguments[0].click()', find_about_people[1])
        assert 'https://tensor.ru/about' == driver.current_url
        photos = tensor_page.find_photos()
        logger.info(f'Получен список фотографий: {photos}')
        first_photo = photos[0]
        first_photo_height = first_photo.size['height']
        first_photo_width = first_photo.size['width']
        for photo in photos:
            assert photo.size['height'] == first_photo_height
            assert photo.size['width'] == first_photo_width
    finally:
        logger.debug("Конец теста")
        driver.quit()
