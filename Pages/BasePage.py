import copy

from Utilities import Logger
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Pages.LoginPage

"""Parent of all pages contains methods and utilities for all the pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(by_locator))
        return element.text

    def get_total_count(self, by_locator):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(by_locator))
        # time.sleep(5)
        ele = self.get_element_text(by_locator)
        ele = ele.split()
        count = int(ele[0])
        return count

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def do_clear(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.implicitly_wait(1.5)
            self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def store_elements_list(self, by_locator):
        ele = []
        lis = []
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, by_locator)))
        ele = self.driver.find_elements(By.XPATH, by_locator)
        for i in range(len(ele)):
            if (i % 2 == 0):
                lis.append(ele[i].text.upper())
        return lis

    def store_to_list(self, by_locator):
        ele = []
        lis = []
        # WebDriverWait(self.driver, 15).until(EC.visibility_of_all_elements_located((By.XPATH, by_locator)))
        self.driver.implicitly_wait(15)
        ele = self.driver.find_elements(By.XPATH, by_locator)

        for i in ele:
            lis.append(i.text)
        return lis

    def list_length(self, by_locator):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, by_locator)))
        ele = []
        ele = self.driver.find_elements(By.XPATH, by_locator)
        return len(ele)

    def store_to_list_trial(self, by_locator):
        ele = []
        lis = []
        # WebDriverWait(self.driver, 15).until(EC.visibility_of_all_elements_located((By.XPATH, by_locator)))
        self.driver.implicitly_wait(15)
        time.sleep(5)
        ele = self.driver.find_elements(By.XPATH, by_locator)

        for i in ele:
            lis.append(i.text.split("\n", 2))
        # lis.sort(key=lambda x: x[0], reverse=True)
        return lis

    def get_row_list(self, by_locator):
        ele = []
        lis = []
        self.driver.implicitly_wait(15)
        time.sleep(5)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_all_elements_located((By.XPATH, by_locator)))
        ele = self.driver.find_elements(By.XPATH, by_locator)
        for i in ele:
            lis.append(i.text.upper().split("\n", 2))
        # lis.sort(key=lambda x: x[0], reverse=True)
        return lis

    def get_list_column(self, by_locator):
        lis = []
        ele = []
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, by_locator)))
        ele = self.driver.find_elements(By.XPATH, by_locator)
        for i in ele:
            lis.append(i.text.upper())
        lis = list(filter(None, lis))
        return lis

    def check_page_loaded(self, by_locator):
        flag = True
        while flag:
            time.sleep(3)
            check = self.check_exists_by_xpath(by_locator)
            if check == True:
                flag = False
            else:
                continue
        return True

    def column_sort_desc(self, loc_button, loc_table_list):
        self.do_click(loc_button)
        time.sleep(1)
        lis1 = self.get_list_column(loc_table_list)
        lis2 = lis1
        lis2.sort(reverse=True)
        if lis1 == lis2:
            return True
        else:
            return False

    def column_sort_asc(self, loc_button, loc_table_list):
        time.sleep(2)
        self.do_click(loc_button)
        time.sleep(2)
        self.do_click(loc_button)
        time.sleep(2)
        lis1 = self.get_list_column(loc_table_list)
        lis2 = lis1
        lis2.sort(reverse=True)
        if lis1 == lis2:
            return True
        else:
            return False

    # basheer
    def checkEmptyInputFields(self, locator):
        if len(locator.text) == 0:
            return True
        return False

    def checkActiveButton(self, locator):
        if locator.is_enabled():
            return True
        return False

    def waitForElement(self, locator):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(locator))
        return element

    def waitForElements(self, locator):
        elements = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(locator))
        return elements

    def currentUrl(self):
        return self.driver.current_url

    def urlPresent(self, url):
        return url in self.currentUrl()

    def isElementVisible(self, element):
        return element.is_displayed()

    def isAttrInAllElements(self, toFind, attribute, element):
        res = True
        for ele in element:
            if not toFind in ele.get_attribute(attribute):
                res = False
                break
        return res

    def isAttrInElement(self, toFind, attribute, element):
        if toFind in element.get_attribute(attribute):
            return True
        return False

    def getTableData(self, tableColumns, map, rows):
        map.clear()
        for ele in tableColumns:
            map[ele] = []

        for i in range(len(rows)):
            self.scrollToElement(rows[i])
            val = rows[i].text.replace("\n", ":")
            val = val.split(":")
            for j in range(len(map)):
                key = tableColumns[j]
                ele = val[j]
                map[key].append(ele)

    def updateTableRow(self, map, newVal, key, idx):
        values = map[key]
        values[idx] = newVal

    def labelTextUnselected(self, te):
        text = (str(te) + " total")
        return text

    def labelTextAllSelected(self, te):
        text = (str(te) + "  of " + str(te) + " total")
        return text

    def labelTextNSelected(self, n, te):
        text = (str(n) + "  of " + str(te) + " total")
        return text

    def getIthRowsData(self, table, i):
        listItem = []
        for keys in table.keys():
            val = table[keys]
            listItem.append(val[i])
        return listItem

    def getIthRowFromTable(self, row):
        val = row.text.replace("\n", ":")
        val = val.split(":")
        return val

    def getIthColData(self, table, i):
        idx = 0
        for keys in table.keys():
            val = table[keys]
            if idx == i:
                return val
            idx = idx + 1
        return []

    def getText(self, locator):
        cmd = "return document.getElementById('" + locator + "').value;"
        return self.driver.execute_script(cmd)

    def addInTable(self, table, keys, newValues):
        for i in range(len(keys)):
            key = keys[i]
            val = table[key]
            val.append(newValues[i])

    def changeUserName(self, table, tableColumns, restore=False):
        key = tableColumns[0]
        value = table[key]
        newVal = []
        if not restore:
            for ele in value:
                if str.startswith(ele, "_"):
                    txt = ele.replace("_", "!")
                    newVal.append(txt)
                else:
                    newVal.append(ele)
        else:
            for ele in value:
                if str.startswith(ele, "!"):
                    txt = ele.replace("!", "_")
                    newVal.append(txt)
                else:
                    newVal.append(ele)
        table[key] = newVal

    def CaseMatch(self, rows, idx):
        for i in range(1, len(rows)):
            rowPrev = rows[i - 1]
            rowCurr = rows[i]
            if str.upper(rowPrev[idx]) == str.upper(rowCurr[idx]):
                temp = rowPrev
                rows[i - 1] = rowCurr
                rows[i] = temp

    def sortTable(self, table, idx, isRev, n, tableColumns):
        oldTable = []
        if idx == 0:
            self.changeUserName(table, tableColumns)

        for i in range(n):
            temp = []
            for keys in table:
                temp.append(table[keys][i])
            oldTable.append(temp)

        sortedRows = sorted(oldTable, key=lambda li: str.upper(
            li[idx]), reverse=(isRev == 1))
        if idx == 0 or isRev == 1:
            self.CaseMatch(sortedRows, idx)
        for keys in table:
            table[keys] = []
        for i in range(n):
            j = 0
            for keys in table:
                table[keys].append(sortedRows[i][j])
                j = j + 1
        if idx == 0:
            self.changeUserName(table, tableColumns, True)

    def isElementPresent(self, css=''):
        try:
            if css == '':
                css = ".cdk-overlay-pane.uwf-dialog-panel"

            element = self.driver.find_element(By.CSS_SELECTOR, css)
            return True
        except NoSuchElementException as e:
            return False

    def isElementsPresent(self, css=''):
        try:
            if css == '':
                css = ".cdk-overlay-pane.uwf-dialog-panel"

            elements = self.driver.find_elements(By.CSS_SELECTOR, css)
            return elements
        except NoSuchElementException as e:
            return []

    def scrollToElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def selectAllCheckBox(self, manageUsers):
        selectAllcb = manageUsers.getSelectAll()
        selectAllcb.click()
        Logger.info("clicked on selectAll CheckBox")

    # changed
    def selectOne(self, manageUsers, index):
        checkbox = self.getAllRowCheckBox(manageUsers)
        selectedCheckBox = checkbox[index]
        self.scrollToElement(selectedCheckBox)
        Logger.info(f"getting checkBox {index} and click")
        selectedCheckBox.click()
        Logger.info("checkbox clicked")

    def getAllRowCheckBox(self, manageUsers):
        checkboxes = manageUsers.getTableCheckbox()
        Logger.info("getting all checkboxes of all rows of table")
        return checkboxes

    # changed
    def getOneRowCheckBox(self, manageUsers, index):
        checkBoxes = self.getAllRowCheckBox(manageUsers)
        Logger.info(f"getting checkbox of {index}th index row")
        self.scrollToElement(checkBoxes[index])
        return checkBoxes[index]

    def getAllTableRows(self, manageUsers):
        Logger.info("getting all rows")
        rows = manageUsers.getAllRows()
        return rows

    # changed
    def getTableOneRow(self, manageUsers, index):
        Logger.info(f"getting row : {index}")
        rows = manageUsers.getAllRows()
        self.scrollToElement(rows[index])
        return rows[index]

    def getLoginUserIndex(self, manageUsers, tableDataMap):
        userNameList = self.getIthColData(tableDataMap, 0)
        index = 0
        loginUser = manageUsers.getLoggedInUser()
        for ele in userNameList:
            if ele == loginUser:
                break
            index = index + 1
        Logger.info(f"Found login User row no: {index}")
        return index

    def UserIndex(self, tableDataMap, username):
        userNameList = self.getIthColData(tableDataMap, 0)
        index = 0
        for ele in userNameList:
            if ele == username:
                Logger.info(f"Found User row no: {index}")
                return index
            index = index + 1
        Logger.info("USER NOT FOUND")
        return -1

    def clickAddUserBtn(self, manageUsers):
        btn = manageUsers.getAddUser()
        Logger.info("clicking addUser button")
        btn.click()

    def checkColumnSorted(self, manageUsers):
        ans = []
        # 0 inc,  1 dec
        Logger.info("Getting all table columns headings for sorting check")
        userName = manageUsers.UserNameClick()
        firstName = manageUsers.FirstNameClick()
        lastName = manageUsers.LastNameClick()
        email = manageUsers.EmailClick()
        role = manageUsers.RoleNameClick()
        if self.isAttrInElement("sorted", "class", userName):
            arrow = manageUsers.getSortedArrow(userName)
            ans.append(0)
            if self.isAttrInElement("asc", "class", arrow):
                Logger.info("USERNAME Column is Sorted in increasing order")
                ans.append(0)
            else:
                ans.append(1)
                Logger.info("USERNAME Column is Sorted in decreasing order")

        elif self.isAttrInElement("sorted", "class", firstName):
            ans.append(1)
            arrow = manageUsers.getSortedArrow(firstName)
            if self.isAttrInElement("asc", "class", arrow):
                Logger.info("FIRSTNAME Column is Sorted in increasing order")
                ans.append(0)
            else:
                ans.append(1)
                Logger.info("FIRSTNAME Column is Sorted in decreasing order")

        elif self.isAttrInElement("sorted", "class", lastName):
            ans.append(2)
            arrow = manageUsers.getSortedArrow(lastName)
            if self.isAttrInElement("asc", "class", arrow):
                Logger.info("LASTNAME Column is Sorted in increasing order")
                ans.append(0)
            else:
                ans.append(1)
                Logger.info("LASTNAME Column is Sorted in decreasing order")

        elif self.isAttrInElement("sorted", "class", email):
            ans.append(3)
            arrow = manageUsers.getSortedArrow(email)
            if self.isAttrInElement("asc", "class", arrow):
                Logger.info("EMAIL Column is Sorted in increasing order")
                ans.append(0)
            else:
                ans.append(1)
                Logger.info("EMAIL Column is Sorted in decreasing order")
        elif self.isAttrInElement("sorted", "class", role):
            ans.append(4)
            arrow = manageUsers.getSortedArrow(role)
            if self.isAttrInElement("asc", "class", arrow):
                Logger.info("ROLE Column is Sorted in increasing order")
                ans.append(0)
            else:
                ans.append(1)
                Logger.info("ROLE Column is Sorted in decreasing order")
        else:
            Logger.info("NO Column is Sorted")
        Logger.info(f"sorting status: {ans}")
        return ans

    def sortClick(self, manageUsers, tableDataMap, tableColumns, idx, isRev, element, n):
        Logger.info("Sort TableData according to type: " + str(isRev))
        self.sortTable(tableDataMap, idx, isRev, n, tableColumns)
        sortedTable = copy.deepcopy(tableDataMap)
        Logger.info(str(idx) + "th Column Clicked")
        element.click()
        Logger.info("getting all rows data after sorting")
        rows = manageUsers.getAllRows()
        Logger.info("getting all table data from rows")
        Logger.info("getting tableData ")
        self.getTableData(tableColumns, tableDataMap, rows)
        checkSorting = copy.deepcopy(tableDataMap)
        Logger.debug(f"{sortedTable}")
        Logger.debug(f"{checkSorting}")
        res = (checkSorting == sortedTable)
        Logger.info(f"DATA MATCHED SUCCESSFULLY: {res}")
        return res

    def getOneDropDownOption(self, manageUsers, idx):
        ele = manageUsers.getDropdownOptions()
        Logger.info(f"{idx}th dropdown option")
        self.scrollToElement(ele[idx])
        return ele[idx]

    def getRolesCount(self, tableDataMap):
        roles = self.getIthColData(tableDataMap, 4)
        count = 1
        for ele in roles:
            if "Read" in ele:
                count = 2
                break
        return count

    def getIndex(self, hashSet, idx, n):
        if idx not in hashSet:
            return idx
        else:
            return self.getIndex(hashSet, (idx + 1) % n, n)


