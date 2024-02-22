from selenium.webdriver.common.by import By

from pages.Base import BasePage


class TensorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def find_force_people(self):
        return self.driver.find_elements(By.CLASS_NAME, 'tensor_ru-Index__card-title')[1]

    def find_about_people(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'a[class="tensor_ru-link tensor_ru-Index__link"]')

    def find_photos(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'div[class="tensor_ru-About__block3-image-wrapper"]')