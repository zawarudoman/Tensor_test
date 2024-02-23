from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Base import BasePage


class SbisPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get("https://sbis.ru/")

    def click_contact(self):
        contact_link = self.driver.find_elements(By.CLASS_NAME, 'sbisru-Header__menu-link')
        contact_link[1].click()

    def click_download(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        return wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Скачать локальные версии")))

