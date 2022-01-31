import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Pages.LoginPage import LoginPage
from Pages.AlertsPage import AlertsPage
from Utilities.BaseClass import BaseClass
from Utilities.testData import TestData


class TestAlerts(BaseClass):

    def reuse(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
        self.driver.implicitly_wait(5)
        self.alerts_page = AlertsPage(self.driver)
        self.alerts_page.open_alerts()

    def test_alerts(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
        self.driver.implicitly_wait(5)
        self.alerts_page = AlertsPage(self.driver)
        self.alerts_page.open_alerts()
        self.alerts_page.get_list_elements()

    def test_no_alerts_found(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
        self.driver.implicitly_wait(10)
        self.alerts_page = AlertsPage(self.driver)
        self.alerts_page.open_alerts()
        time.sleep(5)
        a = ActionChains(self.driver)
        a.key_down(Keys.CONTROL).send_keys('+').perform()
        ''' 
        self.driver.set_window_size(3840, 1938, self.driver.window_handles[0])
        self.driver.execute_script("document.body.style.zoom='40%'")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(100,1000)","")
        '''

    def test_total_count(self):
        # it checks the total count
        self.reuse()
        self.alerts_page.wait_till_page_load()
        assert self.alerts_page.get_alerts_count() == self.alerts_page.get_alerts_list_length()

    def test_select_all(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        self.alerts_page.select_all()

    def test_SortbyEventDesc(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        time.sleep(2)
        assert self.alerts_page.sortby_event_desc()

    def test_SortbyEventASC(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        time.sleep(2)
        assert self.alerts_page.sortby_event_asc()

    def test_SortbyUniqueDesc(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        time.sleep(2)
        assert self.alerts_page.sortby_event_unique_desc()

    def test_SortbyUniqueASC(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        time.sleep(2)
        assert self.alerts_page.sortby_event_unique_asc()

    def test_SortbyLastOccurrencetDesc(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        time.sleep(2)
        assert self.alerts_page.sortby_last_occurrence_desc()

    def test_SortbyFirstOccurrenceASC(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        time.sleep(2)
        assert self.alerts_page.sortby_last_occurrence_asc()

    def test_SortbySeverityDesc(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        time.sleep(2)
        assert self.alerts_page.sortby_severity_desc()

    def test_SortbySeverityASC(self):
        self.reuse()
        self.alerts_page.wait_till_page_load()
        time.sleep(2)
        assert self.alerts_page.sortby_severity_asc()

    def test_button_click_archived_alert(self):
        self.reuse()
        assert self.alerts_page.button_click_archived_alert()
