from selenium.webdriver.common.by import By

from pages.Base import BasePage


class SbisPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get("https://sbis.ru/")

    def click_contact(self):
        contact_link = self.driver.find_elements(By.CLASS_NAME, 'sbisru-Header__menu-link')
        contact_link[1].click()


