import time
from Pages.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass
from dataSet.loginPageData import DDNI_VERSION


class TestLogin(BaseClass):

    def test_DDN_Version(self):
        loginPage = LoginPage(self.driver)
        time.sleep(4)
        assert loginPage.getVersion().text == DDNI_VERSION

    def test_clickRadioBtn(self):
        loginPage = LoginPage(self.driver)
        btns = loginPage.getRadioButtons()
        for i in range(len(btns)):
            btns[i].click()
            assert "selected" in btns[i].get_attribute("class") and not "selected" in btns[(i + 1) % 2].get_attribute(
                "class")

    def test_empty_Fields(self):
        loginPage = LoginPage(self.driver)
        if loginPage.checkEmptyInputFields(loginPage.getPassword()) or loginPage.checkEmptyInputFields(
                loginPage.getUserName()):
            assert not loginPage.checkActiveButton(loginPage.loginButton())

    def test_fill_Credentials(self):
        loginPage = LoginPage(self.driver)
        loginPage.getUserName().send_keys('admin')
        loginPage.getPassword().send_keys('admin')

    def test_nonEmpty_Fields(self):
        loginPage = LoginPage(self.driver)
        if loginPage.checkEmptyInputFields(loginPage.getPassword()) == False and loginPage.checkEmptyInputFields(
                loginPage.getUserName()) == False:
            assert loginPage.checkActiveButton(loginPage.loginButton())

    def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.loginButton().click()
        time.sleep(6)
        url = self.driver.current_url
        assert "dashboard" in url
