import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Utilities.testData import TestData


class LoginPage(BasePage):
    user = (By.XPATH, "//input[@id='user']")
    pwd = (By.XPATH, "//input[@id='password']")
    signin_button = (By.CSS_SELECTOR, "button[type='submit']")
    userName = (By.ID, 'user')
    password = (By.ID, "password")
    loginBtn = (By.CSS_SELECTOR, "button[type='submit']")
    radioBtn = (By.CSS_SELECTOR, "div.uwf-button-group-radio__item")
    version = (By.CSS_SELECTOR, "div.uwf-login-page__version")
    logOut = (By.XPATH, "//div[contains(text(),'Logout')]")
    loginUser = (By.CSS_SELECTOR, "div.uwf-navbar__settings-user")
    Invalid_creds = (By.XPATH, "//div[contains(text(),'Invalid credentials')]")
    Show_Password = (By.XPATH,
                     "//button[@class='uwf-form-field__password-toggle uwf-btn uwf-btn_icon uwf-btn_icon-no-indentations ng-star-inserted']")
    SETTINGS_ICON = (By.XPATH, "//uwf-icon[@class='uwf-navbar__settings-icon']")
    CHANGE_PASSWORD = (By.XPATH, "//div[contains(text(),'Change Password')]")
    OLD_PASSWORD = (By.XPATH, "//input[@placeholder='Enter Old Password']")
    New_Password = (By.XPATH, "//input[@placeholder='Enter New Password']")
    Retype_new_Password = (By.XPATH, "//input[@placeholder='Retype New Password']")
    UPDATE_PASSWORD_BTN = (By.XPATH, "//button[contains(text(),'Update password')]")
    CANCEL_UPDATE_PASSWORD_BTN = (By.XPATH, "//button[contains(text(),'Cancel')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def do_login(self, username, password):
        self.do_send_keys(self.user, username)
        self.do_send_keys(self.pwd, password)
        self.do_click(self.signin_button)

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

    def do_Invalid_login(self):
        self.do_click(self.loginBtn)
        time.sleep(3)
        ele=""
        if self.is_visible(self.Invalid_creds):
            ele = self.get_element_text(self.Invalid_creds)
        return ele

    def do_unhide_password(self, username, password):
        f = False
        self.do_send_keys(self.userName, username)
        self.do_send_keys(self.password, password)
        time.sleep(2)
        if self.is_visible(self.Show_Password):
            f = True
            self.do_click(self.Show_Password)
            time.sleep(2)
        return f

    def do_simple_change_password(self, old, new, retype):
        time.sleep(2)
        self.do_click(self.SETTINGS_ICON)
        time.sleep(2)
        self.do_click(self.CHANGE_PASSWORD)
        time.sleep(2)
        if self.is_visible(self.OLD_PASSWORD):
            time.sleep(3)
            self.do_send_keys(self.OLD_PASSWORD, old)
        if self.is_visible(self.New_Password):
            time.sleep(3)
            self.do_send_keys(self.New_Password, new)
        if self.is_visible(self.Retype_new_Password):
            time.sleep(3)
            self.do_send_keys(self.Retype_new_Password, retype)
        time.sleep(3)
        if (old == TestData.PASSWORD) and (new == retype) and (len(new) > 4):
            return True
        else:
            return False

    def update_password(self):
        if self.is_visible(self.UPDATE_PASSWORD_BTN):
            self.do_click(self.UPDATE_PASSWORD_BTN)

    def cancel_update_password(self):
        if self.is_visible(self.CANCEL_UPDATE_PASSWORD_BTN):
            self.do_click(self.CANCEL_UPDATE_PASSWORD_BTN)

    def do_advanced_change_password(self, old, new, retype):
        time.sleep(2)
        self.do_click(self.SETTINGS_ICON)
        time.sleep(2)
        self.do_click(self.CHANGE_PASSWORD)
        time.sleep(2)
        if self.is_visible(self.OLD_PASSWORD):
            time.sleep(3)
            self.do_send_keys(self.OLD_PASSWORD, old)
        if self.is_visible(self.New_Password):
            time.sleep(3)
            self.do_send_keys(self.New_Password, new)
        if self.is_visible(self.Retype_new_Password):
            time.sleep(3)
            self.do_send_keys(self.Retype_new_Password, retype)
        time.sleep(3)
        l, u, p, d, f = 0, 0, 0, 0, 0
        for i in new:
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if i.isdigit():
                d += 1
            if i == '@' or i == '_' or i == '$':
                p += 1

        if l > 0 and u > 0 and d > 0 and p > 0 and l + u + p + d == len(new):
            f = 1
        time.sleep(2)
        if (old == TestData.PASSWORD) and (new == retype) and (len(new) > 7 and f == 1):
            return True
        else:
            return False