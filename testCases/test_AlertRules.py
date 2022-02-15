import time

import pytest

from Pages.LoginPage import LoginPage
from Pages.AlertrulesPage import AlertRulesPage
from Utilities.BaseClass import BaseClass
from Utilities.testData import TestData

@pytest.mark.usefixtures("initial")
class TestAlertsRules(BaseClass):

    def test_alertrules(self):
        assert self.alert_rule_page.verify_its_that_page() == 3

    def test_buttonStatus(self):
        self.alert_rule_page.status_of_button()

    def test_buttonClickNotification(self):
        assert self.alert_rule_page.button_click_notification() == True

    def test_buttonClickWarning(self):
        assert self.alert_rule_page.button_click_warning() == True

    def test_buttonClickError(self):
        assert self.alert_rule_page.button_click_error() == True

    def test_buttonClickCritical(self):
        assert self.alert_rule_page.button_click_critical() == True

    def test_buttonClickEmergency(self):
        assert self.alert_rule_page.button_click_emergency() == True

    def test_buttonClickPolicy(self):
        assert self.alert_rule_page.button_click_policy() == True

    def test_buttonClickEmail(self):
        assert self.alert_rule_page.button_click_email() == True

    def test_buttonClickCustomPloicy(self):
        assert self.alert_rule_page.button_click_custom_policy()

    def test_NotificationOffDisable(self):
        assert self.alert_rule_page.button_notification_off_disable_all() == True

    def test_buttonClickAddRecipient(self):
        assert self.alert_rule_page.button_click_add_recipient()

    def test_SortbyEventTypeDESC(self):
        print(self.alert_rule_page.sortby_event_desc())

    def test_SortbyStatusDESC(self):
        assert self.alert_rule_page.sortby_status_desc()

    def test_SortbyEventTypeASC(self):
        assert self.alert_rule_page.sortby_event_asc()

    def test_SortbyStatusASC(self):
        assert self.alert_rule_page.sortby_status_asc()

    def test_HoverHelpTrigger(self):
        self.alert_rule_page.hover_help_button()

    def test_total_count_policy(self):
        assert self.alert_rule_page.get_policies_count() == self.alert_rule_page.get_policies_length()

    def test_total_count_recipients(self):
        assert self.alert_rule_page.get_recipients_count() == self.alert_rule_page.get_recipients_length()

    def test_policy_select_all(self):
        assert self.alert_rule_page.select_all_policy()

    def test_recipients_select_all(self):
        assert self.alert_rule_page.select_all_recipients()

    def test_status_button_click(self):
        assert self.alert_rule_page.status_button_click()

    def test_SortbyToDESC(self):
        assert self.alert_rule_page.sortby_to_desc()

    def test_SortbyEsDESC(self):
        assert self.alert_rule_page.sortby_es_desc()

    def test_SortbySfaDESC(self):
        assert self.alert_rule_page.sortby_sfa_desc()

    def test_SortbyInsightDESC(self):
        assert self.alert_rule_page.sortby_insight_desc()

    def test_SortbyToASC(self):
        assert self.alert_rule_page.sortby_to_asc()

    def test_SortbyEsASC(self):
        assert self.alert_rule_page.sortby_es_asc()

    def test_SortbySfaASC(self):
        assert self.alert_rule_page.sortby_sfa_asc()

    def test_SortbyInsightASC(self):
        assert self.alert_rule_page.sortby_insight_asc()

    def test_button_add_recipient_es(self):
        pass
        # //div[@class='product-type ng-star-inserted'][1]/div[2]


    @pytest.fixture()
    def initial(self, openBrowser):
        self.driver = openBrowser
        self.alert_rule_page = AlertRulesPage(self.driver)
        self.driver.implicitly_wait(5)
        if not self.alert_rule_page.urlPresent(self.alert_rule_page.URL):
            self.loginPage = LoginPage(self.driver)
            self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
            self.alert_rule_page.open_alert_rules()
            time.sleep(3)
            # self.alert_rule_page.wait_till_page_load()
