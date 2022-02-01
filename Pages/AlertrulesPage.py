import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AlertRulesPage(BasePage):

    button_manage = (By.XPATH, "//div[contains(text(),'Manage')]")
    button_alert_rules = (By.XPATH, "//div[contains(text(),'Alert Rules')]")
    button_notification = (By.XPATH, "//div[text()='Notification Off']/../self::div[@class='uwf-toggle-button__text']")
    button_warning = (By.XPATH, "//div[text()='Warning']/../self::div[@class='uwf-toggle-button__text']")
    button_error = (By.XPATH, "//div[text()='Error']/../self::div[@class='uwf-toggle-button__text']")
    button_critical = (By.XPATH, "//div[text()='Critical']/../self::div[@class='uwf-toggle-button__text']")
    button_emergency = (By.XPATH, "//div[text()='Emergency']/../self::div[@class='uwf-toggle-button__text']")
    button_policy = (By.XPATH, "//div[text()='Policy Engine Off']/../self::div[@class='uwf-toggle-button__text']")
    button_email = (By.XPATH, "//div[text()='Email Notification Off']/../self::div[@class='uwf-toggle-button__text']")
    button_event_type = (By.XPATH, "//div[contains(text(), 'Event Type')]/..")
    button_status = (By.XPATH, "//div[contains(text(), 'Status')]/..")
    button_notification_disable = "//div[text()='Warning']/../../self::div[contains(@class,'disabled')]"
    button_to = (By.XPATH, "(//div[contains(text(), 'To')])[1]")
    button_sfa = (By.XPATH, "(//div[contains(text(), 'SFA')])[1]")
    button_es = (By.XPATH, "(//div[contains(text(), 'ES')])[1]")
    button_insight = (By.XPATH, "(//div[contains(text(), 'Insight')])[1]")
    button_event_type_list = "//div[@class='event-type-template-wrapper ng-star-inserted']"
    button_add_custom_policy = (By.XPATH, "//div[contains(text(),'Add Custom Policy')]")
    button_add_recipient = (By.XPATH, "//div[contains(text(),'Add Recipient')]")
    button_cancel = (By.XPATH, "//button[text()='Cancel']")
    model_custom_policy = (By.XPATH, "//div[@class='uwf-modal']")

    checkbox_policy_select_all = (By.XPATH, "(//div[@class='uwf-checkbox uwf-checkbox_light'])[1]")
    checkbox_recipient_select_all = (By.XPATH, "(//div[@class='uwf-grid__header_selection_label'])[2]/../uwf-checkbox")
    list_checkbox_selected = "//section[contains(@class,'selected')]"

    status_button_notification = "//div[text()='Notification Off']/../../self::div[contains(@class,'checked')]"
    status_button_warning = "//div[text()='Warning']/../../self::div[contains(@class,'checked')]"
    status_button_error = "//div[text()='Error']/../../self::div[contains(@class,'checked')]"
    status_button_critical = "//div[text()='Critical']/../../self::div[contains(@class,'checked')]"
    status_button_emergency = "//div[text()='Emergency']/../../self::div[contains(@class,'checked')]"
    status_button_policy = "//div[text()='Policy Engine Off']/../../self::div[contains(@class,'checked')]"
    status_button_email = "//div[text()='Email Notification Off']/../../self::div[contains(@class,'checked')]"
    status_question_hover = "//div[contains(@class,'uwf-help-trigger_tippy-visible')]"

    policies_list_total = "(//div[@class='uwf-grid__main_table'])[1]//section"
    policies_text_total = (By.XPATH, "(//div[@class='uwf-grid__header_selection_label'])[1]")
    recipients_list_total = "(//div[@class='uwf-grid__main_table'])[2]//section"
    recipients_text_total = (By.XPATH, "(//div[@class='uwf-grid__header_selection_label'])[2]")


    table_list_event = "(//div[@class='uwf-grid__main_table'])[1]//section"
    table_list_recipient = "(//div[@class='uwf-grid__main_table'])[2]//section"
    table_list_to = "(//div[@class='uwf-grid__main_table'])[2]//section/div[1]"
    table_list_ES = "(//div[@class='uwf-grid__main_table'])[2]//section/div[2]"
    table_list_SFA = "(//div[@class='uwf-grid__main_table'])[2]//section/div[3]"
    table_list_insight = "(//div[@class='uwf-grid__main_table'])[2]//section/div[4]"

    is_empty = "//div[contains(@class,'empty')]"
    is_wait = "//div[contains(@class,'unselectable clickable')]"
    # button_to_list = "//div[@class='uwf-grid__main_table_content_row_cell_content-value uwf-flex-grow']/../../../../div[1]/div"

    trial = "(//div[@class='uwf-grid__main_table'])[1]//section/div[3]"
    button_status_each = (By.XPATH, "((//div[@class='uwf-grid__main_table'])[1]//section/div[3]/div/div[2]/uwf-toggle-button)[1]")
    button_status_check = "((//div[@class='uwf-grid__main_table'])[1]//section/div[3]/div/div[2]/uwf-toggle-button)[1]/div[contains(@class,'checked')]"
    status_change_yes = (By.XPATH, "//button[contains(text(),'Yes')]" )
    # status_button = "((//div[@class='uwf-grid__main_table'])[1]//section/div[3]/div/div[2])[1]/uwf-toggle-button"
    # question = "(//div[@class='uwf-help-trigger type-gray'])[1]"
    # is it hovered //div[contains(@class,'uwf-help-trigger_tippy-visible')]
    URL = "alert-rules"

    def __init__(self, driver):
        super().__init__(driver)

    def open_alert_rules(self):
        self.do_click(self.button_manage)
        self.do_click(self.button_alert_rules)

    def verify_its_that_page(self):
        self.driver.implicitly_wait(10)
        ele = self.driver.find_elements(By.XPATH, "//div[@class='uwf-grid__main']")
        return len(ele)

    def status_of_button(self):
        print("Notification : %r" %(self.check_exists_by_xpath(self.status_button_notification)))
        print("Warning : %r" % (self.check_exists_by_xpath(self.status_button_warning)))
        print("Error : %r" % (self.check_exists_by_xpath(self.status_button_error)))
        print("Critical : %r" % (self.check_exists_by_xpath(self.status_button_critical)))
        print("Emergency : %r" % (self.check_exists_by_xpath(self.status_button_emergency)))
        print("Policy : %r" % (self.check_exists_by_xpath(self.status_button_policy)))
        print("Email : %r" % (self.check_exists_by_xpath(self.status_button_email)))

    def button_click_notification(self):
        flag = self.check_exists_by_xpath(self.status_button_notification)
        self.do_click(self.button_notification)
        flag2 = self.check_exists_by_xpath(self.status_button_notification)
        self.do_click(self.button_notification)
        if flag != flag2:
            return True
        else:
            return False

    def button_click_warning(self):
        if(self.check_exists_by_xpath(self.status_button_notification) == False):
            print("Notification is in Off state")
            return False
        flag = self.check_exists_by_xpath(self.status_button_warning)
        self.do_click(self.button_warning)
        flag2 = self.check_exists_by_xpath(self.status_button_warning)
        self.do_click(self.button_warning)
        if flag != flag2:
            return True
        else:
            return False

    def button_click_error(self):
        if (self.check_exists_by_xpath(self.status_button_notification) == False):
            print("Notification is in Off state")
            return False
        flag = self.check_exists_by_xpath(self.status_button_error)
        self.do_click(self.button_error)
        flag2 = self.check_exists_by_xpath(self.status_button_error)
        self.do_click(self.button_error)
        if flag != flag2:
            return True
        else:
            return False

    def button_click_critical(self):
        if not self.check_exists_by_xpath(self.status_button_notification):
            print("Notification is in Off state")
            return False
        flag = self.check_exists_by_xpath(self.status_button_critical)
        self.do_click(self.button_critical)
        flag2 = self.check_exists_by_xpath(self.status_button_critical)
        self.do_click(self.button_critical)
        if flag != flag2:
            return True
        else:
            return False

    def button_click_emergency(self):
        if (self.check_exists_by_xpath(self.status_button_notification) == False):
            print("Notification is in Off state")
            return False
        flag = self.check_exists_by_xpath(self.status_button_emergency)
        self.do_click(self.button_emergency)
        flag2 = self.check_exists_by_xpath(self.status_button_emergency)
        self.do_click(self.button_emergency)
        if flag != flag2:
            return True
        else:
            return False

    def button_click_policy(self):
        flag = self.check_exists_by_xpath(self.status_button_policy)
        self.do_click(self.button_policy)
        flag2 = self.check_exists_by_xpath(self.status_button_policy)
        self.do_click(self.button_policy)
        if flag != flag2:
            return True
        else:
            return False

    def button_click_email(self):
        flag = self.check_exists_by_xpath(self.status_button_email)
        self.do_click(self.button_email)
        flag2 = self.check_exists_by_xpath(self.status_button_email)
        self.do_click(self.button_email)
        if flag != flag2:
            return True
        else:
            return False

    def button_click_custom_policy(self):
        self.do_click(self.button_add_custom_policy)
        result = self.is_visible(self.model_custom_policy)
        self.do_click(self.button_cancel)
        return result

    def button_click_add_recipient(self):
        self.do_click(self.button_add_recipient)
        result = self.is_visible(self.model_custom_policy)
        self.do_click(self.button_cancel)
        return result

    def button_notification_off_disable_all(self):
        var = self.check_exists_by_xpath(self.status_button_notification)
        if var == True:
            self.do_click(self.button_notification)
        return self.check_exists_by_xpath(self.button_notification_disable) # It will return true when the remaining notification buttons are disabled
    '''
    def sortby_event_desc(self):
        ele = self.store_elements_list(self.button_event_type_list)
        self.do_click(self.button_event_type)
        ele.sort(reverse=True)
        ele1 = self.store_elements_list(self.button_event_type_list)
        return ele[0] == ele1[0]

    def sortby_event_asc(self):
        ele = self.store_elements_list(self.button_event_type_list)
        ele.sort()
        self.do_click(self.button_event_type)
        self.do_click(self.button_event_type)
        ele1 = self.store_elements_list(self.button_event_type_list)
        return ele[0] == ele1[0]
    '''

    def sortby_event_desc(self):
        lis = []
        lis1 = []
        lis = self.get_row_list(self.table_list_event)
        lis.sort(key=lambda x: x[0], reverse=True)
        self.do_click(self.button_event_type)
        lis1 = self.get_row_list(self.table_list_event)
        for i in range(len(lis)):
                if lis[i] != lis1[i]:
                    return False
                else:
                    continue
        return True

    def sortby_event_asc(self):
        lis = []
        lis1 = []
        lis = self.get_row_list(self.table_list_event)
        lis.sort(key=lambda x: x[0], reverse=False)
        self.do_click(self.button_event_type)
        self.do_click(self.button_event_type)
        lis1 = self.get_row_list(self.table_list_event)
        for i in range(len(lis)):
                if(lis[i] != lis1[i]):
                    return False
                else:
                    continue
        return True


    def sortby_status_desc(self):
        lis = []
        lis1= []
        lis = self.get_row_list(self.table_list_event)
        lis.sort(key=lambda x: x[2], reverse=True)
        self.do_click(self.button_status)
        lis1 = self.get_row_list(self.table_list_event)
        for i in range(len(lis)):
            if(lis[i] != lis1[i]):
                return False
            else:
                continue
        return True


    def sortby_status_asc(self):
        lis = []
        lis1= []
        lis = self.get_row_list(self.table_list_event)
        lis.sort(key=lambda x: x[2], reverse=False)
        self.do_click(self.button_status)
        self.do_click(self.button_status)
        lis1 = self.get_row_list(self.table_list_event)
        for i in range(len(lis)):
            if(lis[i] != lis1[i]):
                return False
            else:
                continue
        return True

    def hover_help_button(self):
        a = ActionChains(self.driver)
        self.driver.implicitly_wait(10)
        len = self.list_length(self.table_list_event)
        time.sleep(3)
        for i in range(1, len):
            #m = self.driver.find_element(By.XPATH, ("(//div[@class='uwf-help-trigger type-gray'])[%d]" % i))
            self.driver.find_element(By.XPATH, ("(//div[@class='uwf-help-trigger type-gray'])[%d]" % i)).click()
            time.sleep(3)
            #a.move_to_element(m).perform()
            print(i)
            print(self.check_exists_by_xpath(self.status_question_hover))
            #print(self.driver.find_element(By.XPATH, self.status_question_hover).is_displayed())

    def get_policies_length(self):
        return self.list_length(self.policies_list_total)

    def get_policies_count(self):
        return self.get_total_count(self.policies_text_total)

    def get_recipients_length(self):
        return self.list_length(self.recipients_list_total)

    def get_recipients_count(self):
        return self.get_total_count(self.recipients_text_total)

    def wait_till_page_load(self):
        self.check_page_loaded(self.is_wait)

    def select_all_policy(self):
        self.do_click(self.checkbox_policy_select_all)
        result = self.list_length(self.list_checkbox_selected) == self.get_policies_length()
        self.do_click(self.checkbox_policy_select_all)
        return result

    def select_all_recipients(self):
        self.do_click(self.checkbox_recipient_select_all)
        result = self.list_length(self.list_checkbox_selected) == self.get_recipients_length()
        self.do_click(self.checkbox_recipient_select_all)
        return result

    def status_button_click (self):
        len = self.get_policies_length()
        self.driver.implicitly_wait(5)
        for i in range(1,len+1):
            press = (By.XPATH, "((//div[@class='uwf-grid__main_table'])[1]//section/div[3]/div/div[2]/uwf-toggle-button)[%d]" % i)
            check = ("((//div[@class='uwf-grid__main_table'])[1]//section/div[3]/div/div[2]/uwf-toggle-button)[%d]/div[contains(@class,'checked')]" % i)

            status_before = ""
            status_after = ""
            if self.check_exists_by_xpath(check):
                status_before = True
            else:
                status_before = False
            self.do_click(press)
            self.do_click(self.status_change_yes)
            #print(status_before)
            time.sleep(2)
            if self.check_exists_by_xpath(check):
                status_after = True
            else:
                status_after = False
            #print(status_after)
            self.do_click(press)
            self.do_click(self.status_change_yes)
            '''
            if status_before != status_after:
                print(True)
            else:
                print(False)
            '''
            if status_before == status_after:
                return False
            time.sleep(3)

        return True

    def sortby_to_desc(self):
        return self.column_sort_desc(self.button_to, self.table_list_to)

    def sortby_to_asc(self):
        return self.column_sort_asc(self.button_to, self.table_list_to)

    def sortby_es_desc(self):
        return self.column_sort_desc(self.button_es, self.table_list_ES)

    def sortby_es_asc(self):
        return self.column_sort_asc(self.button_es, self.table_list_ES)

    def sortby_sfa_desc(self):
        return self.column_sort_desc(self.button_sfa, self.table_list_SFA)

    def sortby_sfa_asc(self):
        return self.column_sort_asc(self.button_sfa, self.table_list_SFA)

    def sortby_insight_desc(self):
        return self.column_sort_desc(self.button_insight, self.table_list_insight)

    def sortby_insight_asc(self):
        return self.column_sort_asc(self.button_insight, self.table_list_insight)

    def button_add_recipient_es(self):
        return
