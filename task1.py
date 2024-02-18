import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumwire import webdriver


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


def test_follow_link_tensor_about(browser):
    browser.get("https://sbis.ru/")
    menu = browser.find_elements(By.CLASS_NAME, 'sbisru-Header__menu-link')
    menu[1].click()
    tensor = browser.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
    tensor.click()
    browser.switch_to.window(browser.window_handles[1])
    find_forse_people = browser.find_elements(By.CLASS_NAME, 'tensor_ru-Index__card-title')
    assert find_forse_people[1].is_displayed()
    assert find_forse_people[1].text == 'Сила в людях'
    find_forse_people = browser.find_elements(By.CSS_SELECTOR, 'a[class="tensor_ru-link tensor_ru-Index__link"]')
    browser.execute_script('arguments[0].click()', find_forse_people[1])
    assert 'https://tensor.ru/about' == browser.current_url
    photos = browser.find_elements(By.CSS_SELECTOR, 'div[class="tensor_ru-About__block3-image-wrapper"]')
    first_photo = photos[0]
    first_photo_height = first_photo.size['height']
    first_photo_width = first_photo.size['width']
    for photo in photos:
        assert photo.size['height'] == first_photo_height
        assert photo.size['width'] == first_photo_width
    browser.quit()
