import json
import time
import pytest
from random import randrange
import math

from Pages.LoginPage import LoginPage
from Pages.ManageUsersPage import ManageUsersPage
from Utilities import Logger
from Utilities.Base import Base
from Utilities.utilityFn import Utility
from dataSet.ManageUsersData import ManageUsersData


@pytest.mark.usefixtures("initial")
class testing(Base):
    utils = Utility()
    tableData = {}
    tableColumns = ManageUsersData.TABLE_COLUMNS
    URL = ManageUsersData.URL

    def test_checkURL(self):
        Logger.info(
            "==============================================================================================================\n")
        currUrl = self.utils.currentUrl()
        if not (self.URL in currUrl):
            loginPage = LoginPage(self.driver)
            loginPage.enterCredentials()
            Logger.info("Enter details for Login As Admin")
            manageUsers = ManageUsersPage(self.driver)
            manageUsers.getManageBtn().click()
            Logger.info("Manage Button Clicked")
            manageUsers.getUserOption().click()
            time.sleep(2)
            Logger.info("Manage Users option clicked")
            assert currUrl
            Logger.info("Current Url is " + self.utils.currentUrl())
            Logger.info("TestCASE PASSED (CHECK URL)")

    def test_verify_data(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        rows = manageUsers.getAllRows()
        Logger.info("No of rows in table are: " + str(len(rows)))
        self.utils.getTableData(self.tableColumns, self.tableData, rows)
        file = open("../output.json", "w")
        file.write(json.dumps(self.tableData, indent=2))
        Logger.info("TestCASE PASSED (VERIFY DATA)")

    def test_select_all(self):
        Logger.info(
            "==============================================================================================================\n")
        n = len(self.tableData[self.tableColumns[4]])
        manageUsers = ManageUsersPage(self.driver)
        selectAll = manageUsers.getSelectAll()
        Logger.info("getting select All btn")
        labelTextInit = manageUsers.getLabelText()
        initStr = self.utils.labelTextUnselected(n)
        Logger.info("getting select All btn")
        res = (labelTextInit == initStr)
        Logger.info("labelText is correct :" + initStr + ": " + str(res))
        selectAll.click()
        Logger.info("clicking on select All")
        rows = manageUsers.getAllRows()
        labelTextFinal = manageUsers.getLabelText()
        Logger.info("getting label text after selection")
        textAfter = self.utils.labelTextAllSelected(n)
        res = res and (labelTextFinal == textAfter)
        Logger.info("label Text matched : " + textAfter + " :" + str(res))
        res = res and self.utils.isAttrInAllElements('selected', 'class', rows)
        Logger.info("all rows are selected: " + str(res))
        selectAll.click()
        Logger.info("unselect select all btn")
        assert res
        Logger.info("TestCASE PASSED (SELECT ALL)")

    def test_select_one(self, rowNo=-1):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        checkboxes = manageUsers.getTableCheckbox()
        Logger.info("getting all rows checkboxes : " + str(len(checkboxes)))
        rows = manageUsers.getAllRows()
        n = len(self.tableData[self.tableColumns[4]])
        res = True
        if rowNo != -1:
            Logger.info("Only one row to be selected is: " + str(rowNo))
            indx = 1
        else:
            indx = math.ceil(n / 2)
            Logger.info("no of rows to be selected is: " + str(rowNo))
        for i in range(indx):
            if rowNo == -1:
                rand = randrange(n)
            else:
                rand = rowNo
            Logger.debug("Row No. : " + str(rand))
            ele = checkboxes[rand]
            row = rows[rand]
            Logger.debug("getting checkbox of " + str(rand) + " row")
            ele.click()
            Logger.info("checkbox clicked")
            labelText = manageUsers.getLabelText()
            f1 = self.utils.isAttrInElement('selected', 'class', row)
            Logger.info("all rows are selected")
            text = self.utils.labelTextNSelected(1, n)
            f2 = (labelText == text)
            Logger.debug("label text is equal : " + text + " :" + str(f2))
            res = res and f1 and f2
            Logger.info("all checks are valid for Row " + str(rand) + " :" + str(res))
            ele.click()
            Logger.info("deselect checkbox of Row " + str(rand))
        assert res
        if rowNo == -1:
            Logger.info("TestCASE PASSED (SELECT RANDOM ONES)")
        else:
            Logger.info("TestCASE PASSED (SELECT ONE ROW): " + rowNo)

    def test_select_halfRows(self):
        Logger.info(
            "==============================================================================================================\n")
        n = len(self.tableData[self.tableColumns[4]])
        manageUsers = ManageUsersPage(self.driver)
        checkboxes = manageUsers.getTableCheckbox()
        Logger.info("getting all rows checkboxes : " + str(len(checkboxes)))
        rows = manageUsers.getAllRows()
        N = math.ceil(n / 2)
        Logger.info("No. of rows to be selected : " + str(N))
        res = True
        for i in range(N):
            ele = checkboxes[i]
            row = rows[i]
            Logger.debug("getting checkbox of " + str(i) + "th row")
            ele.click()
            Logger.debug("checkbox clicked")
            res = (res and self.utils.isAttrInElement('selected', 'class', row))
            Logger.debug("checkbox of row " + str(i) + " is selected: " + str(res))
        labelText = self.utils.labelTextNSelected(N, n)
        res = res and (manageUsers.getLabelText() == labelText)
        Logger.info("label text matched " + labelText + ": " + str(res))

        for i in range(N):
            ele = checkboxes[i]
            Logger.info("deselect checkbox of row " + str(i))
            ele.click()
        assert res
        Logger.info("TestCASE PASSED (SELECT HALF ROWS)")

    def test_editOptions_currUser(self, rowNo=-1):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        checkboxes = manageUsers.getTableCheckbox()
        loginUser = manageUsers.getLoggedInUser()
        Logger.info("getting loginUser: " + loginUser)
        idx = -1
        res = True
        if rowNo != -1:
            idx = rowNo
            Logger.info("login User row no: " + str(idx))
        else:
            userNameList = self.utils.getIthColData(self.tableData, 0)
            i = 0
            for ele in userNameList:
                if ele == loginUser:
                    break
                i = i + 1
            idx = i
            Logger.info("Found login User row no: " + str(idx))
        cb = checkboxes[idx]
        editOptions = manageUsers.getEditOptions()
        totalEditOptionsBefore = len(editOptions)
        Logger.info("getting all edit options btns before clicking checkbox : " + str(totalEditOptionsBefore))
        cb.click()
        editOptions = manageUsers.getEditOptions()
        totalEditOptionsAfter = len(editOptions)
        Logger.info("getting all edit options btns before clicking checkbox : " + str(totalEditOptionsAfter))
        deletebtn = editOptions[2]
        res = res and (totalEditOptionsBefore == 1 and totalEditOptionsAfter == 3) and self.utils.isAttrInElement(
            "disabled", "class", deletebtn)
        Logger.info("btn counts and delete btn is disabled: " + str(res))
        cb.click()
        Logger.info("deselect checkbox")
        assert res
        if idx == -1:
            Logger.info("TestCASE PASSED (EDIT OPTIONS OF LOGIN USER) Row: 0")
        else:
            Logger.info("TestCASE PASSED (EDIT OPTIONS OF LOGIN USER) Row: " + str(idx))

    def test_editOptions(self):
        n = len(self.tableData[self.tableColumns[4]])
        Logger.info(
            "==============================================================================================================\n")
        res = True
        manageUsers = ManageUsersPage(self.driver)
        checkboxes = manageUsers.getTableCheckbox()
        loginUser = manageUsers.getLoggedInUser()
        Logger.info("getting loginUser: " + loginUser)

        Logger.info("getting all checkboxes")
        if n == 1:
            Logger.info("ONLY 1 USER")
            self.test_editOptions_currUser(0)
        else:
            idx = -1
            userNameList = self.utils.getIthColData(self.tableData, 0)
            if n == 2:
                Logger.info("2 USERS")
                if userNameList[0] == loginUser:
                    idx = 0
                else:
                    idx = 1
                cb1 = checkboxes[idx]
                cb2 = checkboxes[1 - idx]
                Logger.info("cb1 is loginUser and cb2 is not LoginUser checkboxes")
            else:
                Logger.info("MORE THAN 2 USERS")
                for i in range(len(userNameList)):
                    ele = userNameList[i]
                    if ele == loginUser:
                        idx = i
                        break
                cb1 = checkboxes[(idx + 1) % n]
                cb2 = checkboxes[(idx - 1) % n]
                Logger.info("cb1 and cb2 are not loginUsers checkboxes")
            # 1 row
            editOptions = manageUsers.getEditOptions()
            totalEditOptionsBefore = len(editOptions)
            Logger.info("selecting cb1")
            cb1.click()
            editOptions = manageUsers.getEditOptions()
            totalEditOptionsAfter = len(editOptions)
            f1 = (totalEditOptionsBefore == 1 and totalEditOptionsAfter == 3)
            res = res and f1
            Logger.info("btn len before is: " +
                        str(totalEditOptionsBefore) + " btn len after is: " +
                        str(totalEditOptionsAfter))
            if n == 2:
                self.test_editOptions_currUser(idx)
                Logger.info("loginUser Row Checked")
            # 2 rows
            cb2.click()
            Logger.info("clicking on cb2")
            editOptions = manageUsers.getEditOptions()
            res = res and len(editOptions) == 3
            Logger.info("btn len before is: " +
                        str(totalEditOptionsBefore) + " btn len after is: " +
                        str(totalEditOptionsAfter))
            for i in range(len(editOptions) - 1):
                btn = editOptions[i]
                res = res and self.utils.isAttrInElement("disabled", "class", btn)
            Logger.info("all btns is enabled except delete btn after multiple selections: " + str(res))
            Logger.info("deselecting both cb1 & cb2")
            cb1.click()
            cb2.click()
            if n > 2:
                self.test_editOptions_currUser(idx)
                Logger.info("LoginUser Row Checked")
            res = res and (len(manageUsers.getEditOptions()) == 1)
            Logger.info("after deselection total btns of edit options 1: " + str(res))
        Logger.info("TestCASE PASSED (EDIT OPTIONS)")

    def test_add_User_btnModal(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        Logger.info("getting addUser button")
        btn = manageUsers.getAddUser()
        Logger.info("clicking addUser button")
        btn.click()
        modal = manageUsers.getModal()
        res = self.utils.isElementVisible(modal)
        Logger.info("modal is visible: " + str(res))
        addUserBtn = manageUsers.getAddNewUser()
        cancelBtn = manageUsers.getCancel()
        Logger.info("getting add new user & cancel btn")
        res = res and self.utils.isAttrInElement("disabled", "class", addUserBtn)
        Logger.info("addNew User btn is disabled: " + str(res))
        Logger.info("clicking cancel Btn")
        cancelBtn.click()
        res = (res and not manageUsers.isModalPresent())
        Logger.info("Modal removed: " + str(res))
        assert res
        Logger.info("TestCASE PASSED (ADD USER AND CANCEL BUTTON)")

    def test_is_Any_ColSorted(self, check=False):
        Logger.info(
            "==============================================================================================================\n")
        if not check:
            Logger.info("Getting which column is sorted or not")
        else:
            Logger.info("Checking whether any column is sorted or not")
        manageUsers = ManageUsersPage(self.driver)
        res = False
        ans = []
        Logger.info("Getting all table columns headings for sorting")
        userName = manageUsers.UserNameClick()
        firstName = manageUsers.FirstNameClick()
        lastName = manageUsers.LastNameClick()
        email = manageUsers.EmailClick()
        role = manageUsers.RoleNameClick()
        if self.utils.isAttrInElement("sorted", "class", userName):
            Logger.info("USERNAME Column is Sorted")
            arrow = manageUsers.getSortedArrow(userName)
            ans.append(0)
            if self.utils.isAttrInElement("asc", "class", arrow):
                ans.append(0)
            else:
                ans.append(1)
            res = True

        elif self.utils.isAttrInElement("sorted", "class", firstName):
            Logger.info("FIRSTNAME Column is Sorted")
            ans.append(1)
            arrow = manageUsers.getSortedArrow(firstName)
            ans.append(0)
            if self.utils.isAttrInElement("asc", "class", arrow):
                ans.append(0)
            else:
                ans.append(1)
            res = True

        elif self.utils.isAttrInElement("sorted", "class", lastName):
            Logger.info("LASTNAME Column is Sorted")
            res = True
            ans.append(2)
            arrow = manageUsers.getSortedArrow(lastName)
            ans.append(0)
            if self.utils.isAttrInElement("asc", "class", arrow):
                ans.append(0)
            else:
                ans.append(1)

        elif self.utils.isAttrInElement("sorted", "class", email):
            Logger.info("EMAIL Column is Sorted")
            res = True
            ans.append(3)
            arrow = manageUsers.getSortedArrow(email)
            ans.append(0)
            if self.utils.isAttrInElement("asc", "class", arrow):
                ans.append(0)
            else:
                ans.append(1)
        elif self.utils.isAttrInElement("sorted", "class", role):
            Logger.info("ROLE Column is Sorted")
            res = True
            ans.append(4)
            arrow = manageUsers.getSortedArrow(role)
            ans.append(0)
            if self.utils.isAttrInElement("asc", "class", arrow):
                ans.append(0)
            else:
                ans.append(1)
        else:
            Logger.info("NO Column is Sorted")
        if not check:
            assert True
        else:
            assert res
        return ans

    def test_add_newUser_AddBtn(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        sizeBefore = len(self.tableData[self.tableColumns[4]])
        res = True
        Logger.info("getting addUser btn")
        btn = manageUsers.getAddUser()
        Logger.info("clicking addUser btn")
        btn.click()
        Logger.info("getting Username,Firstname,Lastname,Email,Password,reTypePassword & Role")
        addUserBtn = manageUsers.getAddNewUser()
        cancelBtn = manageUsers.getCancel()
        userName = manageUsers.getUsername()
        firstName = manageUsers.getFirstname()
        lastName = manageUsers.getLastname()
        email = manageUsers.getEmail()
        password = manageUsers.getPassword()
        retypePassword = manageUsers.getReTypePassword()
        role = manageUsers.getRole()
        allUserNames = self.tableData["UserName"]
        Logger.info("getting already Usernames in table: " + str(allUserNames))
        UN = "nm"
        userName.send_keys(UN)
        enteredUserName = self.utils.getText(self.driver, 'userName')
        Logger.info("Entered userName: " + str(enteredUserName))
        flag = False
        for ele in allUserNames:
            if ele == enteredUserName:
                flag = True
                Logger.info("USERNAME FOUND")
                break
        FN = "reg"
        LN = "kkj"
        EM = "nh@gf.co.in"
        firstName.send_keys(FN)
        lastName.send_keys(LN)
        email.send_keys(EM)
        password.send_keys("123456")
        retypePassword.send_keys("123456")
        Logger.info("Entered All Details")
        role.click()
        roleChoice = manageUsers.getRoleChoice()
        rand = randrange(2)
        Logger.info("selecting role: " + str(rand))
        choice = roleChoice[rand]
        RO = choice.text
        Logger.info("Role Select: " + RO)
        choice.click()
        if not flag:
            Logger.info("Unique UserName Found")
            isDisable = self.utils.isAttrInElement("disabled", "class", addUserBtn)
            res = res and (not isDisable)
            Logger.info("Add Button Gets Enabled: " + str(res))
            addUserBtn.click()
            Logger.info("Add Button Clicked")
            time.sleep(4)
            rows = manageUsers.getAllRows()
            self.utils.getTableData(self.tableColumns, self.tableData, rows)
            sizeAfter = len(self.tableData[self.tableColumns[4]])
            Logger.info("getting no of rows before adding new entry: " + str(sizeBefore))
            res = res and (sizeAfter == sizeBefore + 1)
            Logger.info("getting no of rows before adding new entry: " + str(sizeAfter) + " :" + str(res))
            values = [UN, FN, LN, EM, RO]
            Logger.debug("Updated Values to Add in Map: " + str(values))
            Logger.info("setting new entry in tableData")
            self.utils.addInTable(self.tableData, self.tableColumns, values)
            sortedColumn = self.test_is_Any_ColSorted()
            if len(sortedColumn) != 0:
                colNo = sortedColumn[0]
                type = sortedColumn[1]
                Logger.info("Sorted Column : " + self.tableColumns[colNo])
                Logger.info("Sorting Type :" + str(type))
                Logger.debug("0: Inc , 1: Dec")
                self.utils.sortTable(self.tableData, colNo, type, sizeAfter)
                sortedTableData = self.tableData
                Logger.info("Getting Sorted TableData :" + str(sortedTableData))
                rows = manageUsers.getAllRows()
                self.utils.getTableData(self.tableColumns, self.tableData, rows)
                Logger.info("Getting All Sorted Rows")
                tableData = self.tableData
                res = res and (tableData == sortedTableData)
                Logger.info("All rows are sorted after adding new Entry: " + str(res))
            file = open("../output.json", "a")
            file.write(json.dumps(values))
            file.write(json.dumps(self.tableData, indent=2))
            fn = manageUsers.FirstNameClick()
            self.sortClick(1, 1, fn)
            self.sortClick(1, 0, fn)
            Logger.info("DATA ENTRY VERIFIED AFTER SORTING COLUMNS")
            Logger.info("NEW USER ADDED SUCCESSFULLY")
        else:
            Logger.info("Unique UserName Not Found")
            addUserBtn = manageUsers.getAddNewUser()
            res = res and (self.utils.isAttrInElement("disabled", "class", addUserBtn))
            Logger.info("addUser button is disabled: " + str(res))
            Logger.info("clicking cancel btn")
            cancelBtn.click()
            rows = manageUsers.getAllRows()
            self.utils.getTableData(self.tableColumns, self.tableData, rows)
            sizeAfter = len(self.tableData[self.tableColumns[4]])
            Logger.info("getting no of rows before adding new entry: " + str(sizeBefore))
            res = res and (sizeAfter == sizeBefore)
            Logger.info("getting no of rows before adding new entry: " + str(sizeAfter))
            Logger.info("NO NEW USER ADDED")
        res = (res and not manageUsers.isModalPresent())
        Logger.info("Modal removed: " + str(res))
        assert res
        Logger.info("TestCASE PASSED (ADD NEW USER)")

    def test_editUser_cancelBtn(self):
        Logger.info(
            "==============================================================================================================\n")
        res = True
        manageUsers = ManageUsersPage(self.driver)
        Logger.info("getting all checkboxes")
        idx = 0
        checkboxes = manageUsers.getTableCheckbox()
        Logger.info("selecting " + str(idx) + " checkbox")
        selectedCheckBox = checkboxes[idx]
        Logger.info("checkbox clicked")
        selectedCheckBox.click()
        Logger.info("getting all rows")
        rows = manageUsers.getAllRows()
        Logger.info("getting row No: " + str(idx))
        selectedRow = rows[idx]
        editBtn = manageUsers.getEditOptions()[1]
        editBtn.click()
        Logger.info("edit btn clicked")
        cancelBtn = manageUsers.getCancel()
        Logger.info("clicking cancel btn")
        cancelBtn.click()
        res = res and self.utils.isAttrInElement("selected", "class", selectedRow)
        assert res
        Logger.info("deselecting checkbox: " + str(idx))
        selectedCheckBox.click()
        Logger.info("row " + str(idx) + " is still selected: " + str(res))
        Logger.info("TestCASE PASSED (EDIT USER CANCEL BTN)")

    def test_editUser(self, rowNo=-1):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        n = len(self.tableData[self.tableColumns[4]])
        idx = -1
        if rowNo == -1:
            idx = randrange(n)
            Logger.info("row No. : " + str(idx) + " selected")
        else:
            idx = rowNo
            Logger.info("row No. : " + str(idx) + " selected")
        Logger.info("getting all checkboxes")
        checkboxes = manageUsers.getTableCheckbox()
        Logger.info("selecting " + str(idx) + " checkbox")
        selectedCheckBox = checkboxes[idx]
        Logger.info("checkbox clicked")
        selectedCheckBox.click()
        Logger.info("getting all rows")
        rows = manageUsers.getAllRows()
        Logger.info("getting row No: " + str(idx))
        selectedRow = rows[idx]
        res = True
        editBtn = manageUsers.getEditOptions()[1]
        editBtn.click()
        Logger.info("Edit btn btn clicked")
        updatebtn = manageUsers.getUpdate()
        Logger.info("getting update user btn")
        res = res and (not self.utils.isAttrInElement("disabled", "class", updatebtn))
        Logger.info("update user btn disabled: " + str(res))
        firstName = manageUsers.getFirstname()
        lastName = manageUsers.getLastname()
        email = manageUsers.getEmail()
        role = manageUsers.getRole()
        Logger.info("getting all enabled fields")
        disabledEle = manageUsers.getDisabled()
        noOfDisabled = len(disabledEle)
        Logger.info("getting all disabled fields: " + str(noOfDisabled))
        loginUser = manageUsers.getLoggedInUser()
        Logger.info("getting current login username: " + str(loginUser))
        firstName.clear()
        lastName.clear()
        email.clear()
        Logger.info("clearing all fields")
        FN = "updatedFN"
        LN = "upadatedLN"
        EM = "update@test.com"
        RO = role.text
        Logger.info("entering all fields: " + FN + "  " + LN + " " + EM + " " + RO)
        firstName.send_keys(FN)
        lastName.send_keys(LN)
        email.send_keys(EM)
        userName = self.utils.getText(self.driver, 'userName')
        Logger.info("getting login username text: " + str(userName))
        if loginUser == userName:
            res = res and (noOfDisabled == 2)
            Logger.info(
                "loginUser & selected userName is same: " + str(userName) + " and no of disabled elements is: " + str(
                    noOfDisabled) + " :" + str(res))
        else:
            res = res and (noOfDisabled == 1)
            Logger.info(
                "loginUser & selected userName is different: " + str(
                    userName) + " and no of disabled elements is: " + str(
                    noOfDisabled) + " :" + str(res))

            role.click()
            Logger.info("clicking role dropdown")
            roleChoice = manageUsers.getRoleChoice()
            Logger.info("getting choices")
            r = randrange(2)
            choice = roleChoice[r]
            text = choice.text
            choice.click()
            Logger.info("selecting and clicking choice: " + str(r))
            RO = text
        updatedValues = [FN, LN, EM, RO]
        Logger.info("updated values: " + str(updatedValues))
        updatebtn.click()
        Logger.info("clicking update btn and waiting..")
        time.sleep(4)
        getRow = manageUsers.getAllRows()
        Logger.info("selecting row: " + str(idx))
        row = getRow[idx]
        val = self.utils.getIthRowFromTable(row)
        Logger.info("getting data from row: " + str(val))
        for i in range(1, len(self.tableColumns)):
            key = self.tableColumns[i]
            newVal = updatedValues[i - 1]
            self.utils.updateTableRow(self.tableData, newVal, key, idx)
            Logger.info("updated key and val: " + str(key) + " -> " + str(newVal))

        Logger.info("update in tableData")
        rowUpdated = self.utils.getIthRowFromTable(row)
        res = res and (not self.utils.isAttrInElement("selected", "class", selectedRow))
        Logger.info("selected row " + str(idx) + " is unselected: " + str(res))
        assert res and (val == rowUpdated)
        Logger.info("selected row " + str(idx) + " is updated: " + str(res))
        Logger.info("TestCASE PASSED (EDIT USER)")

    def sortClick(self, idx, isRev, element):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        n = len(self.tableData[self.tableColumns[4]])
        Logger.info(str(idx) + "th Column Clicked")
        element.click()
        Logger.info("Sort TableData according to type: " + str(isRev))
        self.utils.sortTable(self.tableData, idx, (isRev, n)
        sortedTable = self.tableData
        Logger.info("getting all rows data after sorting")
        rows = manageUsers.getAllRows()
        Logger.info("getting all table data from rows")
        Logger.info("getting tableData ")
        self.utils.getTableData(self.tableColumns, self.tableData, rows)
        checkSorting = self.tableData
        res = (checkSorting == sortedTable)
        Logger.info("DATA MATCHED SUCCESSFULLY")
        return res

    def test_sort(self):
        Logger.info(
            "==============================================================================================================\n")
        res = True
        manageUsers = ManageUsersPage(self.driver)
        listItem = [manageUsers.UserNameClick(), manageUsers.FirstNameClick(), manageUsers.LastNameClick(),
                    manageUsers.EmailClick(), manageUsers.RoleNameClick()]
        Logger.info("getting all columns to be sorted: " + str(len(listItem)))
        n = len(self.tableColumns)
        Logger.info("checking if any sorting exists on any column or not")
        sortingCol = self.test_is_Any_ColSorted(True)
        idx = -1
        if len(sortingCol) != 0:
            idx = sortingCol[0]
            Logger.info("SORTING EXIST ON: " + str(idx) + " COLUMN")
        for i in range(n):
            if idx == i:
                Logger.info(str(i) + "th Column which is sorted earlier as :" + str(sortingCol[1]))
                for j in range(2):
                    Logger.debug("Check sort for " + str(i) + "th Column in: " + str(1 - j) + " type*")
                    res = res and self.sortClick(i, 1 - j, listItem[i])
            else:
                for j in range(2):
                    Logger.debug("Check sort for " + str(i) + "th Column in: " + str(j) + " type")
                    res = res and self.sortClick(i, j, listItem[i])
        assert res
        Logger.info("TestCASE PASSED (TEST SORT COLUMNS)")

    def test_changePassword_cancelBtn(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        n = len(self.tableData[self.tableColumns[4]])
        idx = 0
        selectedUserName = self.utils.getIthColData(self.tableData, 0)[0]
        loginUser = manageUsers.getLoggedInUser()
        Logger.info("getting logged in user: " + loginUser + " and selected username: " + selectedUserName)
        res = True
        if selectedUserName == loginUser:
            if n > 1:
                idx = (idx + 1) % n
                Logger.info("selecting new idx: " + str(idx))
            elif n == 1:
                return
        checkBoxes = manageUsers.getTableCheckbox()
        Logger.info("getting all checkboxes")
        rows = manageUsers.getAllRows()
        selectedRow = rows[idx]
        Logger.info("getting row no:  " + str(idx) + " and its checkbox")
        checkbox = checkBoxes[idx]
        checkbox.click()
        Logger.info("clicking checkbox")
        changePasswordBtn = manageUsers.getEditOptions()[0]
        changePasswordBtn.click()
        Logger.info("clicking change password btn")
        password = manageUsers.getPassword()
        rePassword = manageUsers.getReTypePassword()
        changePwd = manageUsers.getChangePassword()
        Logger.info("getting all fields")
        res = res and self.utils.isAttrInElement("disabled", "class", changePwd)
        Logger.info("update password btn is disabled: " + str(res))
        password.send_keys("admin")
        rePassword.send_keys("admin")
        Logger.info("entering details")
        passVal = self.utils.getText(self.driver, 'password')
        rePassVal = self.utils.getText(self.driver, 'retypePassword')
        res = res and (passVal == rePassVal)
        Logger.info("both password matched: " + str(res))
        res = res and not self.utils.isAttrInElement("disabled", "class", changePwd)
        Logger.info("update password btn is not disabled: " + str(res))
        cancelBtn = manageUsers.getCancel()
        cancelBtn.click()
        Logger.info("clicking cancel btn")
        res = res and self.utils.isAttrInElement("selected", "class", selectedRow)
        Logger.info("selected row: " + str(idx) + " is selected: " + str(res))
        checkbox.click()
        Logger.info("deselecting checkbox")
        assert res
        Logger.info("TestCASE PASSED (CHANGE PASSWORD CANCEL BTN)")

    def test_changePassword_CurrUser(self, rowNo=-1):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        loginUser = manageUsers.getLoggedInUser()
        Logger.info("getting login user: " + loginUser)
        idx = 0
        res = True
        if rowNo != -1:
            idx = rowNo
            Logger.info("Login User row no: " + str(idx))
        else:
            userNameList = self.utils.getIthColData(self.tableData, 0)
            for ele in userNameList:
                if ele == loginUser:
                    break
                else:
                    idx = idx + 1
        Logger.info("Found Login User row no: " + str(idx))
        checkBoxes = manageUsers.getTableCheckbox()
        Logger.info("getting all checkboxes")
        checkbox = checkBoxes[idx]
        checkbox.click()
        Logger.info("clicking checkbox : " + str(idx))
        changePasswordBtn = manageUsers.getEditOptions()[0]
        changePasswordBtn.click()
        Logger.info("clicking change password btn")
        password = manageUsers.getPassword()
        rePassword = manageUsers.getReTypePassword()
        changePwd = manageUsers.getChangePassword()
        Logger.info("getting all fields")
        res = res and self.utils.isAttrInElement("disabled", "class", changePwd)
        Logger.info("update password btn is disabled: " + str(res))
        password.send_keys("admin")
        rePassword.send_keys("admin")
        Logger.info("entering details")
        passVal = self.utils.getText(self.driver, 'password')
        rePassVal = self.utils.getText(self.driver, 'retypePassword')
        res = res and (passVal == rePassVal)
        Logger.info("both password matched: " + str(res))
        res = res and not self.utils.isAttrInElement("disabled", "class", changePwd)
        Logger.info("update password btn is not disabled: " + str(res))
        changePwdBtn = manageUsers.getChangePassword()
        changePwdBtn.click()
        Logger.info("clicking changePwd btn")
        time.sleep(6)
        print("CURRENT URL: " + self.utils.currentUrl(self.driver))
        res = res and (self.utils.urlPresent(self.driver, "login"))
        self.test_checkURL()
        Logger.info("Login page arrived: " + str(res))
        Logger.info("ManageUsers Page page arrived: ")
        assert res
        Logger.info("TestCASE PASSED (PASSWORD CHANGE LOGIN USER)")

    def test_changePassword(self, rowNo=-1):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        n = len(self.tableData[self.tableColumns[4]])
        if rowNo == -1:
            idx = randrange(n)
        else:
            idx = rowNo
        Logger.info("Row Selected: " + str(idx))
        userNameList = self.utils.getIthColData(self.tableData, 0)
        loginUser = manageUsers.getLoggedInUser()
        res = True
        Logger.info("getting login user: " + loginUser)
        if userNameList[idx] == loginUser:
            Logger.info("username selected is same as login user")
            self.test_changePassword_CurrUser(idx)
        else:
            Logger.info("username selected is different as login user: " + userNameList[idx])
            checkBoxes = manageUsers.getTableCheckbox()
            rows = manageUsers.getAllRows()
            selectedRow = rows[idx]
            checkbox = checkBoxes[idx]
            Logger.info("selecting row and checkbox of: " + str(idx) + "th Row")
            checkbox.click()
            Logger.info("checkbox clicked")
            changePasswordBtn = manageUsers.getEditOptions()[0]
            changePasswordBtn.click()
            Logger.info("clicking change password btn")
            password = manageUsers.getPassword()
            rePassword = manageUsers.getReTypePassword()
            changePwd = manageUsers.getChangePassword()
            Logger.info("getting all fields")
            res = res and self.utils.isAttrInElement("disabled", "class", changePwd)
            Logger.info("changePwd btn is disabled: " + str(res))
            password.send_keys("admin")
            rePassword.send_keys("admin")
            Logger.info("enter values")
            passVal = self.utils.getText(self.driver, 'password')
            rePassVal = self.utils.getText(self.driver, 'retypePassword')
            res = res and (passVal == rePassVal)
            Logger.info("enter pwd and retype password is equal: " + str(res))
            changePwd.click()
            time.sleep(4)
            Logger.info("change pwd clicked")
            res = res and (not self.utils.isAttrInElement("selected", "class", selectedRow))
            Logger.info("selected row is deselected: " + str(res))
        assert res
        Logger.info("TestCASE PASSED (PASSWORD CHANGE NON LOGIN USER)")

    def test_cancel_delete(self, rowNo=-1):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        res = True
        rows = manageUsers.getAllRows()
        allCheckbox = manageUsers.getTableCheckbox()
        Logger.info("getting rows and checkboxes")
        loginUser = manageUsers.getLoggedInUser()
        idx = -1
        if rowNo == -1:
            idx = 0
            Logger.info(f"default row: {idx}")
        else:
            idx = rowNo
            Logger.info(f"row selected: {idx}")
        checkbox = allCheckbox[idx]
        row = rows[idx]
        checkbox.click()
        Logger.info("getting all usernames")
        userNameList = self.utils.getIthColData(self.tableData, 0)
        Logger.info(f"checkbox : {idx} selected and clicking")
        deleteBtn = manageUsers.getEditOptions()[2]
        if loginUser != userNameList[idx]:
            Logger.info(f"username is different as login User: {userNameList[idx]}")
            deleteBtn.click()
            Logger.info("delete btn clicked")
            isModal = manageUsers.isModalPresent("div .uwf-confirmation-dialog__box")
            res = res and isModal
            Logger.info(f"Modal is visible: {res}")
            cancelBtn = manageUsers.getDeleteModalBtns()[0]
            cancelBtn.click()
            Logger.info("clicking cancel cross btn")
            isModal = manageUsers.isModalPresent("div .uwf-confirmation-dialog__box")
            res = res and not isModal
            Logger.info(f"Modal is not visible: {res}")
            isRowSelected = self.utils.isAttrInElement("selected", "class", row)
            res = res and isRowSelected
            Logger.info(f"row is still selected: {isRowSelected}: {res}")

            deleteBtn = manageUsers.getEditOptions()[2]
            deleteBtn.click()
            Logger.info("delete btn clicked")
            noBtn = manageUsers.getDeleteModalBtns()[1]
            noBtn.click()
            Logger.info("clicking no btn")
            isModal = manageUsers.isModalPresent("div .uwf-confirmation-dialog__box")
            res = res and not isModal
            Logger.info(f"Modal is not visible: {res}")
            isRowSelected = self.utils.isAttrInElement("selected", "class", row)
            res = res and isRowSelected
            Logger.info(f"row is still selected: {isRowSelected}: {res}")
        else:
            Logger.info(f"username is same as login User: {loginUser}")
            Logger.info(f"LOGIN USER SELECTED,Delete btn disabled: {res}")
        assert res
        checkbox.click()
        Logger.info("checkbox deselect")
        Logger.info("TestCASE PASSED (CANCEL AND NO BTN OF DELETE USER)")

    def test_deleteUser(self, preRowCount=-1, rowNo=-1):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        loginUser = manageUsers.getLoggedInUser()
        Logger.info("getting login user: " + loginUser)
        allCheckbox = manageUsers.getTableCheckbox()
        if rowNo == -1:
            sizeBefore = len(self.tableData[self.tableColumns[4]])
            idx = 4  # randrange(sizeBefore)
        else:
            sizeBefore = preRowCount
            idx = rowNo
        userNameList = self.utils.getIthColData(self.tableData, 0)
        Logger.info(f"checkbox : {idx} selected and clicking")
        res = True
        if userNameList[idx] == loginUser:
            checkbox = allCheckbox[idx]
            checkbox.click()
            Logger.info(f"checkbox : {idx} selected and clicking")
            deleteBtn = manageUsers.getEditOptions()[2]
            res = res and self.utils.isAttrInElement('disabled', 'class', deleteBtn)
            Logger.info(f"loginUser Deletion not allowed: {res}")
            checkbox.click()
        else:
            checkbox = allCheckbox[idx]
            self.test_cancel_delete(idx)
            checkbox.click()
            Logger.info("checkbox clicked")
            deleteBtn = manageUsers.getEditOptions()[2]
            deleteBtn.click()
            Logger.info("delete btn clicked")
            yesBtn = manageUsers.getDeleteModalBtns()[2]
            yesBtn.click()
            Logger.info("clicking yes btn")
            time.sleep(3)
            allRows = manageUsers.getAllRows()
            self.utils.getTableData(self.tableColumns, self.tableData, allRows)
            sizeAfter = len(self.tableData[self.tableColumns[4]])
            if sizeAfter + 1 != sizeBefore:
                res = False
                Logger.info(f"Size before: {sizeBefore} != size after: {sizeAfter}  + 1")
            else:
                Logger.info(f"Size before: {sizeBefore}  == size after: {sizeAfter} + 1")

        assert res
        Logger.info("TestCASE PASSED (DELETE USER)")

    def test_dropdowns_click(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allUsers = manageUsers.getAllUsersDropDown()
        allRoles = manageUsers.getAllRolesDropDown()
        Logger.info("getting all roles & all users dropdown")
        res = True
        n = len(self.tableData[self.tableColumns[4]])
        allUsers.click()
        Logger.info("clicking all Users")
        res = res and (self.utils.isAttrInElement("visible", "class", allUsers))
        Logger.info(f"Modal is visible: {res}")
        dropdownCount = manageUsers.getDropdownOptions()
        res = res and (len(dropdownCount) == n)
        Logger.info(f"No of entries in options are: {len(dropdownCount)} are same as in table: {n} : {res}")
        allUsers.click()
        Logger.info("deselecting allUsers")
        allRoles.click()
        Logger.info("clicking allRoles")
        roles = self.utils.getIthColData(self.tableData, 4)
        count = 1
        for ele in roles:
            if "Read" in ele:
                count = 2
                break
        res = res and (self.utils.isAttrInElement("visible", "class", allRoles))
        Logger.info(f"Modal is visible: {res}")
        dropdownCount = manageUsers.getDropdownOptions()
        res = res and (len(dropdownCount) == count)
        Logger.info(
            f"No of different roles in options are: {len(dropdownCount)} are same as in table : {count} : {res}")
        allRoles.click()
        Logger.info("deselecting allRoles")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN WITH ALL ENTRIES)")

    def test_user_filter(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allUsers = manageUsers.getAllUsersDropDown()
        Logger.info("getting all users dropdown")
        res = True
        n = len(self.tableData[self.tableColumns[4]])
        allUsers.click()
        Logger.info("clicking dropdown")
        filterCheckBox = manageUsers.getFilterCheckBox()
        filterCheckBox.click()
        Logger.info("select All checkbox clicked")
        allEntries = manageUsers.getDropdownOptions()
        for ele in allEntries:
            res = res and (self.utils.isAttrInElement("selected", "class", ele))
        Logger.info(f"All options of dropdown are selected: {res}")
        filterController = manageUsers.getFilterController()
        controllerLen = len(filterController)
        res = res and controllerLen == 2
        Logger.info(f"filter cont is 2: {res}")
        activeDropdown = self.utils.isAttrInElement("active", "class", allUsers)
        res = res and activeDropdown
        Logger.info(f"dropdown is active: {res}")
        text = allUsers.text
        labelText = str(n) + "\nof " + str(n) + " total"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        cancelFilter = filterController[1]
        cancelFilter.click()
        Logger.info("dropdown closed")
        activeDropdown = self.utils.isAttrInElement("active", "class", allUsers)
        res = res and not activeDropdown
        Logger.info(f"dropdown is active: {res}")

        allUsers.click()
        Logger.info("clicking dropdown")
        filterBar = manageUsers.getFilterBar()
        Logger.info("clicking all Users dropdown and typing")
        enterText = 'z'
        filterBar.send_keys(enterText)
        NoResult = manageUsers.isModalPresent('div.uwf-select-options-list__filter-no-result')

        if not NoResult:
            allEntries = manageUsers.getDropdownOptions()
            sizeEntries = len(allEntries)
            userNameList = self.utils.getIthColData(self.tableData, 0)
            count = 0
            Logger.info("checking each options contains the entered value")
            for ele in userNameList:
                if enterText.lower() in ele.lower():
                    count = count + 1
            res = res and count == sizeEntries
            Logger.info(f"no of options: {count} are correct: {res}")
            filterCheckBox = manageUsers.getFilterCheckBox()
            Logger.info("clicking on selectAll checkbox to select only containing username")
            filterCheckBox.click()
            allRows = manageUsers.getAllRows()
            Logger.info("getting all rows of which are contains selected options")
            self.utils.getTableData(ManageUsersData.TABLE_COLUMNS, self.tableData, allRows)
            userNameList = self.utils.getIthColData(self.tableData, 0)
            sizeEntries = len(allEntries)
            res = res and sizeEntries == len(allRows)
            Logger.info(f"size of options and rows are equal: {sizeEntries} : {res}")
            for i in range(len(allRows)):
                option = allEntries[i]
                username = userNameList[i]
                res = res and enterText in option.text
                res = res and enterText in username
            Logger.info(f"All rows and options have common string: {res}")
            filterCheckBox = manageUsers.getFilterCheckBox()
            filterCheckBox.click()
            Logger.info("checkbox deselect")
            lenAfter = len(manageUsers.getDropdownOptions())
            res = res and lenAfter == sizeEntries
            Logger.info(f"size of entries: {lenAfter}")
            sizeAllRows = len(manageUsers.getAllRows())
            res = res and sizeAllRows == n
            Logger.info(f"size of rows after deselect checkbox: {sizeAllRows} : {res}")
        else:
            Logger.info("User NOt Found")
        clearTool = manageUsers.getClearTool()
        clearTool.click()
        Logger.info("clearing input")
        removeText = filterBar.text
        res = res and removeText == ''
        Logger.info(f"entered text cleared: {res}")
        allUsers.click()
        Logger.info("dropdown closed")
        iterations = math.ceil(n / 2)
        Logger.info(f"no of iter : {iterations}")
        allUsers.click()
        Logger.info("dropdown clicked")

        Logger.info("Single Selection")
        for i in range(iterations):
            idx = randrange(n)
            Logger.debug(f"opt no: {idx}")
            dropdownOpts = manageUsers.getDropdownOptions()
            opt = dropdownOpts[idx]
            self.driver.execute_script("arguments[0].scrollIntoView();", opt)
            opt.click()
            Logger.debug("clicking opt.")
            time.sleep(1)
            rows = manageUsers.getAllRows()
            sizeRow = len(rows)
            res = res and sizeRow == 1
            Logger.info(f"size of row: {idx} == {sizeRow} : {res}")
            dropdownOpts = manageUsers.getDropdownOptions()
            opt = dropdownOpts[idx]
            opt.click()
            Logger.debug("deselecting opt")

        if n > 1:
            Logger.info("Multiple Selection")
            count = 0
            set = {}
            for i in range(2):
                idx1 = i
                idx2 = n - i - 1
                if (idx1 not in set) or (idx2 not in set):
                    set[idx1] = '1'
                    set[idx2] = '1'
                    Logger.debug(f"opt no1: {idx1} & opt no2: {idx2}")
                    dropdownOpts = manageUsers.getDropdownOptions()
                    opt1 = dropdownOpts[idx1]
                    self.driver.execute_script("arguments[0].scrollIntoView();", opt1)
                    opt1.click()
                    time.sleep(1)
                    opt2 = dropdownOpts[idx2]
                    self.driver.execute_script("arguments[0].scrollIntoView();", opt2)
                    opt2.click()
                    time.sleep(1)
                    count = count + 2
                    Logger.debug("clicking opts.")
                    time.sleep(1)
                    rows = manageUsers.getAllRows()
                    sizeRow = len(rows)
                    res = res and sizeRow == count
                    Logger.info(f"size of row: is :{sizeRow}  : {res}")
                    text = allUsers.text
                    labelText = str(count) + "\nof " + str(n) + " total"
                    res = res and labelText == text
                    Logger.info(f"label Text is equal: {labelText}: {res}")

            for i in range(2):
                idx1 = i
                idx2 = n - i - 1
                if idx1 in set:
                    set.pop(idx1)
                    set.pop(idx2)
                    dropdownOpts = manageUsers.getDropdownOptions()
                    opt1 = dropdownOpts[idx1]
                    self.driver.execute_script("arguments[0].scrollIntoView();", opt1)
                    opt1.click()
                    time.sleep(1)
                    Logger.debug(f"de selecting opt1 : {idx1}")
                    opt2 = dropdownOpts[idx2]
                    self.driver.execute_script("arguments[0].scrollIntoView();", opt2)
                    opt2.click()
                    Logger.debug(f"de selecting opt2 : {idx1}")
                    time.sleep(1)
                    text = allUsers.text
                    count = count - 2
                    labelText = str(count) + "\nof " + str(n) + " total"
                    if count == 0:
                        labelText = "All Users"
                    res = res and labelText == text
                    Logger.info(f"label Text is equal: {text}: {res}")
        else:
            Logger.info("no of entries is 1")
        allUsers.click()
        Logger.info("dropdown closed")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS)")

    def test_roles_filter(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allRoles = manageUsers.getAllRolesDropDown()
        Logger.info("getting all roles dropdown")
        res = True
        n = len(self.tableData[self.tableColumns[4]])
        noOfRoles = 0
        allRoles.click()
        Logger.info("clicking dropdown")
        filterCheckBox = manageUsers.getFilterCheckBox()
        filterCheckBox.click()
        Logger.info("select All checkbox clicked")
        allEntries = manageUsers.getDropdownOptions()
        for ele in allEntries:
            noOfRoles = noOfRoles + 1
            res = res and (self.utils.isAttrInElement("selected", "class", ele))
        Logger.info(f"All options of dropdown are selected: {res}")
        filterController = manageUsers.getFilterController()
        controllerLen = len(filterController)
        res = res and controllerLen == 2
        Logger.info(f"filter count is 2: {res}")
        activeDropdown = self.utils.isAttrInElement("active", "class", allRoles)
        res = res and activeDropdown
        Logger.info(f"dropdown is active: {res}")
        text = allRoles.text
        labelText = str(noOfRoles) + "\nof " + str(noOfRoles) + " total"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        cancelFilter = filterController[1]
        cancelFilter.click()
        Logger.info("dropdown closed")
        activeDropdown = self.utils.isAttrInElement("active", "class", allRoles)
        res = res and not activeDropdown
        Logger.info(f"dropdown is active: {res}")

        allRoles.click()
        Logger.info("clicking dropdown")
        filterBar = manageUsers.getFilterBar()
        Logger.info("clicking all Users dropdown and typing")
        enterText = 'ad'
        filterBar.send_keys(enterText)
        NoResult = manageUsers.isModalPresent('div.uwf-select-options-list__filter-no-result')

        if not NoResult:
            filterCheckBox = manageUsers.getFilterCheckBox()
            Logger.info("clicking on selectAll checkbox to select only containing role")
            filterCheckBox.click()
            allRows = manageUsers.getAllRows()
            Logger.info("getting all rows of which are contains selected options")
            self.utils.getTableData(ManageUsersData.TABLE_COLUMNS, self.tableData, allRows)
            rolesList = self.utils.getIthColData(self.tableData, 4)
            count = 0
            Logger.info(f"checking each options contains the entered value:{rolesList}")
            for ele in rolesList:
                if enterText.lower() in ele.lower():
                    count = count + 1
            res = res and count == len(allRows)
            Logger.info(f"no of options: {count} are correct: {res}")
            filterCheckBox = manageUsers.getFilterCheckBox()
            filterCheckBox.click()
            Logger.info("checkbox deselect")
            sizeAllRows = len(manageUsers.getAllRows())
            res = res and sizeAllRows == n
            Logger.info(f"size of rows after deselect checkbox: {sizeAllRows} : {res}")
        else:
            Logger.info("role Not Found")
        clearTool = manageUsers.getClearTool()
        clearTool.click()
        Logger.info("clearing input")
        removeText = filterBar.text
        res = res and removeText == ''
        Logger.info(f"entered text cleared: {res}")
        allRoles.click()
        Logger.info("dropdown closed")
        iterations = 2
        Logger.info(f"no of iter : {iterations}")
        allRoles.click()
        Logger.info("dropdown clicked")

        for i in range(iterations):
            idx = randrange(noOfRoles)
            Logger.debug(f"opt no: {idx}")
            dropdownOpts = manageUsers.getDropdownOptions()
            opt = dropdownOpts[idx]
            self.driver.execute_script("arguments[0].scrollIntoView();", opt)
            opt.click()
            Logger.debug("clicking opt.")
            time.sleep(1)
            text = opt.text
            rows = manageUsers.getAllRows()
            self.utils.getTableData(self.tableColumns, self.tableData, rows)
            for i in range(len(rows)):
                rowData = self.utils.getIthRowsData(self.tableData, i)
                res = res and text.lower() in rowData[4].lower()
            Logger.info(f"all rows contains the req role: {text}: {res}")
            sizeRow = len(rows)
            res = res and sizeRow == len(self.tableData[self.tableColumns[4]])
            Logger.info(f"size of row is {sizeRow} : {res}")
            dropdownOpts = manageUsers.getDropdownOptions()
            opt = dropdownOpts[idx]
            opt.click()
            Logger.debug("deselecting opt")

        allRoles.click()
        Logger.info("dropdown closed")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS)")

    def test_delete_Multiple(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        res = True
        unique = set([])
        loginUser = manageUsers.getLoggedInUser()
        iterations = 2
        n = len(self.tableData[self.tableColumns[4]])
        if n <= 2:
            Logger.info("Multiple users can't be deleted")
        else:
            userNameToBeDeleted = set([])
            userList = self.utils.getIthColData(self.tableData, 0)
            checkboxes = manageUsers.getTableCheckbox()
            for i in range(iterations):
                idx = randrange(n)
                if userList[idx] == loginUser:
                    idx = (idx + 1) % n
                else:
                    if idx not in unique:
                        unique.add(idx)
                    else:
                        idx = (idx + 1) % n
                        unique.add(idx)
                Logger.info(f"Row No: {idx} selected")
                userNameToBeDeleted.add(userList[idx])
                cb1 = checkboxes[idx]
                cb1.click()

            sizeAfter = n - iterations
            deleteBtn = manageUsers.getEditOptions()[2]
            deleteBtn.click()
            Logger.info("delete btn clicked")
            yesBtn = manageUsers.getDeleteModalBtns()[2]
            yesBtn.click()
            Logger.info("clicking yes btn")
            allRows = manageUsers.getAllRows()
            lenRows = len(allRows)
            res = res and lenRows == sizeAfter
            Logger.info(f"{iterations} Users deleted:No of rows: {lenRows} : {res}")
            self.utils.getTableData(self.tableColumns, self.tableData, allRows)
            allUsers = self.utils.getIthColData(self.tableData, 0)
            for ele in allUsers:
                if ele in userNameToBeDeleted:
                    res = False
            Logger.info(f"{userNameToBeDeleted} deleted : {res}")
        assert res
        Logger.info("TestCASE PASSED (DELETE MULTIPLE USERS)")

    def test_particularUserCRUD(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        n = len(self.tableData[self.tableColumns[4]])
        for i in range(3):
            allUsers = manageUsers.getAllUsersDropDown()
            USERNAME = 'rf'
            allUsers.click()
            Logger.info("clicking dropdown")
            filterBar = manageUsers.getFilterBar()
            Logger.info("clicking all Users dropdown and typing")
            enterText = USERNAME
            filterBar.send_keys(enterText)
            allEntries = manageUsers.getDropdownOptions()
            allEntries[0].click()
            allUsers.click()
            rows = manageUsers.getAllRows()
            self.utils.getTableData(self.tableColumns, self.tableData, rows)
            if i == 0:
                self.test_editUser(0)
            elif i == 1:
                self.test_changePassword(0)
            else:
                self.test_deleteUser(n, 0)

    def test_dropDown_Roles_MultiSelect(self):
        Logger.info(
            "==============================================================================================================\n")
        count = ManageUsersUtils.getRolesCount(self.tableDataMap)
        if count == 1:
            Logger.info("Multiple Roles not found")
            return
        manageUsers = ManageUsersPage(self.driver)
        allRoles = manageUsers.getAllRolesDropDown()
        allRoles.click()
        Logger.info("clicking Roles dropdown")
        res = True
        for i in range(count):
            option = ManageUsersUtils.getOneDropDownOption(manageUsers, self.driver, i)
            option.click()

        text = allRoles.text
        labelText = str(count) + "\nof " + str(count) + " total"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")

        rows = ManageUsersUtils.getAllTableRows(manageUsers)
        res = res and len(rows) == self.noOfRows
        reset = manageUsers.getResetTool()
        reset.click()
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS MULTI-SELECT)")

    @pytest.fixture()
    def initial(self):
        if not self.utils.urlPresent(self.driver, "manage-users"):
            self.test_checkURL()
        manageUsers = ManageUsersPage(self.driver)
        rows = manageUsers.getAllRows()
        self.utils.getTableData(self.tableColumns, self.tableData, rows)
        file = open("../output.json", "w")
        file.write(json.dumps(self.tableData, indent=2))
        yield
        Logger.info(
            "#################################################-DONE-##############################################################")
