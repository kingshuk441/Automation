import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class AlertsPage(BasePage):
    button_manage = (By.XPATH, "//div[contains(text(),'Manage')]")
    button_alerts = (By.XPATH, "//div[contains(text(),'Alerts')]")
    button_event_type = (By.XPATH, "(//div[contains(text(), 'Event Type')])[1]")
    button_event_unique_id = (By.XPATH, "(//div[contains(text(), 'Event Unique ID')])[1]")
    button_last_occurrence = (By.XPATH, "(//div[contains(text(), 'Last occurrence')])[1]")
    button_first_occurrence_time = (By.XPATH, "(//div[contains(text(), 'First occurrence Time')])[1]")
    button_severity = (By.XPATH, "(//div[contains(text(), 'Severity')])[1]")
    button_archived_alerts = (By.XPATH, "//span[contains(text(),'Archived Alerts')]")

    table_list_event_type = "(//div[@class='uwf-grid__main_table'])[1]//section/div[1]"
    table_list_event_unique = "(//div[@class='uwf-grid__main_table'])[1]//section/div[1]"
    table_list_last_occurrence = "(//div[@class='uwf-grid__main_table'])[1]//section/div[1]"
    table_list_occurrence_time = "(//div[@class='uwf-grid__main_table'])[1]//section/div[1]"
    table_list_severity = "(//div[@class='uwf-grid__main_table'])[1]//section/div[1]"

    checkbox_select_all = (By.XPATH, "(//div[@class='uwf-checkbox uwf-checkbox_light'])[1]")
    status_archived_alerts = "//div[@class='uwf-button-group-radio']/div[2]/div/../self::div[contains(@class,'selected')]"

    text_no_elements_found = "//div[text()=' No alerts found ']"
    text_total = (By.XPATH, "(//div[@class='uwf-grid__header_selection_label'])[1]")
    list_total = "(//div[@class='uwf-grid__main_table'])[1]//section"
    list_checkbox_selected = "//section[contains(@class,'selected')]"
    trial = "(//div[@class='uwf-grid__main_table'])[2]//section/div[1]"

    is_empty = "//div[contains(@class,'empty')]"
    is_wait = "//div[contains(@class,'unselectable clickable')]"
    URL = "alerts"


    def __init__(self, driver):
        super().__init__(driver)

    def open_alerts(self):
        self.do_click(self.button_manage)
        self.do_click(self.button_alerts)
        time.sleep(2)


    def get_alerts_count(self):
        return self.get_total_count(self.text_total)

    def get_alerts_list_length(self):
        return self.list_length(self.list_total)
        # return self.list_length(self.trial)

    def get_list_elements(self):
        lis = []
        lis = self.store_to_list(self.list_total)
        for i in lis:
            print(i)

    def wait_till_page_load(self):
        self.check_page_loaded(self.is_wait)

    def select_all(self):
        self.do_click(self.checkbox_select_all)
        result = self.list_length(self.list_checkbox_selected) == self.get_alerts_list_length()
        self.do_click(self.checkbox_select_all)
        return result

    def sortby_event_desc(self):
        return self.column_sort_desc(self.button_event_type, self.table_list_event_type)

    def sortby_event_asc(self):
        return self.column_sort_desc(self.button_event_type, self.table_list_event_type)

    def sortby_event_unique_desc(self):
        return self.column_sort_desc(self.button_event_unique_id, self.table_list_event_unique)

    def sortby_event_unique_asc(self):
        return self.column_sort_desc(self.button_event_unique_id, self.table_list_event_unique)

    def sortby_last_occurrence_desc(self):
        return self.column_sort_desc(self.button_last_occurrence, self.table_list_last_occurrence)

    def sortby_last_occurrence_asc(self):
        return self.column_sort_desc(self.button_last_occurrence, self.table_list_last_occurrence)

    def sortby_first_occurrence_desc(self):
        return self.column_sort_desc(self.button_first_occurrence_time, self.table_list_occurrence_time)

    def sortby_first_occurrence_asc(self):
        return self.column_sort_desc(self.button_first_occurrence_time, self.table_list_occurrence_time)

    def sortby_severity_desc(self):
        return self.column_sort_desc(self.button_severity, self.table_list_severity)

    def sortby_severity_asc(self):
        return self.column_sort_desc(self.button_severity, self.table_list_severity)

    def no_alerts_found(self):
        return self.check_exists_by_xpath(self.text_no_elements_found)

    def button_click_archived_alert(self):
        self.do_click(self.button_archived_alerts)
        if self.check_exists_by_xpath(self.status_archived_alerts):
            return True
        else:
            return False
