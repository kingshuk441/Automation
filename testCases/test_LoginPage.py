import time
from Pages.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass
from Utilities.testData import TestData
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

    def test_Invalid_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.getUserName().send_keys(TestData.Invalid_ID)
        loginpage.getPassword().send_keys(TestData.Invalid_Pswd)
        res = loginpage.do_Invalid_login()
        assert res.lower() in TestData.Invalid_login_text.lower()

    def test_unhide_password(self):
        loginpage = LoginPage(self.driver)
        res = loginpage.do_unhide_password(TestData.USERNAME, TestData.PASSWORD)
        assert res == True

    def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.loginButton().click()
        time.sleep(6)
        url = self.driver.current_url
        assert "dashboard" in url

    # def test_change_password(self):
    #     loginPage = LoginPage(self.driver)
    #     loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
    #     res = loginPage.do_simple_change_password(TestData.old_password, TestData.new_password,
    #                                               TestData.retype_password)
    #     if res:
    #         # TestData.PASSWORD = TestData.new_password
    #         loginPage.update_password()
    #         time.sleep(3)
    #         loginPage.enterCredentials(TestData.USERNAME, TestData.new_password)
    #     else:
    #         assert res
    #
    # def test_cancel_change_password(self):
    #     loginPage = LoginPage(self.driver)
    #     loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
    #     loginPage.do_simple_change_password(TestData.old_password, TestData.new_password, TestData.retype_password)
    #     loginPage.cancel_update_password()
    #
    # def test_advance_change_password(self):
    #     loginPage = LoginPage(self.driver)
    #     loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
    #     res = loginPage.do_advanced_change_password(TestData.PASSWORD, TestData.new_A_P, TestData.retype_A_P)
    #     if res:
    #         TestData.PASSWORD = TestData.new_A_P
    #         loginPage.update_password()
    #         time.sleep(3)
    #         loginPage.enterCredentials(TestData.USERNAME, TestData.new_A_P)
    #     else:
    #         assert res
