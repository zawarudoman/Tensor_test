from selenium.webdriver.common.by import By

from pages.Base import BasePage


class SbisDownloadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def find_plugin_button(self):
        return self.driver.find_elements(By.CLASS_NAME, 'controls-tabButton__overlay')[1]

    def click_download_button(self):
        return self.driver.find_elements(
            By.CSS_SELECTOR, 'a[class="sbis_ru-DownloadNew-loadLink__link js-link"]'
        )[10].click()