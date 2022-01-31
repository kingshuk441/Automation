import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    userName = (By.ID, 'user')
    password = (By.ID, "password")
    loginBtn = (By.CSS_SELECTOR, "button[type='submit']")
    radioBtn = (By.CSS_SELECTOR, "div.uwf-button-group-radio__item")
    version = (By.CSS_SELECTOR, "div.uwf-login-page__version")
    logOut = (By.XPATH, "//div[contains(text(),'Logout')]")
    loginUser = (By.CSS_SELECTOR, "div.uwf-navbar__settings-user")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getVersion(self):
        return self.driver.find_element(*LoginPage.version)

    def getUserName(self):
        return self.driver.find_element(*LoginPage.userName)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def loginButton(self):
        return self.driver.find_element(*LoginPage.loginBtn)

    def getRadioButtons(self):
        return self.driver.find_elements(*LoginPage.radioBtn)

    def getLoginUserBtn(self):
        return self.driver.find_element(*LoginPage.loginUser)

    def clickLogout(self):
        return self.driver.find_element(*LoginPage.logOut).click()

    def enterCredentials(self, userNameText='admin', passwordText='admin'):
        userName = self.getUserName()
        password = self.getPassword()
        submitBtn = self.loginButton()
        userName.send_keys(userNameText)
        password.send_keys(passwordText)
        submitBtn.click()
        time.sleep(5)

    def Logout(self):
        user = self.getLoginUserBtn()
        action = ActionChains(self.driver)
        action.move_to_element(user).perform()
        self.clickLogout()
        time.sleep(6)
