import json
import copy
import time

import pytest
from random import randrange
import math

from Pages.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass
from Pages.ManageUsersPage import ManageUsersPage
from Utilities import Logger
from dataSet.ManageUsersData import ManageUsersData


@pytest.mark.usefixtures("initial")
class TestManageUsers(BaseClass):
    driver = None
    tableDataMap = {}
    noOfRows = 0
    newUserAdded = []
    tableColumns = ManageUsersData.TABLE_COLUMNS
    URL = ManageUsersData.URL
    AddUserBtnText = ManageUsersData.ADD_USER_BTN
    ChangePasswordBtnBtn = ManageUsersData.CHANGE_PASSWORD_BTN
    EditBtnText = ManageUsersData.EDIT_BTN
    DeleteBtnText = ManageUsersData.DELETE_BTN
    Roles = ManageUsersData.ROLES
    userFields = ManageUsersData.NEW_USERS_FIELDS
    editFields = ManageUsersData.EDIT_USERS_FIELDS
    changePwdFields = ManageUsersData.CHANGE_PWD_USERS_FIELDS

    def test_checkURL(self, userName='admin', password='admin'):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        res = manageUsers.loginWithAdmin(manageUsers, userName, password)
        assert res
        Logger.info("TestCASE PASSED (CHECK URL)")

    # def test_anyColumn_Sorted(self):
    #     Logger.info(
    #         "==============================================================================================================\n")
    #     manageUsers = ManageUsersPage(self.driver)
    #     fn = manageUsers.LastNameClick()
    #     fn.click()
    #     fn.click()
    #     sortingStatus = manageUsers.checkColumnSorted(manageUsers)
    #     if len(sortingStatus) != 0:
    #         columnNo = sortingStatus[0]
    #         sortingType = sortingStatus[1]
    #         manageUsers.sortTable(self.tableDataMap, columnNo, sortingType, self.noOfRows, self.tableColumns)
    #         sortedTable = copy.deepcopy(self.tableDataMap)
    #         Logger.debug(f"{sortedTable}")
    #         rows = manageUsers.getAllTableRows(manageUsers)
    #         manageUsers.getTableData(self.tableColumns, self.tableDataMap, rows)
    #         Logger.debug(f"{self.tableDataMap}")
    #         res = sortedTable == self.tableDataMap
    #         assert res
    #         Logger.info(f"Table Data is acc to sorting : {res}")
    #     Logger.info("TestCASE PASSED (ANY COLUMN SORTING)")

    # def test_testing(self):
    #     manageUsers = ManageUsersPage(self.driver)
    #     btn = manageUsers.LastNameClick()
    #
    #     manageUsers.sortTable(self.tableDataMap, 2, 1, self.noOfRows, self.tableColumns)
    #     Logger.info(f"{self.tableDataMap}")
    #     btn.click()
    #     rows = manageUsers.getAllRows()
    #     manageUsers.getTableData(self.tableColumns, self.tableDataMap, rows)
    #     Logger.info(f"{self.tableDataMap}")
    #     manageUsers.sortTable(self.tableDataMap, 2, 0, self.noOfRows, self.tableColumns)
    #     Logger.info(f"{self.tableDataMap}")
    #     btn.click()
    #     rows = manageUsers.getAllRows()
    #     manageUsers.getTableData(self.tableColumns, self.tableDataMap, rows)
    #     Logger.info(f"{self.tableDataMap}")
    #
    # def test_sortColumns(self):
    #     Logger.info(
    #         "==============================================================================================================\n")
    #     res = True
    #     manageUsers = ManageUsersPage(self.driver)
    #     listItem = [manageUsers.UserNameClick(), manageUsers.FirstNameClick(), manageUsers.LastNameClick(),
    #                 manageUsers.EmailClick(), manageUsers.RoleNameClick()]
    #     noOfColumns = len(listItem)
    #     Logger.info(f"getting all columns to be sorted: {noOfColumns}")
    #     sortingCol = manageUsers.checkColumnSorted(manageUsers)
    #     idx = -1
    #     type = -1
    #     if len(sortingCol) != 0:
    #         idx = sortingCol[0]
    #         type = sortingCol[1]
    #         Logger.info("SORTING EXIST ON: " + str(idx) + " COLUMN")
    #     for i in range(noOfColumns):
    #         if idx == i:
    #             Logger.info(str(i) + "th Column which is sorted earlier as :" + str(sortingCol[1]))
    #             for j in range(2):
    #                 Logger.debug("Check sort for " + str(i) + "th Column in: " + str((type + j + 1) % 2) + " type*")
    #                 res = res and manageUsers.sortClick(manageUsers, self.tableDataMap, self.tableColumns, i,
    #                                                          (type + j + 1) % 2,
    #                                                          listItem[i], self.noOfRows)
    #         else:
    #             for j in range(2):
    #                 Logger.debug("Check sort for " + str(i) + "th Column in: " + str(1 - j) + " type")
    #                 res = res and manageUsers.sortClick(manageUsers, self.tableDataMap, self.tableColumns, i,
    #                                                          1 - j,
    #                                                          listItem[i], self.noOfRows)
    #     assert res
    #     Logger.info("TestCASE PASSED (TEST SORT COLUMNS)")

    # def test_addNewUser_NewEntryAdded_ColumnUnSorted(self):
    #     Logger.info(
    #         "==============================================================================================================\n")
    #     manageUsers = ManageUsersPage(self.driver)
    #     userName = manageUsers.UserNameClick()
    #     userName.click()
    #
    #     ans = manageUsers.checkColumnSorted(manageUsers)
    #     print(ans)
    # TODO: Sorting add new user
    # TODO: test sort columns
    # TODO: Sorting on any col or not
    def test_addUserBtn_Modal(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        manageUsers.clickAddUserBtn(manageUsers)
        # TODO
        res = manageUsers.isElementPresent()
        Logger.info(f"modal is visible: {res}")
        addUserBtn = manageUsers.getAddNewUser()
        cancelBtn = manageUsers.getCancel()
        Logger.info("getting add new user & cancel btn")
        res = res and manageUsers.isAttrInElement(
            "disabled", "class", addUserBtn)
        Logger.info(f"addNew User btn is disabled: {res}")
        Logger.info("clicking cancel Btn")
        cancelBtn.click()
        res = (res and not manageUsers.isElementPresent())
        Logger.info(f"Modal removed: {res}")
        assert res
        Logger.info("TestCASE PASSED (ADD USER AND CANCEL BUTTON)")

    def test_addNewUser_Fields(self, addUserData):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        res = True
        errors = False
        empty = False
        userData = addUserData
        for keys in userData:
            value = userData[keys]
            if value == '':
                Logger.info(f"{keys} empty")
                empty = True
        username = userData[self.userFields[0]]
        firstname = userData[self.userFields[1]]
        lastname = userData[self.userFields[2]]
        email = userData[self.userFields[3]]
        role = userData[self.userFields[4]]
        pwd = userData[self.userFields[5]]
        retypepwd = userData[self.userFields[6]]
        newUser = manageUsers.NewUser(manageUsers)
        newUser.setUserName(username)
        newUser.setFirstName(firstname)
        newUser.setLastName(lastname)
        selectedRole = newUser.setRole(role)
        newUser.setEmail(email)
        newUser.setPassword(pwd)
        newUser.setReTypePassword(retypepwd)
        res = res and selectedRole.lower() == role.lower()
        Logger.info(f"role: {selectedRole} selected :{res}")
        errorFields = manageUsers.isElementsPresent(
            manageUsers.errorFields)
        addNewUser = manageUsers.getAddNewUser()
        if len(errorFields) != 0 or empty:
            errors = True
            for ele in errorFields:
                Logger.error(ele.text)
            res = res and (errors or empty)
            Logger.error(f"Fields validated Failed: {errors}")
            res = res and (manageUsers.isAttrInElement(
                "disabled", "class", addNewUser))
            Logger.info(f"add new User btn disabled: {res}")

        else:
            Logger.info(f"All Fields validated: {not errors}")
            res = res and not manageUsers.isAttrInElement(
                "disabled", "class", addNewUser)
            Logger.info(f"add new User btn enabled: {res}")
        assert res
        Logger.info("TestCASE PASSED (ADD NEW USER FIELDS VALIDATE)")

    def test_addNewUser_NewEntry(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        manageUsers.clickAddUserBtn(manageUsers)
        res = True
        userData = ['gf', 'gf', 'gh', 'e@gmail.com',
                    'Read only', '123456', '123456']
        username = userData[0]
        firstname = userData[1]
        lastname = userData[2]
        email = userData[3]
        role = userData[4]
        pwd = userData[5]
        retypepwd = userData[6]
        newUser = manageUsers.NewUser(manageUsers)
        newUser.setUserName(username)
        newUser.setFirstName(firstname)
        newUser.setLastName(lastname)
        newUser.setRole(role)
        newUser.setEmail(email)
        newUser.setPassword(pwd)
        newUser.setReTypePassword(retypepwd)
        addNewUser = manageUsers.getAddNewUser()
        sizeBefore = self.noOfRows
        Logger.info("Entered All Details")
        addNewUser.click()
        Logger.info("Add Button Clicked")
        time.sleep(3)
        res = res and not manageUsers.isElementPresent()
        Logger.info(f"Modal removed: {res}")
        rows = manageUsers.getAllRows()
        manageUsers.getTableData(
            self.tableColumns, self.tableDataMap, rows)
        sizeAfter = len(self.tableDataMap[self.tableColumns[4]])
        Logger.info(
            "getting no of rows before adding new entry: " + str(sizeBefore))
        res = res and (sizeAfter == sizeBefore + 1)
        Logger.info("getting no of rows before adding new entry: " +
                    str(sizeAfter) + " :" + str(res))
        values = userData
        Logger.debug("Updated Values to Add in Map: " + str(values))
        Logger.info("setting new entry in tableDataMap")
        manageUsers.addInTable(self.tableDataMap, self.tableColumns, values)
        # if len(sortedColumn) != 0:
        #     colNo = sortedColumn[0]
        #     type = sortedColumn[1]
        #     Logger.info("Sorted Column : " + self.tableColumns[colNo])
        #     Logger.info("Sorting Type :" + str(type))
        #     Logger.debug("0: Inc , 1: Dec")
        #     manageUsers.sortTable(self.tableDataMap, colNo, type, sizeAfter)
        #     sortedTableData = self.tableDataMap
        #     Logger.info("Getting Sorted TableData :" + str(sortedTableData))
        #     rows = manageUsers.getAllRows()
        #     manageUsers.getTableData(self.tableColumns, self.tableDataMap, rows)
        #     Logger.info("Getting All Sorted Rows")
        #     tableDataMap = self.tableDataMap
        #     res = res and (tableDataMap == sortedTableData)
        #     Logger.info("All rows are sorted after adding new Entry: " + str(res))
        file = open("../output.json", "a")
        file.write(json.dumps(values))
        file.write(json.dumps(self.tableDataMap, indent=2))
        # TODO: check Row Data Matched

        # fn = manageUsers.FirstNameClick()
        # # self.sortClick(1, 1, fn)
        # # self.sortClick(1, 0, fn)
        # # Logger.info("DATA ENTRY VERIFIED AFTER SORTING COLUMNS")
        # Logger.info("NEW USER ADDED SUCCESSFULLY")
        # loginPage.enterCredentials(self.newUsers[size - 1][self.userFields[0]],
        #                            self.newUsers[size - 1][self.userFields[0]])
        loginPage = LoginPage(self.driver)
        loginPage.Logout()
        userName = username
        password = pwd
        if role == 'Admin':
            res = res and manageUsers.loginWithAdmin(manageUsers, userName,
                                                     password)
        else:
            res = res and manageUsers.loginWithNonAdmin(manageUsers, userName,
                                                        password)
        Logger.info(f"Login with newly added user: {res}")
        loginPage = LoginPage(self.driver)
        loginPage.Logout()
        assert res
        Logger.info("TestCASE PASSED (ADD NEW USER)")

    def test_editOptions_Modal(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        idx = randrange(self.noOfRows)
        Logger.info(f"row choose: {idx}")
        manageUsers.selectOne(manageUsers, idx)
        row = manageUsers.getTableOneRow(manageUsers, idx)
        editBtn = manageUsers.getEditOptions()[1]
        editBtn.click()
        Logger.info("edit btn clicked")
        res = manageUsers.isElementPresent()
        Logger.info(f"Modal appeared: {res}")
        cancelBtn = manageUsers.getCancel()
        cancelBtn.click()
        Logger.info("clicking cancel btn")
        res = res and not manageUsers.isElementPresent()
        Logger.info(f"Modal removed: {res}")
        res = res and manageUsers.isAttrInElement("selected", "class", row)
        Logger.info("row " + str(idx) + " is still selected: " + str(res))
        manageUsers.selectOne(manageUsers, idx)

        assert res
        Logger.info("TestCASE PASSED (EDIT USER CANCEL BTN)")

    def test_selectAllCheckBox_Clickable(self):
        Logger.info(
            "==============================================================================================================\n")
        res = True
        manageUsers = ManageUsersPage(self.driver)
        manageUsers.selectAllCheckBox(manageUsers)
        isCheckIconPresent = manageUsers.isElementPresent(
            manageUsers.checkIcon)
        res = res and isCheckIconPresent
        Logger.info(f"checkIcon present : {res}")
        manageUsers.selectAllCheckBox(manageUsers)
        isCheckIconPresent = manageUsers.isElementPresent(
            manageUsers.checkIcon)
        assert res and not isCheckIconPresent
        Logger.info(f"checkIcon not present : {res}")
        Logger.info("TestCASE PASSED (SELECT ALL CLICKABLE)")

    def test_selectAllCheckBox_LabelText(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        labelTextInit = manageUsers.getLabelText()
        Logger.info(f"getting initial label text: {labelTextInit}")
        initStr = manageUsers.labelTextUnselected(self.noOfRows)
        res = (labelTextInit == initStr)
        Logger.info(f"labelText is correct : {initStr}  :  {res}")
        manageUsers.selectAllCheckBox(manageUsers)
        labelTextFinal = manageUsers.getLabelText()
        Logger.info(f"getting label text after selection: {labelTextFinal}")
        textAfter = manageUsers.labelTextAllSelected(self.noOfRows)
        res = res and (labelTextFinal == textAfter)
        Logger.info(
            f"label Text matched after selectAll:  {textAfter} : {res}")
        manageUsers.selectAllCheckBox(manageUsers)
        labelTextEnd = manageUsers.getLabelText()
        Logger.info(f"getting label text after deselecting: {labelTextEnd}")
        endStr = manageUsers.labelTextUnselected(self.noOfRows)
        res = res and endStr == labelTextEnd
        Logger.info(
            f"label Text matched after deselect selectAll:  {endStr} : {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT ALL LABEL TEXT)")

    def test_selectAllCheckBox_rowsSelected(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        manageUsers.selectAllCheckBox(manageUsers)
        rows = manageUsers.getAllTableRows(manageUsers)
        res = manageUsers.isAttrInAllElements('selected', 'class', rows)
        Logger.info(f"all rows are selected: {res}")
        checkBoxes = manageUsers.isElementsPresent(manageUsers.checkIconRow)
        isChecked = len(checkBoxes)
        res = res and isChecked == self.noOfRows
        Logger.info(f"all rows checkboxes are selected: {res}")
        manageUsers.selectAllCheckBox(manageUsers)
        rows = manageUsers.getAllTableRows(manageUsers)
        res = res and not manageUsers.isAttrInAllElements(
            'selected', 'class', rows)
        Logger.info(f"all rows are de-selected: {res}")
        checkBoxes = manageUsers.isElementsPresent(manageUsers.checkIconRow)
        isChecked = len(checkBoxes)
        res = res and isChecked == 0
        Logger.info(f"all rows checkboxes are de-selected: {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT ALL , ALL ROWS SELECTED)")

    def test_selectOneRow_Clickable(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        index = randrange(self.noOfRows)
        Logger.info(f"no of rows to be selected is: {index}")
        manageUsers.selectOne(manageUsers, index)
        isPartial = manageUsers.isElementPresent(
            manageUsers.partialCheckIcon)
        res = isPartial
        Logger.info(f"Partial symbol in selectAll present: {res}")
        isChecked = manageUsers.isElementPresent(
            manageUsers.checkIconRow)
        res = res and isChecked
        Logger.info(f"checkbox selected : {res}")
        manageUsers.selectOne(manageUsers, index)
        isPartial = manageUsers.isElementPresent(
            manageUsers.partialCheckIcon)
        res = res and not isPartial
        Logger.info(f"Partial symbol removed in selectAll present: {res}")
        isChecked = manageUsers.isElementPresent(
            manageUsers.checkIconRow)
        res = res and not isChecked
        Logger.info(f"checkbox de-selected : {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT ONE ROW CLICKABLE)")

    def test_selectOneRow_LabelText(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        index = randrange(self.noOfRows)
        Logger.info(f"row to be selected is: {index}")
        manageUsers.selectOne(manageUsers, index)
        labelText = manageUsers.getLabelText()
        text = manageUsers.labelTextNSelected(1, self.noOfRows)
        res = labelText == text
        Logger.info(f"label text is equal after select:   {text}   : {res}")
        manageUsers.selectOne(manageUsers, index)
        Logger.info(f"deselect checkbox of Row {index}")
        labelText = manageUsers.getLabelText()
        Logger.info("getting labelText after de-select")
        text = manageUsers.labelTextUnselected(self.noOfRows)
        res = res and labelText == text
        Logger.info(f"label text is equal after de-select:   {text}   : {res}")
        Logger.info("TestCASE PASSED (SELECT ONE ROW LABEL TEXT)")

    def test_selectOneRow_RowSelected(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        index = randrange(self.noOfRows)
        Logger.info(f"row to be selected is: {index}")
        manageUsers.selectOne(manageUsers, index)
        row = manageUsers.getTableOneRow(manageUsers, index)
        res = manageUsers.isAttrInElement('selected', 'class', row)
        Logger.info(f"row {index}th is selected: {res}")
        manageUsers.selectOne(manageUsers, index)
        row = manageUsers.getTableOneRow(manageUsers, index)
        res = res and not manageUsers.isAttrInElement('selected', 'class', row)
        Logger.info(f"row {index}th is de-selected: {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT ONE ROW SELECTED)")

    def test_selectHalfRows_Clickable(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        N = math.ceil(self.noOfRows / 2)
        res = True
        Logger.info(f"No. of rows to be selected : {N}")
        for i in range(self.noOfRows):
            if i < N:
                manageUsers.selectOne(manageUsers, i)
                isPartial = manageUsers.isElementPresent(
                    manageUsers.partialCheckIcon)
                res = res and isPartial
                Logger.debug(
                    f"Partial symbol present in selecting a row {i}th : {res}")
                isChecked = manageUsers.isElementsPresent(
                    manageUsers.checkIconRow)
                res = res and len(isChecked) == i + 1
                Logger.debug(f"{i}th row checkbox selected: {res}")
            else:
                isPartial = manageUsers.isElementPresent(
                    manageUsers.partialCheckIcon)
                res = res and isPartial
                isChecked = manageUsers.isElementsPresent(
                    manageUsers.checkIconRow)
                res = res and len(isChecked) == N
                Logger.debug(f"Unselected {i}th row : {res}")

        Logger.info(f"Partial symbol present and checkbox is selected: {res}")

        for i in range(N):
            if i < N:
                manageUsers.selectOne(manageUsers, i)
                isChecked = manageUsers.isElementsPresent(
                    manageUsers.checkIconRow)
                isPartial = manageUsers.isElementPresent(
                    manageUsers.partialCheckIcon)
                length = len(isChecked)
                if i == N - 1:
                    res = res and length == 0
                    res = res and not isPartial
                else:
                    res = res and length == N - i - 1
                    res = res and isPartial
                Logger.debug(f"{i}th row checkbox de-selected: {res}")
            else:
                isPartial = manageUsers.isElementPresent(
                    manageUsers.partialCheckIcon)
                res = res and not isPartial
                isChecked = manageUsers.isElementsPresent(
                    manageUsers.checkIconRow)
                res = res and len(isChecked) == 0
                Logger.debug(f"Unselected {i}th row : {res}")

        Logger.info(
            f"Partial symbol not present and checkbox is de-selected: {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT HALF ROWS CLICKABLE)")

    def test_selectHalfRows_LabelText(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        N = math.ceil(self.noOfRows / 2)
        res = True
        Logger.info(f"No. of rows to be selected : {N}")
        noOfElements = 0
        for i in range(N):
            manageUsers.selectOne(manageUsers, i)
            Logger.debug(f"{i}th row checkbox selected: {res}")
            noOfElements = noOfElements + 1
            labelText = manageUsers.getLabelText()
            Text = manageUsers.labelTextNSelected(noOfElements, self.noOfRows)
            res = res and labelText == Text
            Logger.debug(f"labelText is same: {Text}")
        Logger.info(f"LabelText is same after selecting: {res}")

        for i in range(N):
            manageUsers.selectOne(manageUsers, i)
            Logger.debug(f"{i}th row checkbox de-selected: {res}")
            noOfElements = noOfElements - 1
            labelText = manageUsers.getLabelText()
            if i == N - 1:
                Text = manageUsers.labelTextUnselected(self.noOfRows)
            else:
                Text = manageUsers.labelTextNSelected(
                    noOfElements, self.noOfRows)
            res = res and labelText == Text
            Logger.debug(f"labelText is same: {Text}")

        Logger.info(f"LabelText is same after de-selecting: {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT HALF ROWS LABEL TEXT)")

    def test_selectHalfRows_RowsSelected(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        N = math.ceil(self.noOfRows / 2)
        res = True
        Logger.info(f"No. of rows to be selected : {N}")
        for i in range(self.noOfRows):
            if i < N:
                manageUsers.selectOne(manageUsers, i)
                row = manageUsers.getTableOneRow(manageUsers, i)
                Logger.debug(f"{i}th row checkbox selected: {res}")
                res = (res and manageUsers.isAttrInElement(
                    'selected', 'class', row))
            else:
                row = manageUsers.getTableOneRow(manageUsers, i)
                Logger.debug(f"un-selected {i}th row: {res}")
                res = (res and not manageUsers.isAttrInElement(
                    'selected', 'class', row))

        Logger.info(f"all Half Rows are selected: {res}")

        for i in range(self.noOfRows):
            if i < N:
                manageUsers.selectOne(manageUsers, i)
                Logger.debug(f"{i}th row checkbox de-selected: {res}")
                row = manageUsers.getTableOneRow(manageUsers, i)
                Logger.debug(f"{i}th row checkbox selected: {res}")
                res = (res and not manageUsers.isAttrInElement(
                    'selected', 'class', row))
            else:
                row = manageUsers.getTableOneRow(manageUsers, i)
                Logger.debug(f"un-selected {i}th row: {res}")
                res = (res and not manageUsers.isAttrInElement(
                    'selected', 'class', row))

        Logger.info(f"all Half Rows deselected: {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT HALF ROWS LABEL TEXT)")

    def test_editOptions_LoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        loginUserIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        editOptions = manageUsers.getEditOptions()
        totalEditOptionsBefore = len(editOptions)
        editOptionsText = editOptions[0].text
        res = editOptionsText == self.AddUserBtnText and totalEditOptionsBefore == 1
        Logger.info(
            f"Only 1 Edit: {editOptions} option before selecting row: {res}")
        manageUsers.selectOne(manageUsers, loginUserIndex)
        editOptions = manageUsers.getEditOptions()
        totalEditOptionsAfter = len(editOptions)
        res = res and totalEditOptionsAfter == 3
        Logger.info(
            f"getting all edit options Btn after selecting: {totalEditOptionsAfter} : {res}")
        changePwdBtn = editOptions[0]
        res = res and changePwdBtn.text == self.ChangePasswordBtnBtn
        editBtn = editOptions[1]
        res = res and editBtn.text == self.EditBtnText
        deleteBtn = editOptions[2]
        res = res and deleteBtn.text == self.DeleteBtnText
        Logger.info(f"All edit options btn text matched: {res}")
        res = res and manageUsers.isAttrInElement(
            "disabled", "class", deleteBtn)
        Logger.info(f"for Login user delete btn is disabled:  {res}")
        manageUsers.selectOne(manageUsers, loginUserIndex)
        Logger.info("de-selection")
        assert res
        Logger.info("TestCASE PASSED (EDIT OPTIONS OF LOGIN USER)")

    def test_editOptions_NormalUser(self):
        Logger.info(
            "==============================================================================================================\n")
        if self.noOfRows == 1:
            Logger.info("Normal User Not Available")
            Logger.info("TestCASE PASSED (EDIT OPTIONS OF LOGIN USER)")
            return
        manageUsers = ManageUsersPage(self.driver)
        loginIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        idx = randrange(self.noOfRows)
        if idx == loginIndex:
            idx = (loginIndex + 1) % self.noOfRows
        editOptions = manageUsers.getEditOptions()
        totalEditOptionsBefore = len(editOptions)
        editOptionsText = editOptions[0].text
        res = editOptionsText == self.AddUserBtnText and totalEditOptionsBefore == 1
        Logger.info(
            f"Only 1 Edit: {editOptions} option before selecting row: {res}")
        manageUsers.selectOne(manageUsers, idx)
        editOptions = manageUsers.getEditOptions()
        totalEditOptionsAfter = len(editOptions)
        res = res and totalEditOptionsAfter == 3
        Logger.info(
            f"getting all edit options Btn after selecting: {totalEditOptionsAfter} : {res}")
        changePwdBtn = editOptions[0]
        res = res and changePwdBtn.text == self.ChangePasswordBtnBtn
        editBtn = editOptions[1]
        res = res and editBtn.text == self.EditBtnText
        deleteBtn = editOptions[2]
        res = res and deleteBtn.text == self.DeleteBtnText
        Logger.info(f"All edit options btn text matched: {res}")
        res = res and not manageUsers.isAttrInElement(
            "disabled", "class", deleteBtn)
        Logger.info(f"for Normal user delete btn is enabled:  {res}")
        manageUsers.selectOne(manageUsers, idx)
        Logger.info("de-selection")
        assert res
        Logger.info("TestCASE PASSED (EDIT OPTIONS OF NON-LOGIN USER)")

    def test_editOptions_MultiSelect_IncludingLoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        if self.noOfRows == 1:
            Logger.info(f"MultiSelection Not Possible: only 1 User")
            self.test_editOptions_LoginUser()
            Logger.info(
                "TestCASE PASSED (EDIT OPTIONS AFTER MULTIPLE SELECTIONS INCLUDING LOGIN USER)")
            return
        res = True
        manageUsers = ManageUsersPage(self.driver)
        loginUserIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        manageUsers.selectOne(manageUsers, loginUserIndex)
        Index2 = (loginUserIndex + 1) % self.noOfRows
        manageUsers.selectOne(manageUsers, Index2)
        editOptions = manageUsers.getEditOptions()
        btnCount = len(editOptions)
        res = res and btnCount == 3
        Logger.info(f"count of btn is : {btnCount} : {res}")
        for ele in editOptions:
            res = res and manageUsers.isAttrInElement("disabled", "class", ele)
        Logger.info(
            f"all edit options are disabled after multiple selection: {res}")
        manageUsers.selectOne(manageUsers, Index2)
        manageUsers.selectOne(manageUsers, loginUserIndex)
        Logger.info("de-selection")
        assert res
        Logger.info(
            "TestCASE PASSED (EDIT OPTIONS AFTER MULTIPLE SELECTIONS INCLUDING LOGIN USER)")

    def test_editOptions_MultiSelect_ExcludingLoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        if self.noOfRows == 1:
            Logger.info(
                f"MultiSelection Not Possible: only 1 User (ONLY LOGIN USER)")
            self.test_editOptions_LoginUser()
            Logger.info(
                "TestCASE PASSED (EDIT OPTIONS AFTER MULTIPLE SELECTIONS EXCLUDING LOGIN USER)")
            return
        res = True
        manageUsers = ManageUsersPage(self.driver)
        loginUserIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        Index1 = loginUserIndex
        skipped = 1
        if self.noOfRows > 2:
            Logger.info("Login User Row Skipped")
            Index1 = (loginUserIndex - 1) % self.noOfRows
        else:
            skipped = 0
            Logger.info("Login User Row included")
        manageUsers.selectOne(manageUsers, Index1)
        Index2 = (loginUserIndex + 1) % self.noOfRows
        manageUsers.selectOne(manageUsers, Index2)
        editOptions = manageUsers.getEditOptions()
        btnCount = len(editOptions)
        res = res and btnCount == 3
        Logger.info(f"count of btn is : {btnCount} : {res}")
        for i in range(len(editOptions) - skipped):
            ele = editOptions[i]
            res = res and manageUsers.isAttrInElement("disabled", "class", ele)
        if skipped == 1:
            res = res and not manageUsers.isAttrInElement(
                "disabled", "class", editOptions[2])
            Logger.info(
                f"all edit options are disabled except delete btn after multiple selection: {res}")
        else:
            Logger.info(
                f"all edit options are disabled after multiple selection: {res}")
        manageUsers.selectOne(manageUsers, Index2)
        manageUsers.selectOne(manageUsers, Index1)
        Logger.info("de-selection")
        assert res
        Logger.info(
            "TestCASE PASSED (EDIT OPTIONS AFTER MULTIPLE SELECTIONS INCLUDING LOGIN USER)")

    def test_editOptions_Fields(self, editUserData):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        loginUserIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        idx = randrange(self.noOfRows)
        manageUsers.selectOne(manageUsers, idx)
        disableItem = 1
        if idx == loginUserIndex:
            disableItem = 2
        editBtn = manageUsers.getEditOptions()[1]
        editBtn.click()
        Logger.info("Edit btn clicked")
        res = True
        errors = False
        empty = False
        userData = editUserData
        for keys in userData:
            value = userData[keys]
            if value == '':
                Logger.info(f"{keys} empty")
                empty = True
        Logger.info("getting all disabled fields")
        disabledEle = manageUsers.getDisabled()
        noOfDisabled = len(disabledEle)
        res = res and noOfDisabled == disableItem
        Logger.debug(f"{disableItem}")
        firstname = userData[self.editFields[0]]
        lastname = userData[self.editFields[1]]
        email = userData[self.editFields[2]]
        if noOfDisabled != 2:
            role = userData[self.editFields[3]]
        newUser = manageUsers.NewUser(manageUsers)
        newUser.setFirstName(firstname)
        newUser.setLastName(lastname)
        if noOfDisabled != 2:
            selectedRole = newUser.setRole(role)
            res = res and selectedRole.lower() == role.lower()
            Logger.info(f"role: {selectedRole} selected :{res}")
        else:
            Logger.info("role dropdown disabled")
        newUser.setEmail(email)
        errorFields = manageUsers.isElementsPresent(
            manageUsers.errorFields)
        updateBtn = manageUsers.getUpdate()
        if len(errorFields) != 0 or empty:
            errors = True
            for ele in errorFields:
                Logger.error(ele.text)
            res = res and (errors or empty)
            Logger.error(f"Fields validated Failed: {errors}")
            res = res and (manageUsers.isAttrInElement(
                "disabled", "class", updateBtn))
            Logger.info(f"edit User btn disabled: {res}")

        else:
            Logger.info(f"All Fields validated: {not errors}")
            res = res and not manageUsers.isAttrInElement(
                "disabled", "class", updateBtn)
            Logger.info(f"Edit User btn enabled: {res}")
        cancelBtn = manageUsers.getCancel()
        cancelBtn.click()
        manageUsers.selectOne(manageUsers, idx)
        assert res
        Logger.info("TestCASE PASSED (EDIT USER FIELDS VALIDATE)")

    def test_editUser_LoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        loginUserIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        manageUsers.selectOne(manageUsers, loginUserIndex)
        res = True
        editBtn = manageUsers.getEditOptions()[1]
        editBtn.click()
        Logger.info("Edit btn clicked")
        updatebtn = manageUsers.getUpdate()
        Logger.info("getting update user btn")
        disabledEle = manageUsers.getDisabled()
        Logger.info("getting all disabled fields")
        noOfDisabled = len(disabledEle)
        res = res and (noOfDisabled == 2)
        Logger.info("no of disabled elements is: " +
                    str(noOfDisabled) + " :" + str(res))
        newUser = manageUsers.NewUser(manageUsers)
        FN = "updatedFN"
        LN = "upadatedLN"
        EM = "update@test.com"
        RO = newUser.roleDropDown().text
        newUser.setFirstName(FN)
        newUser.setLastName(LN)
        newUser.setEmail(EM)
        Logger.info("entering all fields: " + FN +
                    "  " + LN + " " + EM + " " + RO)
        updatedValues = [FN, LN, EM, RO]
        Logger.info("updated values: " + str(updatedValues))
        updatebtn.click()
        Logger.info("clicking update btn and waiting..")
        time.sleep(4)
        res = res and not manageUsers.isElementPresent()
        Logger.info(f"Modal removed: {res}")
        row = manageUsers.getTableOneRow(
            manageUsers, loginUserIndex)
        val = manageUsers.getIthRowFromTable(row)
        Logger.info("getting data from row: " + str(val))
        for i in range(1, len(self.tableColumns)):
            key = self.tableColumns[i]
            newVal = updatedValues[i - 1]
            manageUsers.updateTableRow(
                self.tableDataMap, newVal, key, loginUserIndex)
            Logger.info("updated key and val: " +
                        str(key) + " -> " + str(newVal))

        Logger.info("update in tableDataMap")
        rowUpdated = manageUsers.getIthRowFromTable(row)
        res = res and (not manageUsers.isAttrInElement(
            "selected", "class", row))
        Logger.info("selected row " + str(loginUserIndex) +
                    " is unselected: " + str(res))
        assert res and (val == rowUpdated)
        Logger.info("selected row " + str(loginUserIndex) +
                    " is updated: " + str(res))
        Logger.info("TestCASE PASSED (EDIT LOGIN USER)")

    def test_editUser_NonLoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        if self.noOfRows == 1:
            Logger.info("Non Login user not found")
            return
        loginIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        idx = randrange(self.noOfRows)
        if idx == loginIndex:
            idx = (loginIndex + 1) % self.noOfRows
        Logger.info("row No. : " + str(idx) + " choose")
        res = True
        manageUsers.selectOne(manageUsers, idx)
        editBtn = manageUsers.getEditOptions()[1]
        editBtn.click()
        Logger.info("Edit btn clicked")
        updatebtn = manageUsers.getUpdate()
        newUser = manageUsers.NewUser(manageUsers)
        FN = "updatedFN"
        LN = "upadatedLN"
        EM = "update@test.com"
        disabledEle = manageUsers.getDisabled()
        noOfDisabled = len(disabledEle)
        res = res and (noOfDisabled == 1)
        Logger.info(f"disabled fields: 1 : {res} ")
        newUser.setFirstName(FN)
        newUser.setLastName(LN)
        newUser.setEmail(EM)
        newUser.setRole('admin')
        RO = newUser.roleDropDown().text
        Logger.info("entering all fields: " + FN +
                    "  " + LN + " " + EM + " " + RO)
        updatedValues = [FN, LN, EM, RO]
        Logger.info("updated values: " + str(updatedValues))
        updatebtn.click()
        Logger.info("clicking update btn and waiting..")
        time.sleep(4)
        res = res and not manageUsers.isElementPresent()
        Logger.info(f"Modal removed: {res}")
        row = manageUsers.getTableOneRow(manageUsers, idx)
        val = manageUsers.getIthRowFromTable(row)
        Logger.info("getting data from row: " + str(val))
        for i in range(1, len(self.tableColumns)):
            key = self.tableColumns[i]
            newVal = updatedValues[i - 1]
            manageUsers.updateTableRow(self.tableDataMap, newVal, key, idx)
            Logger.info("updated key and val: " +
                        str(key) + " -> " + str(newVal))

        Logger.info("update in tableDataMap")
        rowUpdated = manageUsers.getIthRowFromTable(row)
        res = res and (not manageUsers.isAttrInElement(
            "selected", "class", row))
        Logger.info("selected row " + str(idx) + " is unselected: " + str(res))
        assert res and (val == rowUpdated)
        Logger.info("selected row " + str(idx) + " is updated: " + str(res))
        Logger.info("TestCASE PASSED (EDIT LOGIN USER)")

    def test_changePassword_Modal(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        idx = randrange(self.noOfRows)
        manageUsers.selectOne(manageUsers, idx)
        Logger.info(f"row choose: {idx}")
        changePasswordBtn = manageUsers.getEditOptions()[0]
        changePasswordBtn.click()
        Logger.info("clicking change password btn")
        res = manageUsers.isElementPresent()
        Logger.info(f"Modal opened: {res}")
        changePwd = manageUsers.getChangePassword()
        disabledEle = manageUsers.getDisabled()
        noOfDisabled = len(disabledEle)
        res = res and (noOfDisabled == 1)
        Logger.info(f"disabled fields: 1 : {res} ")
        res = res and manageUsers.isAttrInElement(
            "disabled", "class", changePwd)
        Logger.info("update password btn is disabled: " + str(res))
        cancelBtn = manageUsers.getCancel()
        cancelBtn.click()
        Logger.info("clicking cancel btn")
        res = res and not manageUsers.isElementPresent()
        Logger.info(f"Modal removed: {res}")
        manageUsers.selectOne(manageUsers, idx)
        assert res
        Logger.info("TestCASE PASSED (CHANGE PASSWORD MODAL)")

    def test_changePassword_fields(self, editPwdUserData):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        idx = randrange(self.noOfRows)
        manageUsers.selectOne(manageUsers, idx)
        Logger.info(f"row choose: {idx}")
        changePasswordBtn = manageUsers.getEditOptions()[0]
        changePasswordBtn.click()
        Logger.info("clicking change password btn")
        res = True
        errors = False
        empty = False
        userData = editPwdUserData
        for keys in userData:
            value = userData[keys]
            if value == '':
                Logger.info(f"{keys} empty")
                empty = True
        changePwd = manageUsers.getChangePassword()
        newUser = manageUsers.NewUser(manageUsers)
        pwd = userData[self.userFields[5]]
        repwd = userData[self.userFields[6]]
        newUser.setPassword(pwd)
        newUser.setReTypePassword(repwd)
        errorFields = manageUsers.isElementsPresent(
            manageUsers.errorFields)
        if len(errorFields) != 0 or empty:
            errors = True
            for ele in errorFields:
                Logger.error(ele.text)
            res = res and (errors or empty)
            Logger.error(f"Fields validated Failed: {errors}")
            res = res and (manageUsers.isAttrInElement(
                "disabled", "class", changePwd))
            Logger.info(f"change pwd btn disabled: {res}")

        else:
            Logger.info(f"All Fields validated: {not errors}")
            res = res and not manageUsers.isAttrInElement(
                "disabled", "class", changePwd)
            Logger.info(f"change pwd btn enabled: {res}")
        cancelBtn = manageUsers.getCancel()
        cancelBtn.click()
        selectedRow = manageUsers.getTableOneRow(manageUsers, idx)
        res = res and manageUsers.isAttrInElement(
            "selected", "class", selectedRow)
        Logger.info("selected row: " + str(idx) + " is selected: " + str(res))
        manageUsers.selectOne(manageUsers, idx)
        Logger.info("deselecting checkbox")
        assert res
        Logger.info("TestCASE PASSED (CHANGE PASSWORD FIELDS)")

    def test_changePassword_LoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        loginUser = manageUsers.getLoggedInUser()
        loginUserIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        manageUsers.selectOne(manageUsers, loginUserIndex)
        changePasswordBtn = manageUsers.getEditOptions()[0]
        changePasswordBtn.click()
        Logger.info("clicking change password btn")
        data = ["admin", "admin"]
        newUser = manageUsers.NewUser(manageUsers)
        newUser.setPassword(data[0])
        newUser.setReTypePassword(data[1])
        changePwdBtn = manageUsers.getChangePassword()
        changePwdBtn.click()
        Logger.info("clicking changePwd btn")
        time.sleep(6)
        res = manageUsers.urlPresent("login")
        Logger.info("Login page arrived: " + str(res))
        res = res and manageUsers.loginWithAdmin(
            manageUsers, loginUser, data[0])
        Logger.info("ManageUsers Page page arrived: ")
        assert res
        Logger.info("TestCASE PASSED (PASSWORD CHANGE LOGIN USER)")

    def test_changePassword_NonLoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        if self.noOfRows == 1:
            Logger.info("Non login User not found")
            return
        manageUsers = ManageUsersPage(self.driver)
        loginIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        idx = randrange(self.noOfRows)
        if idx == loginIndex:
            idx = (loginIndex + 1) % self.noOfRows
        userName = manageUsers.getIthColData(self.tableDataMap, 0)[idx]
        role = manageUsers.getIthColData(self.tableDataMap, 4)[idx]
        manageUsers.selectOne(manageUsers, idx)
        changePasswordBtn = manageUsers.getEditOptions()[0]
        changePasswordBtn.click()
        Logger.info("clicking change password btn")
        data = ["admin", "admin"]
        newUser = manageUsers.NewUser(manageUsers)
        newUser.setPassword(data[0])
        newUser.setReTypePassword(data[1])
        changePwdBtn = manageUsers.getChangePassword()
        changePwdBtn.click()
        Logger.info("clicking changePwd btn")
        time.sleep(1)
        res = not manageUsers.isElementPresent()
        Logger.info(f"Modal removed: {res}")
        loginPage = LoginPage(self.driver)
        loginPage.Logout()
        time.sleep(6)
        if role == 'Admin':
            res = res and manageUsers.loginWithAdmin(manageUsers, userName,
                                                     data[0])
        else:
            res = res and manageUsers.loginWithNonAdmin(manageUsers, userName,
                                                        data[0])

        loginPage = LoginPage(self.driver)
        loginPage.Logout()
        assert res
        Logger.info("TestCASE PASSED (PASSWORD CHANGE NON LOGIN USER)")

    def test_dropDown_UserModal(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allUsers = manageUsers.getAllUsersDropDown()
        allUsers.click()
        Logger.info("clicking all Users")
        res = manageUsers.isAttrInElement("visible", "class", allUsers)
        Logger.info(f"Modal is visible: {res}")
        dropdownCount = manageUsers.getDropdownOptions()
        res = res and (len(dropdownCount) == self.noOfRows)
        Logger.info(
            f"No of entries in options are: {len(dropdownCount)} are same as in table: {self.noOfRows} : {res}")
        allUsers.click()
        Logger.info("deselecting allUsers")
        res = res and (not manageUsers.isAttrInElement(
            "visible", "class", allUsers))
        Logger.info(f"Modal removed: {res}")
        assert res
        Logger.info("TestCASE PASSED (ALL USERS DROPDOWN MODAL)")

    # TODO add in excel
    def test_dropdown_User_Reset(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allUsers = manageUsers.getAllUsersDropDown()
        allUsers.click()
        Logger.info("clicking dropdown")
        filterCheckBox = manageUsers.getFilterCheckBox()
        filterCheckBox.click()
        res = True
        Logger.info("select All checkbox clicked")
        resetBtn = manageUsers.getResetTool()[1]
        resetBtn.click()
        Logger.info("reset btn clicked")
        res = res and (not manageUsers.isAttrInElement(
            "visible", "class", allUsers))
        Logger.info(f"Modal removed: {res}")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS RESET)")

    def test_dropdown_User_FilterController(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allUsers = manageUsers.getAllUsersDropDown()
        allUsers.click()
        Logger.info("clicking User dropdown")
        filterCheckBox = manageUsers.getFilterCheckBox()
        filterCheckBox.click()
        Logger.info("select All checkbox clicked")
        filterController = manageUsers.getFilterController()
        controllerLen = len(filterController)
        res = controllerLen == 2
        Logger.info(f"filter count is 2: {res}")
        reset = manageUsers.getFilterController()[1]
        reset.click()
        Logger.info("Filter controller cancel btn clicked")
        res = res and (not manageUsers.isAttrInElement(
            "visible", "class", allUsers))
        Logger.info(f"Modal removed: {res}")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS FILTER CONTROLLER)")

    def test_dropDown_User_SelectAll(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allUsers = manageUsers.getAllUsersDropDown()
        allUsers.click()
        Logger.info("clicking User dropdown")
        filterCheckBox = manageUsers.getFilterCheckBox()
        filterCheckBox.click()
        res = manageUsers.isElementPresent(
            manageUsers.dropdownCheckIcon)
        Logger.info(f"checkbox ticked: {res}")
        text = allUsers.text
        labelText = str(self.noOfRows) + "\nof " + \
                    str(self.noOfRows) + " total"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        allEntries = manageUsers.getDropdownOptions()
        activeDropdown = manageUsers.isAttrInElement(
            "active", "class", allUsers)
        res = res and activeDropdown
        Logger.info(f"dropdown is active: {res}")
        for ele in allEntries:
            res = res and (manageUsers.isAttrInElement(
                "selected", "class", ele))
        Logger.info(f"All options of dropdown are selected: {res}")
        filterCheckBox.click()
        res = res and not manageUsers.isElementPresent(
            manageUsers.dropdownCheckIcon)
        Logger.info(f"checkbox de-select: {res}")
        for ele in allEntries:
            res = res and (not manageUsers.isAttrInElement(
                "selected", "class", ele))
        Logger.info(f"All options of dropdown deselected: {res}")
        activeDropdown = manageUsers.isAttrInElement(
            "active", "class", allUsers)
        res = res and not activeDropdown
        Logger.info(f"dropdown is not active: {res}")
        allUsers.click()
        res = res and (not manageUsers.isAttrInElement(
            "visible", "class", allUsers))
        Logger.info(f"Modal removed: {res}")
        text = allUsers.text
        labelText = "All Users"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS SELECT ALL)")

    # TODO: icon check
    def test_dropDown_User_SelectOne(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allUsers = manageUsers.getAllUsersDropDown()
        allUsers.click()
        Logger.info("clicking User dropdown")
        idx = randrange(self.noOfRows)
        option = manageUsers.getOneDropDownOption(
            manageUsers, idx)
        option.click()
        rows = manageUsers.getAllTableRows(manageUsers)
        sizeRow = len(rows)
        res = sizeRow == 1
        Logger.info(f"size of row:{sizeRow} : {res}")
        text = allUsers.text
        labelText = str(1) + "\nof " + str(self.noOfRows) + " total"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        uName = option.text
        uNameIdx = -1
        userNameList = manageUsers.getIthColData(self.tableDataMap, 0)
        for i in range(len(userNameList)):
            if userNameList[i] == uName:
                uNameIdx = i
                break
        Logger.info(f"uName selected: {uName}")
        selectedData = manageUsers.getIthRowsData(self.tableDataMap, uNameIdx)
        manageUsers.getTableData(
            self.tableColumns, self.tableDataMap, rows)
        rowData = manageUsers.getIthRowsData(self.tableDataMap, 0)
        res = res and selectedData == rowData
        Logger.info(f"rowData Matched: {selectedData}:{res}")
        option = manageUsers.getOneDropDownOption(
            manageUsers, idx)
        option.click()
        allUsers.click()
        text = allUsers.text
        labelText = "All Users"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS SELECT ONE)")

    # TODO: for sorted also
    def test_dropDown_User_MultiSelect(self):
        Logger.info(
            "==============================================================================================================\n")
        if self.noOfRows == 1:
            Logger.info("Multiple users not found")
            return
        manageUsers = ManageUsersPage(self.driver)
        mainTableData = copy.deepcopy(self.tableDataMap)
        allUsers = manageUsers.getAllUsersDropDown()
        allUsers.click()
        Logger.info("clicking User dropdown")
        count = 0
        iterations = randrange(1, self.noOfRows)
        Logger.info(f"no of rows selected: {iterations}")
        allUserNames = []
        indexSet = set([])
        res = True
        for i in range(iterations):
            idx = randrange(self.noOfRows)
            idx = manageUsers.getIndex(indexSet, idx, self.noOfRows)
            indexSet.add(idx)
            Logger.debug(f"opt no: {idx}")
            option = manageUsers.getOneDropDownOption(
                manageUsers, idx)
            option.click()
            time.sleep(1)
            count += 1
            text = allUsers.text
            labelText = str(count) + "\nof " + str(self.noOfRows) + " total"
            res = res and labelText == text
            Logger.info(f"label text :{labelText}: {res}")
            rowSize = len(manageUsers.getAllTableRows(manageUsers))
            res = res and rowSize == count
            Logger.info(f"row size: {rowSize}: {res}")
            uName = option.text
            Logger.info(f"uName selected: {uName}")
            allUserNames.append(uName)
            time.sleep(1)
            rows = manageUsers.getAllTableRows(manageUsers)
            userNameData = []
            for idx in indexSet:
                userNameData.append(
                    manageUsers.getIthRowsData(mainTableData, idx))
            manageUsers.getTableData(
                self.tableColumns, self.tableDataMap, rows)
            rows = manageUsers.getAllTableRows(manageUsers)
            for row in rows:
                rowData = manageUsers.getIthRowFromTable(row)
                data = []
                rowUserName = rowData[0]
                for idx in range(len(userNameData)):
                    username = userNameData[idx][0]
                    if username == rowUserName:
                        data = userNameData[idx]
                        break
                res = res and data == rowData
                Logger.debug(f"{res} : {data}")
                Logger.debug(f"{res} :{rowData}")
        Logger.info(f"rowData Matched:{res}")

        for idx in indexSet:
            option = manageUsers.getOneDropDownOption(
                manageUsers, idx)
            option.click()
            time.sleep(1)
            text = allUsers.text
            count -= 1
            labelText = str(count) + "\nof " + str(self.noOfRows) + " total"
            rowSize = len(manageUsers.getAllTableRows(manageUsers))
            if count == 0:
                labelText = "All Users"
                count = self.noOfRows
            res = res and labelText == text
            Logger.info(f"label Text is equal: {text}: {res}")
            res = res and rowSize == count
            Logger.info(f"row size: {rowSize}: {res}")
        rows = manageUsers.getAllTableRows(manageUsers)
        res = res and len(rows) == self.noOfRows
        Logger.info(f"table all rows restored: {res}")
        assert res
        allUsers = manageUsers.getAllUsersDropDown()
        allUsers.click()
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS MULTI-SELECT)")

    def test_dropDown_User_FilterBar(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allUsers = manageUsers.getAllUsersDropDown()
        allUsers.click()
        res = True
        Logger.info("clicking User dropdown")
        filterBar = manageUsers.getFilterBar()
        enterText = 'z'
        Logger.info(f"typing value in input: {enterText}")
        filterBar.send_keys(enterText)
        NoResult = manageUsers.isElementPresent(manageUsers.noResult)
        if not NoResult:
            allEntries = manageUsers.getDropdownOptions()
            sizeEntries = len(allEntries)
            userNameList = manageUsers.getIthColData(self.tableDataMap, 0)
            count = 0
            Logger.info("checking each options contains the entered value")
            for ele in userNameList:
                if enterText.lower() in ele.lower():
                    count = count + 1
            res = res and count == sizeEntries
            Logger.info(f"no of options: {count} are correct: {res}")
            filterCheckBox = manageUsers.getFilterCheckBox()
            Logger.info(
                "clicking on selectAll checkbox to select only containing username")
            filterCheckBox.click()
            allRows = manageUsers.getAllTableRows(manageUsers)
            Logger.info(
                "getting all rows of which are contains selected options")
            manageUsers.getTableData(
                self.tableColumns, self.tableDataMap, allRows)
            userNameList = manageUsers.getIthColData(self.tableDataMap, 0)
            sizeEntries = len(allEntries)
            res = res and sizeEntries == len(allRows)
            Logger.info(
                f"size of options and rows are equal: {sizeEntries} : {res}")
            for i in range(len(allRows)):
                option = allEntries[i]
                username = userNameList[i]
                res = res and enterText.lower() in option.text.lower()
                res = res and enterText.lower() in username.lower()
            Logger.info(f"All rows and options have common string: {res}")
            filterCheckBox = manageUsers.getFilterCheckBox()
            filterCheckBox.click()
            Logger.info("checkbox deselect")
            lenAfter = len(manageUsers.getDropdownOptions())
            res = res and lenAfter == sizeEntries
            Logger.info(f"size of entries: {lenAfter}")
            sizeAllRows = len(manageUsers.getAllRows())
            res = res and sizeAllRows == self.noOfRows
            Logger.info(
                f"size of rows after deselect checkbox: {sizeAllRows} : {res}")
        else:
            Logger.info("User Not Found")
            rows = manageUsers.getAllTableRows(manageUsers)
            res = res and len(rows) == self.noOfRows
            Logger.info(f"all rows displayed: {len(rows)}: {res}")
        clearTool = manageUsers.getClearTool()
        clearTool.click()
        Logger.info("clearing input")
        removeText = filterBar.text
        res = res and removeText == ''
        Logger.info(f"entered text cleared: {res}")
        allUsers.click()
        Logger.info("dropdown closed")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL USERS FILTER-BAR)")

    def test_dropDown_RolesModal(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allRoles = manageUsers.getAllRolesDropDown()
        allRoles.click()
        Logger.info("clicking all Roles")
        res = manageUsers.isAttrInElement("visible", "class", allRoles)
        Logger.info(f"Modal is visible: {res}")
        count = manageUsers.getRolesCount(self.tableDataMap)
        dropdownCount = manageUsers.getDropdownOptions()
        res = res and (len(dropdownCount) == count)
        Logger.info(
            f"No of different roles in options are: {len(dropdownCount)} are same as in table : {count} : {res}")
        allRoles.click()
        Logger.info("closing allRoles")
        res = res and (not manageUsers.isAttrInElement(
            "visible", "class", allRoles))
        Logger.info(f"Modal removed: {res}")
        assert res
        Logger.info("TestCASE PASSED (ALL ROLES DROPDOWN MODAL)")

    def test_dropDown_Roles_Reset(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allRoles = manageUsers.getAllRolesDropDown()
        allRoles.click()
        Logger.info("clicking Roles dropdown")
        filterCheckBox = manageUsers.getFilterCheckBox()
        filterCheckBox.click()
        res = True
        Logger.info("select All checkbox clicked")
        resetBtn = manageUsers.getResetTool()[0]
        resetBtn.click()
        Logger.info("reset btn clicked")
        res = res and (not manageUsers.isAttrInElement(
            "visible", "class", allRoles))
        Logger.info(f"Modal removed: {res}")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL ROLES RESET)")

    def test_dropdown_Roles_FilterController(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allRoles = manageUsers.getAllRolesDropDown()
        allRoles.click()
        Logger.info("clicking Roles dropdown")
        filterCheckBox = manageUsers.getFilterCheckBox()
        filterCheckBox.click()
        Logger.info("select All checkbox clicked")
        filterController = manageUsers.getFilterController()
        controllerLen = len(filterController)
        res = controllerLen == 2
        Logger.info(f"filter count is {controllerLen}: {res}")
        reset = manageUsers.getFilterController()[1]
        reset.click()
        Logger.info("Filter controller cancel btn clicked")
        res = res and (not manageUsers.isAttrInElement(
            "visible", "class", allRoles))
        Logger.info(f"Modal removed: {res}")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL ROLES FILTER CONTROLLER)")

    def test_dropDown_Roles_SelectAll(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allRoles = manageUsers.getAllRolesDropDown()
        allRoles.click()
        Logger.info("clicking Roles dropdown")
        filterCheckBox = manageUsers.getFilterCheckBox()
        filterCheckBox.click()
        res = manageUsers.isElementPresent(
            manageUsers.dropdownCheckIcon)
        Logger.info(f"checkbox ticked: {res}")
        text = allRoles.text
        count = manageUsers.getRolesCount(self.tableDataMap)
        labelText = str(count) + "\nof " + str(count) + " total"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        allEntries = manageUsers.getDropdownOptions()
        activeDropdown = manageUsers.isAttrInElement(
            "active", "class", allRoles)
        res = res and activeDropdown
        Logger.info(f"dropdown is active: {res}")
        for ele in allEntries:
            res = res and (manageUsers.isAttrInElement(
                "selected", "class", ele))
        Logger.info(f"All options of dropdown are selected: {res}")
        filterCheckBox.click()
        res = res and not manageUsers.isElementPresent(
            manageUsers.dropdownCheckIcon)
        Logger.info(f"checkbox de-select: {res}")
        for ele in allEntries:
            res = res and (not manageUsers.isAttrInElement(
                "selected", "class", ele))
        Logger.info(f"All options of dropdown deselected: {res}")
        activeDropdown = manageUsers.isAttrInElement(
            "active", "class", allRoles)
        res = res and not activeDropdown
        Logger.info(f"dropdown is not active: {res}")
        allRoles.click()
        res = res and (not manageUsers.isAttrInElement(
            "visible", "class", allRoles))
        Logger.info(f"Modal removed: {res}")
        text = allRoles.text
        labelText = "All Roles"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL ROLES SELECT ALL)")

    # TODO: icon check
    def test_dropDown_Roles_SelectOne(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        roleList = manageUsers.getIthColData(self.tableDataMap, 4)
        allRoles = manageUsers.getAllRolesDropDown()
        allRoles.click()
        Logger.info("clicking User dropdown")
        count = manageUsers.getRolesCount(self.tableDataMap)
        idx = randrange(count)
        option = manageUsers.getOneDropDownOption(
            manageUsers, idx)
        option.click()
        role = option.text
        Logger.info(f"Role selected: {role}")
        size = 0
        for r in roleList:
            if role.lower() == r.lower():
                size += 1
        rows = manageUsers.getAllTableRows(manageUsers)
        res = size == len(rows)
        Logger.info(f"size of row : {size} : {res}")
        text = allRoles.text
        labelText = str(1) + "\nof " + str(count) + " total"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        roleData = []

        for i in range(len(roleList)):
            if roleList[i].lower() == role.lower():
                data = manageUsers.getIthRowsData(self.tableDataMap, i)
                roleData.append(data)

        manageUsers.getTableData(
            self.tableColumns, self.tableDataMap, rows)
        size = len(self.tableDataMap[self.tableColumns[0]])
        for i in range(size):
            rowData = manageUsers.getIthRowsData(self.tableDataMap, i)
            uname = rowData[0]
            selectedData = []
            for data in roleData:
                if uname == data[0]:
                    selectedData = data
                    break
            res = res and selectedData == rowData
            Logger.info(f"rowData Matched: {selectedData}:{res}")
        option = manageUsers.getOneDropDownOption(
            manageUsers, idx)
        option.click()
        allRoles.click()
        text = allRoles.text
        labelText = "All Roles"
        res = res and labelText == text
        Logger.info(f"label text :{labelText}: {res}")
        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL ROLES SELECT ONE)")

    def test_dropDown_Roles_FilterBar(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        allRoles = manageUsers.getAllRolesDropDown()
        Logger.info("getting all roles dropdown")
        res = True
        allRoles.click()
        Logger.info("clicking dropdown")

        filterBar = manageUsers.getFilterBar()
        Logger.info("clicking all Users dropdown and typing")
        enterText = 'ad'
        filterBar.send_keys(enterText)
        NoResult = manageUsers.isElementPresent(
            manageUsers.noResult)

        if not NoResult:
            filterCheckBox = manageUsers.getFilterCheckBox()
            Logger.info(
                "clicking on selectAll checkbox to select only containing role")
            filterCheckBox.click()
            allRows = manageUsers.getAllTableRows(manageUsers)
            Logger.info(
                "getting all rows of which are contains selected options")
            manageUsers.getTableData(
                ManageUsersData.TABLE_COLUMNS, self.tableDataMap, allRows)
            rolesList = manageUsers.getIthColData(self.tableDataMap, 4)
            count = 0
            Logger.info(
                f"checking each options contains the entered value:{rolesList}")
            for ele in rolesList:
                if enterText.lower() in ele.lower():
                    count = count + 1
            res = res and count == len(allRows)
            Logger.info(f"no of options: {count} are correct: {res}")
            filterCheckBox = manageUsers.getFilterCheckBox()
            filterCheckBox.click()
            Logger.info("checkbox deselect")
            sizeAllRows = len(manageUsers.getAllRows())
            res = res and sizeAllRows == self.noOfRows
            Logger.info(
                f"size of rows after deselect checkbox: {sizeAllRows} : {res}")
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

        assert res
        Logger.info("TestCASE PASSED (DROPDOWN ALL ROLES FILTER BAR)")

    def test_dropDown_Roles_MultiSelect(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        count = manageUsers.getRolesCount(self.tableDataMap)
        if count == 1:
            Logger.info("Multiple Roles not present")
            return
        allRoles = manageUsers.getAllRolesDropDown()
        allRoles.click()
        res = True
        roles = []
        for i in range(2):
            idx = 1 - i
            Logger.debug(f"opt no: {idx}")
            option = manageUsers.getOneDropDownOption(
                manageUsers, idx)
            option.click()
            Logger.debug("clicking opt.")
            time.sleep(1)
            text = option.text
            roles.append(text)
            count = 0
            data = manageUsers.getIthColData(self.tableDataMap, 4)
            for j in range(len(data)):
                ele = data[j]
                if ele in roles:
                    count += 1
            rows = manageUsers.getAllTableRows(manageUsers)
            size = len(rows)
            res = res and size == count
            Logger.info(f"size of row: {count}")
        reset = manageUsers.getResetTool()[0]
        reset.click()
        Logger.info("dropdown closed")

    def test_delete_Multiple_Select_Users(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        res = True
        unique = set([])
        iterations = 2
        if self.noOfRows <= 2:
            Logger.info("Multiple users can't be deleted")
            return
        loginUserIdx = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        userNameToBeDeleted = []
        userList = manageUsers.getIthColData(self.tableDataMap, 0)
        for i in range(iterations):
            idx = randrange(self.noOfRows)
            if idx == loginUserIdx:
                idx = (idx + 1) % self.noOfRows
            idx = manageUsers.getIndex(unique, idx, self.noOfRows)
            unique.add(idx)
            Logger.info(f"Row No: {idx} selected")
            userNameToBeDeleted.append(userList[idx])
            manageUsers.selectOne(manageUsers, idx)

        sizeAfter = self.noOfRows - iterations
        deleteBtn = manageUsers.getEditOptions()[2]
        deleteBtn.click()
        Logger.info("delete btn clicked")
        yesBtn = manageUsers.getDeleteModalBtns()[2]
        yesBtn.click()
        Logger.info("clicking yes btn")
        allRows = manageUsers.getAllRows()
        lenRows = len(allRows)
        res = res and lenRows == sizeAfter
        Logger.info(
            f"{iterations} Users deleted:No of rows: {lenRows} : {res}")
        manageUsers.getTableData(
            self.tableColumns, self.tableDataMap, allRows)
        allUsers = manageUsers.getIthColData(self.tableDataMap, 0)
        for ele in allUsers:
            if ele in userNameToBeDeleted:
                res = False
        Logger.info(f"{userNameToBeDeleted} deleted : {res}")
        assert res
        Logger.info("TestCASE PASSED (DELETE MULTIPLE USERS)")

    def test_delete_Modal(self):
        Logger.info(
            "==============================================================================================================\n")
        if self.noOfRows == 1:
            Logger.info("No User other than admin to delete")
            return
        manageUsers = ManageUsersPage(self.driver)
        loginIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        idx = randrange(self.noOfRows)
        if idx == loginIndex:
            idx = (loginIndex + 1) % self.noOfRows
        manageUsers.selectOne(manageUsers, idx)
        deleteBtn = manageUsers.getEditOptions()[2]
        deleteBtn.click()
        Logger.info("delete btn clicked")
        res = manageUsers.isElementPresent(
            manageUsers.deleteDialogBox)
        Logger.info(f"Modal is visible: {res}")
        cancelBtn = manageUsers.getDeleteModalBtns()[0]
        cancelBtn.click()
        Logger.info("clicking cross btn")
        isModal = manageUsers.isElementPresent(
            manageUsers.deleteDialogBox)
        res = res and not isModal
        Logger.info(f"Modal is not visible: {res}")
        row = manageUsers.getTableOneRow(manageUsers, idx)
        isRowSelected = manageUsers.isAttrInElement("selected", "class", row)
        res = res and isRowSelected
        Logger.info(f"row is still selected: {isRowSelected}: {res}")
        assert res
        manageUsers.selectOne(manageUsers, idx)
        Logger.info("TestCASE PASSED (MODAL OF DELETE USER)")

    def test_delete_Modal_NoBtn(self):
        Logger.info(
            "==============================================================================================================\n")
        if self.noOfRows == 1:
            Logger.info("No User other than admin to delete")
            return
        manageUsers = ManageUsersPage(self.driver)
        loginIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        idx = randrange(self.noOfRows)
        if idx == loginIndex:
            idx = (loginIndex + 1) % self.noOfRows
        manageUsers.selectOne(manageUsers, idx)
        deleteBtn = manageUsers.getEditOptions()[2]
        deleteBtn.click()
        Logger.info("delete btn clicked")
        res = manageUsers.isElementPresent(
            manageUsers.deleteDialogBox)
        Logger.info(f"Modal is visible: {res}")
        noBtn = manageUsers.getDeleteModalBtns()[1]
        noBtn.click()
        Logger.info("clicking no btn")
        isModal = manageUsers.isElementPresent(
            manageUsers.deleteDialogBox)
        res = res and not isModal
        Logger.info(f"Modal is not visible: {res}")
        row = manageUsers.getTableOneRow(manageUsers, idx)
        isRowSelected = manageUsers.isAttrInElement("selected", "class", row)
        res = res and isRowSelected
        Logger.info(f"row is still selected: {isRowSelected}: {res}")
        assert res
        manageUsers.selectOne(manageUsers, idx)
        Logger.info("TestCASE PASSED (NO BTN OF DELETE USER MODAL)")

    def test_delete_LoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        loginUserIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        manageUsers.selectOne(manageUsers, loginUserIndex)
        deleteBtn = manageUsers.getEditOptions()[2]
        res = manageUsers.isAttrInElement('disabled', 'class', deleteBtn)
        Logger.info(f"loginUser Deletion not allowed: {res}")
        manageUsers.selectOne(manageUsers, loginUserIndex)
        assert res
        Logger.info("TestCASE PASSED (DELETE LOGIN USER)")

    def test_delete_NonLoginUser(self):
        Logger.info(
            "==============================================================================================================\n")
        if self.noOfRows == 1:
            Logger.info("No User other than admin to delete")
            return
        manageUsers = ManageUsersPage(self.driver)
        loginIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        idx = randrange(self.noOfRows)
        if idx == loginIndex:
            idx = (loginIndex + 1) % self.noOfRows
        uname = manageUsers.getIthColData(self.tableDataMap, 0)[idx]
        Logger.info(f"{uname} to be deleted")
        manageUsers.selectOne(manageUsers, idx)
        deleteBtn = manageUsers.getEditOptions()[2]
        deleteBtn.click()
        Logger.info("delete btn clicked")
        yesBtn = manageUsers.getDeleteModalBtns()[2]
        yesBtn.click()
        Logger.info("clicking yes btn")
        time.sleep(3)
        allRows = manageUsers.getAllRows()
        manageUsers.getTableData(
            self.tableColumns, self.tableDataMap, allRows)
        sizeAfter = len(self.tableDataMap[self.tableColumns[4]])
        res = self.noOfRows == sizeAfter + 1
        Logger.info(
            f"Size before: {self.noOfRows}  == size after: {sizeAfter} + 1 : {res}")
        unameList = manageUsers.getIthColData(self.tableDataMap, 0)
        for ele in unameList:
            if ele == uname:
                res = False
                break
        Logger.info(f"data removed from table: {res}")
        isModal = manageUsers.isElementPresent(
            manageUsers.deleteDialogBox)
        res = res and not isModal
        Logger.info(f"Modal is removed: {res}")
        assert res
        Logger.info("TestCASE PASSED (DELETE NON LOGIN USER)")

    # BULK # NON-LOGIN-USER

    def test_addUser_multipleUser(self, addUserDataMulti):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        manageUsers.clickAddUserBtn(manageUsers)
        res = True
        userData = addUserDataMulti
        username = userData[self.userFields[0]]
        firstname = userData[self.userFields[1]]
        lastname = userData[self.userFields[2]]
        email = userData[self.userFields[3]]
        role = userData[self.userFields[4]]
        pwd = userData[self.userFields[5]]
        retypepwd = userData[self.userFields[6]]
        newUser = manageUsers.NewUser(manageUsers)
        newUser.setUserName(username)
        newUser.setFirstName(firstname)
        newUser.setLastName(lastname)
        newUser.setRole(role)
        newUser.setEmail(email)
        newUser.setPassword(pwd)
        newUser.setReTypePassword(retypepwd)
        addNewUser = manageUsers.getAddNewUser()
        sizeBefore = self.noOfRows
        Logger.info("Entered All Details")
        addNewUser.click()
        Logger.info("Add Button Clicked")
        time.sleep(3)
        rows = manageUsers.getAllRows()
        manageUsers.getTableData(
            self.tableColumns, self.tableDataMap, rows)
        sizeAfter = len(self.tableDataMap[self.tableColumns[4]])
        Logger.info(
            "getting no of rows before adding new entry: " + str(sizeBefore))
        res = res and (sizeAfter == sizeBefore + 1)
        Logger.info("getting no of rows before adding new entry: " +
                    str(sizeAfter) + " :" + str(res))
        values = [username, firstname, lastname, email, role, pwd, retypepwd]
        Logger.debug("Updated Values to Add in Map: " + str(values))
        Logger.info("setting new entry in tableDataMap")
        manageUsers.addInTable(self.tableDataMap, self.tableColumns, values)
        file = open("../output.json", "a")
        file.write(json.dumps(values))
        file.write(json.dumps(self.tableDataMap, indent=2))
        # TODO: check Row Data Matched
        self.newUserAdded.append([username, pwd, role])
        assert res
        Logger.info("TestCASE PASSED (ADD MULTIPLE NEW USER)")

    def test_editUser_multipleUser(self, editUserDataMulti):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        if self.noOfRows == 1:
            Logger.info("Non Login user not found")
            return
        loginUserIndex = manageUsers.getLoginUserIndex(
            manageUsers, self.tableDataMap)
        Logger.info(f"{self.editFields[0]}")
        idx = manageUsers.UserIndex(
            self.tableDataMap, editUserDataMulti["User Name"])
        manageUsers.selectOne(manageUsers, idx)
        disableItem = 1
        if idx == loginUserIndex:
            disableItem = 2
        editBtn = manageUsers.getEditOptions()[1]
        editBtn.click()
        Logger.info("Edit btn clicked")
        res = True
        userData = editUserDataMulti
        Logger.info("getting all disabled fields")
        disabledEle = manageUsers.getDisabled()
        noOfDisabled = len(disabledEle)
        res = res and noOfDisabled == disableItem
        firstname = userData[self.editFields[0]]
        lastname = userData[self.editFields[1]]
        email = userData[self.editFields[2]]
        role = 'Admin'
        if noOfDisabled != 2:
            role = userData[self.editFields[3]]
        newUser = manageUsers.NewUser(manageUsers)
        if firstname != '':
            newUser.setFirstName(firstname)
        if lastname != '':
            newUser.setLastName(lastname)
        if noOfDisabled != 2:
            if role != '':
                selectedRole = newUser.setRole(role)
                Logger.info(f"role: {selectedRole} selected :{res}")
        else:
            Logger.info("role dropdown disabled")
        if email != '':
            newUser.setEmail(email)
        updatebtn = manageUsers.getUpdate()
        FN = newUser.firstNameInput().text
        LN = newUser.lastNameInput().text
        EM = newUser.emailInput().text
        RO = newUser.roleDropDown().text
        Logger.info("entering all fields: " + FN +
                    "  " + LN + " " + EM + " " + RO)
        updatedValues = [FN, LN, EM, RO]
        Logger.info("updated values: " + str(updatedValues))
        updatebtn.click()
        Logger.info("clicking update btn and waiting..")
        time.sleep(4)
        res = res and not manageUsers.isElementPresent()
        Logger.info(f"Modal removed: {res}")
        row = manageUsers.getTableOneRow(manageUsers, idx)
        val = manageUsers.getIthRowFromTable(row)
        Logger.info("getting data from row: " + str(val))
        for i in range(1, len(self.tableColumns)):
            key = self.tableColumns[i]
            newVal = updatedValues[i - 1]
            manageUsers.updateTableRow(self.tableDataMap, newVal, key, idx)
            Logger.info("updated key and val: " +
                        str(key) + " -> " + str(newVal))

        Logger.info("update in tableDataMap")
        rowUpdated = manageUsers.getIthRowFromTable(row)
        res = res and (not manageUsers.isAttrInElement(
            "selected", "class", row))
        Logger.info("selected row " + str(idx) + " is unselected: " + str(res))
        assert res and (val == rowUpdated)
        Logger.info("selected row " + str(idx) + " is updated: " + str(res))
        Logger.info("TestCASE PASSED (EDIT LOGIN USER)")

    def test_ChangePwdUser_multiple_user(self, changePwdDataMulti):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        res = True
        userName = changePwdDataMulti[self.changePwdFields[0]]
        idx = manageUsers.UserIndex(self.tableDataMap, userName)
        role = manageUsers.getIthColData(self.tableDataMap, 4)[idx]
        manageUsers.selectOne(manageUsers, idx)
        changePasswordBtn = manageUsers.getEditOptions()[0]
        changePasswordBtn.click()
        Logger.info("clicking change password btn")
        data = [changePwdDataMulti[self.changePwdFields[1]],
                changePwdDataMulti[self.changePwdFields[2]]]
        newUser = manageUsers.NewUser(manageUsers)
        newUser.setPassword(data[0])
        newUser.setReTypePassword(data[1])
        changePwdBtn = manageUsers.getChangePassword()
        changePwdBtn.click()
        Logger.info("clicking changePwd btn")
        time.sleep(1)
        loginPage = LoginPage(self.driver)
        loginPage.Logout()
        time.sleep(6)
        if role == 'Admin':
            res = res and manageUsers.loginWithAdmin(manageUsers, userName,
                                                     data[0])
        else:
            res = res and manageUsers.loginWithNonAdmin(manageUsers, userName,
                                                        data[0])
        loginPage = LoginPage(self.driver)
        loginPage.Logout()
        assert res
        Logger.info("TestCASE PASSED (PASSWORD CHANGE MULTI_USER)")

    def test_deleteUser_multipleUser(self, deleteUserDataMulti):
        Logger.info(
            "==============================================================================================================\n")
        manageUsers = ManageUsersPage(self.driver)
        userName = deleteUserDataMulti
        Logger.info(f"{userName}")
        uIdx = manageUsers.UserIndex(self.tableDataMap, userName)
        Logger.info(f"{uIdx}")
        manageUsers.selectOne(manageUsers, uIdx)
        deleteBtn = manageUsers.getEditOptions()[2]
        deleteBtn.click()
        Logger.info("delete btn clicked")
        yesBtn = manageUsers.getDeleteModalBtns()[2]
        yesBtn.click()
        Logger.info("clicking yes btn")
        time.sleep(3)
        allRows = manageUsers.getAllTableRows(manageUsers)
        manageUsers.getTableData(
            self.tableColumns, self.tableDataMap, allRows)
        sizeAfter = len(self.tableDataMap[self.tableColumns[4]])
        res = self.noOfRows == sizeAfter + 1
        Logger.info(
            f"Size before: {self.noOfRows}  == size after: {sizeAfter} + 1 : {res}")
        unameList = manageUsers.getIthColData(self.tableDataMap, 0)
        for ele in unameList:
            if ele == userName:
                res = False
                break
        Logger.info(f"data removed from table:{userName} : {res}")
        assert res
        Logger.info("TestCASE PASSED (DELETE MULTI-USER)")

    @pytest.fixture(params=ManageUsersData.getAddTestData('Sheet1'))
    def addUserData(self, request):
        manageUsers = ManageUsersPage(self.driver)
        manageUsers.clickAddUserBtn(manageUsers)
        yield request.param
        cancelBtn = manageUsers.getCancel()
        cancelBtn.click()

    @pytest.fixture(params=ManageUsersData.getAddTestData('Sheet3'))
    def addUserDataMulti(self, request):
        itemsCount = len(ManageUsersData.DEFAULT_ADD_USER_DATA)
        yield request.param
        if itemsCount - len(self.newUserAdded) == 0:
            manageUsers = ManageUsersPage(self.driver)
            res = True
            loginPage = LoginPage(self.driver)
            loginPage.Logout()
            for entry in self.newUserAdded:
                uname = entry[0]
                pwd = entry[1]
                role = entry[2]
                if role == 'Admin':
                    res = res and manageUsers.loginWithAdmin(manageUsers, uname, pwd)
                else:
                    res = res and manageUsers.loginWithNonAdmin(manageUsers, uname, pwd)
                loginPage = LoginPage(self.driver)
                loginPage.Logout()
            assert res

    @pytest.fixture(params=ManageUsersData.getEditTestData('Sheet2'))
    def editUserData(self, request):
        return request.param

    @pytest.fixture(params=ManageUsersData.getEditTestData('Sheet4'))
    def editUserDataMulti(self, request):
        return request.param

    @pytest.fixture(params=ManageUsersData.DELETE_USER)
    def deleteUserDataMulti(self, request):
        return request.param

    @pytest.fixture(params=ManageUsersData.getChangePwdTestData())
    def changePwdDataMulti(self, request):
        return request.param

    @pytest.fixture(params=ManageUsersData.CHANGE_PASSWORD)
    def deleteUserDataMulti(self, request):
        return request.param

    @pytest.fixture(params=ManageUsersData.DEFAULT_PASSWORD_DATA)
    def editPwdUserData(self, request):
        return request.param

    @pytest.fixture()
    def initial(self, openBrowser):
        self.driver = openBrowser
        manageUsers = ManageUsersPage(self.driver)
        if not manageUsers.urlPresent(self.URL):
            manageUsers.loginWithAdmin(manageUsers)
        rows = manageUsers.getAllTableRows(manageUsers)
        self.noOfRows = len(rows)
        manageUsers.getTableData(self.tableColumns, self.tableDataMap, rows)
        file = open("output.json", "w")
        file.write(json.dumps(self.tableDataMap, indent=2))
        yield
        Logger.info(
            "#################################################-DONE-##############################################################")

    # TODO:non sorting edit at that idx
    # TODO:sorting -> add acc to sorting col and data
