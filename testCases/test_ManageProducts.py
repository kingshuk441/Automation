import json
import time

from random import randrange

import pytest

from Pages.LoginPage import LoginPage
from Pages.ManageProductsPage import ManageProductsPage
from Utilities import Logger
from dataSet.ManageProductsData import ManageProductsData


@pytest.mark.usefixtures("initial")
class TestManageProducts:
    driver = None
    tableDataMap = {}
    noOfRows = 0
    tableColumns = ManageProductsData.TABLE_COLUMNS
    url = ManageProductsData.URL

    def test_checkURL(self, userName='admin', password='admin'):
        Logger.info(
            "==============================================================================================================\n")
        manageProducts = ManageProductsPage(self.driver)
        currUrl = self.currentUrl()
        res = True
        if not (self.url in currUrl):
            if "login" in currUrl:
                loginPage = LoginPage(self.driver)
                loginPage.enterCredentials(userName, password)
                Logger.info(f"Enter details for Login As userName : {userName}")
            time.sleep(2)
            manageProducts.getManageBtn().click()
            Logger.info("Manage Button Clicked")
            manageProducts.getProductOption().click()
            Logger.info("Manage Product option clicked")
            time.sleep(2)
            currUrl = self.currentUrl()
            Logger.info("Current Url is " + self.currentUrl())
        res = res and (self.url in currUrl)
        Logger.info("TestCASE PASSED (CHECK URL)")

    def test_selectAllCheckBox_Clickable(self):
        Logger.info(
            "==============================================================================================================\n")
        res = True
        manageProducts = ManageProductsPage(self.driver)
        manageProducts.selectAll(manageProducts)
        isCheckIconPresent = self.utils.isElementPresent(manageProducts.checkIcon)
        res = res and isCheckIconPresent
        Logger.info(f"checkIcon present : {res}")
        manageProducts.selectAll(manageProducts)
        isCheckIconPresent = self.utils.isElementPresent(manageProducts.checkIcon)
        assert res and not isCheckIconPresent
        Logger.info(f"checkIcon not present : {res}")
        Logger.info("TestCASE PASSED (SELECT ALL CLICKABLE)")

    def test_selectAllCheckBox_LabelText(self):
        Logger.info(
            "==============================================================================================================\n")
        manageProducts = ManageProductsPage(self.driver)
        labelTextInit = manageProducts.getLabelText()
        Logger.info(f"getting initial label text: {labelTextInit}")
        initStr = self.utils.labelTextUnselected(self.noOfRows)
        res = (labelTextInit == initStr)
        Logger.info(f"labelText is correct : {initStr}  :  {res}")
        manageProducts.selectAll(manageProducts)
        labelTextFinal = manageProducts.getLabelText()
        Logger.info(f"getting label text after selection: {labelTextFinal}")
        textAfter = self.utils.labelTextAllSelected(self.noOfRows)
        res = res and (labelTextFinal == textAfter)
        Logger.info(f"label Text matched after selectAll:  {textAfter} : {res}")
        manageProducts.selectAll(manageProducts)
        labelTextEnd = manageProducts.getLabelText()
        Logger.info(f"getting label text after deselecting: {labelTextEnd}")
        endStr = self.utils.labelTextUnselected(self.noOfRows)
        res = res and endStr == labelTextEnd
        Logger.info(f"label Text matched after deselect selectAll:  {endStr} : {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT ALL LABEL TEXT)")

    def test_selectAllCheckBox_rowsSelected(self):
        Logger.info(
            "==============================================================================================================\n")
        manageProducts = ManageProductsPage(self.driver)
        manageProducts.selectAll(manageProducts)
        rows = manageProducts.getAllTableRows(manageProducts)
        res = self.utils.isAttrInAllElements('selected', 'class', rows)
        Logger.info(f"all rows are selected: {res}")
        checkBoxes = self.utils.isElementsPresent(manageProducts.checkIconRow)
        isChecked = len(checkBoxes)
        res = res and isChecked == self.noOfRows
        Logger.info(f"all rows checkboxes are selected: {res}")
        manageProducts.selectAll(manageProducts)
        rows = manageProducts.getAllTableRows(manageProducts)
        res = res and not self.utils.isAttrInAllElements('selected', 'class', rows)
        Logger.info(f"all rows are de-selected: {res}")
        checkBoxes = self.utils.isElementsPresent(manageProducts.checkIconRow)
        isChecked = len(checkBoxes)
        res = res and isChecked == 0
        Logger.info(f"all rows checkboxes are de-selected: {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT ALL , ALL ROWS SELECTED)")

    def test_selectOneRow_Clickable(self):
        Logger.info(
            "==============================================================================================================\n")
        manageProducts = ManageProductsPage(self.driver)
        index = randrange(self.noOfRows)
        Logger.info(f"no of rows to be selected is: {index}")
        manageProducts.selectOne(manageProducts, index)
        isPartial = self.utils.isElementPresent(manageProducts.partialCheckIcon)
        res = isPartial
        Logger.info(f"Partial symbol in selectAll present: {res}")
        isChecked = self.utils.isElementPresent(manageProducts.checkIconRow)
        res = res and isChecked
        Logger.info(f"checkbox selected : {res}")
        manageProducts.selectOne(manageProducts, index)
        isPartial = self.utils.isElementPresent(manageProducts.partialCheckIcon)
        res = res and not isPartial
        Logger.info(f"Partial symbol removed in selectAll present: {res}")
        isChecked = self.utils.isElementPresent(manageProducts.checkIconRow)
        res = res and not isChecked
        Logger.info(f"checkbox de-selected : {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT ONE ROW CLICKABLE)")

    @pytest.fixture()
    def initial(self, openBrowser):
        self.driver = openBrowser
        manageProducts = ManageProductsPage(self.driver)
        if not self.utils.urlPresent(self.url):
            self.test_checkURL()
        rows = manageProducts.getAllTableRows(manageProducts)
        self.noOfRows = len(rows)
        self.utils.getTableData(self.tableColumns, self.tableDataMap, rows)
        file = open("output.json", "w")
        file.write(json.dumps(self.tableDataMap, indent=2))
        yield
        Logger.info(
            "#################################################-DONE-##############################################################")
