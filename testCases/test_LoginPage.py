import time
from Pages.LoginPage import LoginPage
from Utilities.Base import Base
from dataSet.loginPageData import DDNI_VERSION
from Utilities.utilityFn import Utility


class TestLogin(Base):
    util = Utility()

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
        if self.util.checkEmptyInputFields(loginPage.getPassword()) or self.util.checkEmptyInputFields(
                loginPage.getUserName()):
            assert not self.util.checkActiveButton(loginPage.loginButton())

    def test_fill_Credentials(self):
        loginPage = LoginPage(self.driver)
        loginPage.getUserName().send_keys('admin')
        loginPage.getPassword().send_keys('admin')

    def test_nonEmpty_Fields(self):
        loginPage = LoginPage(self.driver)
        if self.util.checkEmptyInputFields(loginPage.getPassword()) == False and self.util.checkEmptyInputFields(
                loginPage.getUserName()) == False:
            assert self.util.checkActiveButton(loginPage.loginButton())

    def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.loginButton().click()
        time.sleep(6)
        url = self.driver.current_url
        assert "dashboard" in url
        # self.driver.find_element(By.CSS_SELECTOR, 'div.product-bar-add-item-button-container button').click()
