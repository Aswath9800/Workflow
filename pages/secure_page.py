from selenium.webdriver.common.by import By

class SecurePage:
    def __init__(self, driver):
        self.driver = driver

    def get_flash_message(self):
        return self.driver.find_element(By.ID, "flash").text

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()
