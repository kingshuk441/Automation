import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Pages.LoginPage import LoginPage
from Pages.AlertsPage import AlertsPage
from Utilities.BaseClass import BaseClass
from Utilities.testData import TestData

@pytest.mark.usefixtures("initial")
class TestAlerts(BaseClass):



    def test_alerts(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        self.alerts_page.get_list_elements()


    def test_total_count(self):
        # it checks the total count
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.get_alerts_count() == self.alerts_page.get_alerts_list_length()

    def test_select_all(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.select_all()

    def test_SortbyEventDesc(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_event_desc()

    def test_SortbyUniqueDesc(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_event_unique_desc()

    def test_SortbyLastOccurrencetDesc(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_last_occurrence_desc()

    def test_SortbyFirstOccurrenceDESC(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_first_occurrence_desc()

    def test_SortbySeverityDesc(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_severity_desc()

    def test_SortbyEventASC(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_event_asc()

    def test_SortbyUniqueASC(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_event_unique_asc()

    def test_SortbyLastOccurrencetASC(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_last_occurrence_asc()

    def test_SortbyFirstOccurrenceASC(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_first_occurrence_asc()

    def test_SortbySeverityASC(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.sortby_severity_asc()

    def test_button_click_archived_alert(self):
        if self.alerts_page.no_alerts_found():
            print("No Alerts found")
            assert False
        assert self.alerts_page.button_click_archived_alert()


    @pytest.fixture()
    def initial(self, openBrowser):
        self.driver = openBrowser
        self.alerts_page = AlertsPage(self.driver)
        if not self.alerts_page.urlPresent(self.alerts_page.URL):
            self.loginPage = LoginPage(self.driver)
            self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
            self.alerts_page.open_alerts()
