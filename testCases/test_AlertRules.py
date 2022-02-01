import pytest

from Pages.LoginPage import LoginPage
from Pages.AlertrulesPage import AlertRulesPage
from Utilities.BaseClass import BaseClass
from Utilities.testData import TestData

@pytest.mark.usefixtures("initial")
class TestAlertsRules(BaseClass):

    def reuse(self):
        self.driver.implicitly_wait(15)
        '''
        self.loginPage = LoginPage(self.driver)
        # self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

        self.alert_rule_page = AlertRulesPage(self.driver)
        self.alert_rule_page.open_alert_rules()
        '''
        #  self.alert_rule_page = AlertRulesPage(self.driver)
        #self.alert_rule_page.open_alert_rules()
        # self.alert_rule_page.verify_its_that_page() # return list but in this case using for wait

    def test_alertrules(self):
        # wait = WebDriverWait(self.driver, 30)
        '''
        wait.until(expected_conditions.presence_of_element_located((By.ID, "user")))
        self.loginPage = LoginPage(self.driver)
        self.loginPage.credentials()
        '''
        '''
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.driver.implicitly_wait(5)
        self.alert_rule_page = AlertRulesPage(self.driver)
        self.alert_rule_page.open_alert_rules()
        '''
        self.reuse()
        assert self.alert_rule_page.verify_its_that_page() == 3
        # print(self.alert_rule_page.no_of_elements_in_that_page())
        '''
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(text(),'Manage')]")))
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Manage')]").click()
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(text(),'Alert Rules')]")))
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Alert Rules')]").click()
        '''
        # utility.waitElement(self.driver, "//div[contains(text(),'Policy Engine Off')]")
        # self.driver.find_element(By.XPATH, "//div[contains(text(),'Policy Engine Off')]").click()
        '''
        self.driver.find_element(By.XPATH,"//div[(text()='Notification Off')]").click()
        self.driver.find_element(By.XPATH, "//div[(text()='Notification Off')]").click()'''

    def test_buttonStatus(self):
        #self.reuse()
        #self.alert_rule_page = AlertRulesPage(self.driver)
        #self.alert_rule_page.open_alert_rules()
        self.reuse()
        self.alert_rule_page.status_of_button()

    def test_buttonClickNotification(self):
        self.reuse()
        assert self.alert_rule_page.button_click_notification() == True

    def test_buttonClickWarning(self):
        self.reuse()
        assert self.alert_rule_page.button_click_warning() == True

    def test_buttonClickError(self):
        self.reuse()
        assert self.alert_rule_page.button_click_error() == True

    def test_buttonClickCritical(self):
        self.reuse()
        assert self.alert_rule_page.button_click_critical() == True

    def test_buttonClickEmergency(self):
        self.reuse()
        assert self.alert_rule_page.button_click_emergency() == True

    def test_buttonClickPolicy(self):
        self.reuse()
        assert self.alert_rule_page.button_click_policy() == True

    def test_buttonClickEmail(self):
        self.reuse()
        assert self.alert_rule_page.button_click_email() == True

    def test_buttonClickCustomPloicy(self):
        self.reuse()
        self.alert_rule_page.wait_till_page_load()
        assert self.alert_rule_page.button_click_custom_policy()

    def test_buttonClickAddRecipient(self):
        self.reuse()
        self.alert_rule_page.wait_till_page_load()
        assert self.alert_rule_page.button_click_add_recipient()

    def test_NotificationOffDisable(self):
        self.reuse()
        assert self.alert_rule_page.button_notification_off_disable_all() == True

    def test_SortbyEventTypeDESC(self):
        self.reuse()
        print(self.alert_rule_page.sortby_event_desc())

    def test_SortbyStatusDESC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_status_desc()

    def test_SortbyEventTypeASC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_event_asc()

    def test_SortbyStatusASC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_status_asc()

    def test_HoverHelpTrigger(self):
        self.reuse()
        self.alert_rule_page.hover_help_button()

    def test_total_count_policy(self):
        self.reuse()
        assert self.alert_rule_page.get_policies_count() == self.alert_rule_page.get_policies_length()

    def test_total_count_recipients(self):
        self.reuse()
        assert self.alert_rule_page.get_recipients_count() == self.alert_rule_page.get_recipients_length()

    def test_policy_select_all(self):
        self.reuse()
        assert self.alert_rule_page.select_all_policy()

    def test_recipients_select_all(self):
        self.reuse()
        assert self.alert_rule_page.select_all_recipients()

    def test_status_button_click(self):
        self.reuse()
        assert self.alert_rule_page.status_button_click()

    def test_SortbyToDESC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_to_desc()

    def test_SortbyEsDESC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_es_desc()

    def test_SortbySfaDESC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_sfa_desc()

    def test_SortbyInsightDESC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_insight_desc()

    def test_SortbyToASC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_to_asc()

    def test_SortbyEsASC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_es_asc()

    def test_SortbySfaASC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_sfa_asc()

    def test_SortbyInsightASC(self):
        self.reuse()
        assert self.alert_rule_page.sortby_insight_asc()

    def test_button_add_recipient_es(self):
        self.reuse()
        self.alert_rule_page.wait_till_page_load()

    @pytest.fixture()
    def initial(self, openBrowser):
        self.driver = openBrowser
        self.alert_rule_page = AlertRulesPage(self.driver)
        if not self.alert_rule_page.urlPresent(self.alert_rule_page.URL):
            self.loginPage = LoginPage(self.driver)
            self.loginPage.enterCredentials(TestData.USERNAME, TestData.PASSWORD)
            self.alert_rule_page.open_alert_rules()
            self.alert_rule_page.wait_till_page_load()
