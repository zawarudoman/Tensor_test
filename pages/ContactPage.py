import time

from selenium.webdriver.common.by import By

from pages.Base import BasePage


class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def find_element_tensor_link(self):
        return self.driver.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')

    def click_on_element(self,):
        return self.find_element_tensor_link().click()

    def check_region(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'span[class="sbis_ru-Region-Chooser__text sbis_ru-link"]')

    def region_partners(self):
        return self.driver.find_elements(By.CLASS_NAME, 'sbisru-Contacts-List__name')

    def click_change_kamchatka_region(self):
        self.check_region().click()
        time.sleep(2)
        kamchatka_region = self.driver.find_elements(By.CLASS_NAME, 'sbis_ru-link')
        kamchatka_region[42].click()
        return kamchatka_region
