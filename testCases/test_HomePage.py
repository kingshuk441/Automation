import pytest
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass
from Utilities.testData import TestData

from Pages.HomePage import HomePage
import time

@pytest.mark.usefixtures("initial")
class Test_Home(BaseClass):

    def reuse(self):
        self.driver.implicitly_wait(15)
        self.homepage = HomePage(self.driver)
        self.homepage.go_to_callhome()

    def test_homepage_title(self):
        #self.loginPage = LoginPage(self.driver)
        #homepage = self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
        homepage_title = self.homepage.get_homepage_title(TestData.HOME_PAGE_TITLE)
        assert homepage_title == TestData.HOME_PAGE_TITLE

    '''TESTCASE TO NAVIGATE TO CALLHOME PAGE'''

    def test_goto_callhome(self):
        self.reuse()
        #homepage = self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        #homepage.go_to_callhome()
        #self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        #self.homepage = HomePage(self.driver)
        uurl = self.homepage.get_cur_url()
        assert uurl == TestData.call_home_url

    '''IF callHome is off it turns on and viceversa'''
    def test_Click_CallHomeButton(self):
        self.reuse()
        time.sleep(3)
        assert self.homepage.do_callhome_button_click() == True

    def test_Get_count_TotalCases_in_Callhome(self):
        self.reuse()
        time.sleep(2)
        assert self.homepage.total_cases() == self.homepage.get_callhome_list_length()

    '''TESTCASE TO SORT USING CASE-NO IN CALLHOME'''

    def test_sort_by_case_no(self):
        self.reuse()
        self.homepage.sort_by_caseno()

    '''TESTCASE TO SORT USING TICKET-ID IN CALLHOME'''

    def test_sort_by_ticket_id(self):
        self.reuse()
        self.homepage.sort_by_TicketID()

    '''TESTCASE TO SORT USING SUBJECT IN CALLHOME'''

    def test_sort_by_SUBJECT(self):
        self.reuse()
        time.sleep(4)
        self.homepage.sort_by_Subject()

    '''TESTCASE TO SORT USING CREATED ON IN CALLHOME'''

    def test_sort_by_CreatedOn(self):
        self.reuse()
        self.homepage.sort_by_CreatedOn()

    '''TESTCASE TO SORT USING STATUS IN CALLHOME'''

    def test_sort_by_STATUS(self):
        self.reuse()
        self.homepage.sort_by_Status()

    '''TESTCASE FOR USING CONFIGURE IN CALLHOME'''

    def test_Configure_Callhome(self):
        self.reuse()
        time.sleep(4)
        res = self.homepage.configure_home(TestData.config_uname, TestData.config_passs)
        time.sleep(4)
        print(res)
        if res in "Success: Test Successful":
            self.homepage.configure_home_Save_btn()
            assert res == "Success: Test Successful"
        else:
            assert (res == "Error occured while connecting to Salesforce")
        #print(res)
        '''
        if(res == "Success: Test Successful"):
            homepage.configure_home_Save_btn()
            assert 1 == 1
        else:
            assert 1 == 2
            '''

    '''TEST CASE FOR CLICKING CANCEL BUTTON IN CALLHOME CONFIGURE'''

    def test_Configure_Callhome_Cancel_Btn(self):
        self.reuse()
        time.sleep(2)
        self.homepage.configure_home_Cancel_btn()

    def test_SELECTALL_IN_CALLHOME_CHECKBOX(self):
        self.reuse()
        self.homepage.click_selectall_checkbox()

    def test_Cancel_del_using_Xmark(self):
        self.reuse()
        self.homepage.cancel_del_using_xmark()

    @pytest.fixture()
    def initial(self, openBrowser):
        self.driver = openBrowser
        self.homepage = HomePage(self.driver)
        if not self.homepage.urlPresent(self.homepage.URL):
            self.loginPage = LoginPage(self.driver)
            self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
            self.homepage.go_to_callhome()