import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class CallHomePage(BasePage):

    MANAGE = (By.XPATH, "//div[contains(text(),'Manage')]")
    SETTINGS = (By.XPATH, "//*[name()='use' and @*='#settings']")
    #ADMIN = (By.XPATH, "//div[contains(text(),'admin')]")
    #LOGOUT = (By.XPATH, "//div[contains(text(),'Logout')]")
    CALLHOME = (By.XPATH, "//div[contains(text(),'Call Home')]")
    CASENO = (By.XPATH, "//div[contains(text(),'Case No')]")
    TICKETID = (By.XPATH, "//div[contains(text(),'Ticket ID')]")
    SUBJECT = (By.XPATH, "//div[contains(text(),'Subject')]")
    CREATED_ON = (By.XPATH, "//div[contains(text(),'Created On')]")
    STATUS = (By.XPATH, "//div[contains(text(),'Status')]")
    GET_COUNT = (By.XPATH, "//div[contains(text(),'total') and @class='uwf-grid__header_selection_label']")
    #CALLHOME_BUTTON = (By.XPATH, "//div[contains(text(),'Call Home Disabled')]")
    CALLHOME_Button_noti = (By.XPATH, "//div[text()='Call Home Disabled']/../self::div[@class='uwf-toggle-button__text']")
    CALLHOME_BUTTON = "//div[text()='Call Home Disabled']/../../self::div[contains(@class,'checked')]"
    CALLHOME_CONFIGURE_BTN = (By.XPATH, "//div[contains(text(),'Configure')]")
    CALLHOME_SELF_SERVICE_USERNAME = (By.ID, "ssuser")
    CALLHOME_SELF_SERVICE_PASSWORD = (By.ID, "sspass")
    CALLHOME_SELF_SERVICE_TEST_BTN = (By.XPATH, "//button[contains(text(),'Test')]")
    CALLHOME_SELF_SERVICE_CANCEL_BTN = (By.XPATH, "//button[contains(text(),'Cancel')]")
    CALLHOME_ERROR_MSG1 = (By.XPATH, "//div[contains(text(),'Error occured while connecting to Salesforce')]")
    CALLHOME_ERROR_MSG2 = (By.XPATH, "//div[@class='uwf-modal__bottom-line-container']")
    CALLHOME_CONFIGURE_SAVE_BTN = (By.XPATH, "//button[contains(text(),'Save')]")
    COUNT= []
    CALLHOME_SELECTALL_CHECKBOX_BTN = (By.XPATH, "//div[@class='uwf-checkbox uwf-checkbox_light']")
    tot_rows = "(//div[@class='uwf-grid__main_table'])[1]//section"
    Close_Mark = (By.XPATH, "//button[@class='uwf-dialog-box__close uwf-btn uwf-btn_icon ng-star-inserted']")
    URL = "call-home"
    call_home_status = (By.XPATH, "//div[@class='uwf-grid__no-data-container ng-star-inserted']")
    case_no_column_wise_data = "(//div[@class='uwf-grid__main_table'])[1]//section/div[1]"
    created_on_column_wise_data = "(//div[@class='uwf-grid__main_table'])[1]//section/div[4]"

    #COUNT = (By.XPATH, "(//div[@class='uwf-grid__main_table'])[1]//section")
    #CALL_HOME_ROWS = (By.XPATH, "(//div[@class='uwf-grid__main_table'])[1]//section")

    def __init__(self, driver):
        super().__init__(driver)

    def get_homepage_title(self, title):
        return self.get_title(title)

    def do_callhome_button_click(self):
        #if self.is_visible(self.CALLHOME_BUTTON):
        flag = self.check_exists_by_xpath(self.CALLHOME_BUTTON)
        self.do_click(self.CALLHOME_Button_noti)
        flag2 = self.check_exists_by_xpath(self.CALLHOME_BUTTON)
        if flag != flag2:
            return True
        else:
            return False

    def do_manage_click(self):
        return self.do_click(self.MANAGE)

    def go_to_callhome(self):
        if self.is_visible((self.MANAGE)):
            self.do_click(self.MANAGE)
            if self.is_visible(self.CALLHOME):
                self.do_click(self.CALLHOME)

    def do_check_callhome_stat(self):
        flag = True
        res = ""
        if self.is_visible(self.call_home_status):
            res = self.get_element_text(self.call_home_status)
        res = res.upper()
        if "ENABLE CALL HOME" in res:
            self.do_callhome_button_click()
            self.do_check_callhome_stat()
        if "NO TICKET" in res:
            flag = False
        return flag



    def sort_by_caseno(self):
        if self.is_visible(self.CASENO):
            return True
        else:
            return False
        #self.do_click(self.CASENO)

    def sort_by_TicketID(self):
        if self.is_visible(self.TICKETID):
            return True
        else:
            return False
        #self.do_click(self.TICKETID)

    def sort_by_Subject(self):
        if self.is_visible(self.SUBJECT):
            return True
        else:
            return False
        #self.do_click(self.SUBJECT)

    def sort_by_CreatedOn(self):
        if self.is_visible(self.CREATED_ON):
            return True
        else:
            return False
        #self.do_click(self.CREATED_ON)

    def sort_by_Status(self):
        if self.is_visible(self.STATUS):
            return True
        else:
            return False
        #self.do_click(self.STATUS)

    def sort_by_caseno_desc(self):
        return self.column_sort_desc(self.CASENO, self.case_no_column_wise_data)

    def sort_by_caseno_asc(self):
        return self.column_sort_asc(self.CASENO, self.case_no_column_wise_data)

    def sort_by_TicId_desc(self):
        return self.column_sort_desc(self.TICKETID, self.case_no_column_wise_data)

    def sort_by_TicId_asc(self):
        return self.column_sort_asc(self.TICKETID, self.case_no_column_wise_data)

    def sort_by_sub_desc(self):
        return self.column_sort_desc(self.SUBJECT, self.case_no_column_wise_data)

    def sort_by_sub_asc(self):
        return self.column_sort_asc(self.SUBJECT, self.case_no_column_wise_data)

    def sort_by_created_on_desc(self):
        return self.column_sort_desc(self.CREATED_ON, self.created_on_column_wise_data)

    def sort_by_created_on_asc(self):
        return self.column_sort_asc(self.CREATED_ON, self.created_on_column_wise_data)

    def sort_by_status_desc(self):
        return self.column_sort_desc(self.STATUS, self.case_no_column_wise_data)

    def sort_by_status_asc(self):
        return self.column_sort_asc(self.STATUS, self.case_no_column_wise_data)

    def total_cases(self):
        time.sleep(2)
        return self.get_total_count(self.GET_COUNT)
        #return self.get_element_text(self.GET_COUNT)

    def get_callhome_list_length(self):
        return self.list_length(self.tot_rows)
        #return self.list_length(self.list_total)

    def configure_home(self, username, password):
        user=""
        pswd=""
        self.do_click(self.CALLHOME_CONFIGURE_BTN)
        time.sleep(4)
        if self.is_visible(self.CALLHOME_SELF_SERVICE_USERNAME):
            time.sleep(4)
            self.do_clear(self.CALLHOME_SELF_SERVICE_USERNAME)
            time.sleep(4)
            self.do_send_keys(self.CALLHOME_SELF_SERVICE_USERNAME, username)
            #user = self.get_element_text(self.CALLHOME_SELF_SERVICE_USERNAME)
        if self.is_visible(self.CALLHOME_SELF_SERVICE_PASSWORD):
            time.sleep(4)
            self.do_clear(self.CALLHOME_SELF_SERVICE_PASSWORD)
            time.sleep(4)
            self.do_send_keys(self.CALLHOME_SELF_SERVICE_PASSWORD, password)
            #pswd = self.get_element_text(self.CALLHOME_SELF_SERVICE_PASSWORD)
        time.sleep(4)
        self.do_click(self.CALLHOME_SELF_SERVICE_TEST_BTN)
        time.sleep(2)
        return self.get_element_text(self.CALLHOME_ERROR_MSG2)

    def configure_home_Cancel_btn(self):
        self.do_click(self.CALLHOME_CONFIGURE_BTN)
        time.sleep(2)
        self.do_click(self.CALLHOME_SELF_SERVICE_CANCEL_BTN)

    def configure_home_Save_btn(self):
        self.do_click(self.CALLHOME_CONFIGURE_SAVE_BTN)

    def get_total_row_count(self, locator):
        return self.get_element_text(locator)

    def get_cur_url(self):
        return self.driver.current_url

    def click_selectall_checkbox(self):
        time.sleep(2)
        self.do_click(self.CALLHOME_SELECTALL_CHECKBOX_BTN)
        time.sleep(2)

    def cancel_del_using_xmark(self):
        time.sleep(2)