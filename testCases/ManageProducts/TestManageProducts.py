import json
from random import randrange

import pytest

from Pages.ManageProductsPage import ManageProductsPage
from Utilities import Logger
from Utilities.utilityFn import Utility
from dataSet.ManageProductsData import ManageProductsData
from testCases.ManageProducts import ManageProductsUtils


@pytest.mark.usefixtures("initial")
class TestManageProducts:
    utils = Utility()
    driver = None
    tableDataMap = {}
    noOfRows = 0
    tableColumns = ManageProductsData.TABLE_COLUMNS
    url = ManageProductsData.URL

    def test_checkURL(self, userName='admin', password='admin'):
        Logger.info(
            "==============================================================================================================\n")
        manageProducts = ManageProductsPage(self.driver)
        res = ManageProductsUtils.loginWithAdmin(self.driver, manageProducts, userName, password)
        assert res
        Logger.info("TestCASE PASSED (CHECK URL)")

    def test_selectAllCheckBox_Clickable(self):
        Logger.info(
            "==============================================================================================================\n")
        res = True
        manageProducts = ManageProductsPage(self.driver)
        ManageProductsUtils.selectAll(manageProducts)
        isCheckIconPresent = self.utils.isElementPresent(self.driver, manageProducts.checkIcon)
        res = res and isCheckIconPresent
        Logger.info(f"checkIcon present : {res}")
        ManageProductsUtils.selectAll(manageProducts)
        isCheckIconPresent = self.utils.isElementPresent(self.driver, manageProducts.checkIcon)
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
        ManageProductsUtils.selectAll(manageProducts)
        labelTextFinal = manageProducts.getLabelText()
        Logger.info(f"getting label text after selection: {labelTextFinal}")
        textAfter = self.utils.labelTextAllSelected(self.noOfRows)
        res = res and (labelTextFinal == textAfter)
        Logger.info(f"label Text matched after selectAll:  {textAfter} : {res}")
        ManageProductsUtils.selectAll(manageProducts)
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
        ManageProductsUtils.selectAll(manageProducts)
        rows = ManageProductsUtils.getAllTableRows(manageProducts)
        res = self.utils.isAttrInAllElements('selected', 'class', rows)
        Logger.info(f"all rows are selected: {res}")
        checkBoxes = self.utils.isElementsPresent(self.driver, manageProducts.checkIconRow)
        isChecked = len(checkBoxes)
        res = res and isChecked == self.noOfRows
        Logger.info(f"all rows checkboxes are selected: {res}")
        ManageProductsUtils.selectAll(manageProducts)
        rows = ManageProductsUtils.getAllTableRows(manageProducts)
        res = res and not self.utils.isAttrInAllElements('selected', 'class', rows)
        Logger.info(f"all rows are de-selected: {res}")
        checkBoxes = self.utils.isElementsPresent(self.driver, manageProducts.checkIconRow)
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
        ManageProductsUtils.selectOne(self.driver, manageProducts, index)
        isPartial = self.utils.isElementPresent(self.driver, manageProducts.partialCheckIcon)
        res = isPartial
        Logger.info(f"Partial symbol in selectAll present: {res}")
        isChecked = self.utils.isElementPresent(self.driver, manageProducts.checkIconRow)
        res = res and isChecked
        Logger.info(f"checkbox selected : {res}")
        ManageProductsUtils.selectOne(self.driver, manageProducts, index)
        isPartial = self.utils.isElementPresent(self.driver, manageProducts.partialCheckIcon)
        res = res and not isPartial
        Logger.info(f"Partial symbol removed in selectAll present: {res}")
        isChecked = self.utils.isElementPresent(self.driver, manageProducts.checkIconRow)
        res = res and not isChecked
        Logger.info(f"checkbox de-selected : {res}")
        assert res
        Logger.info("TestCASE PASSED (SELECT ONE ROW CLICKABLE)")

    @pytest.fixture()
    def initial(self, openBrowser):
        self.driver = openBrowser
        manageProducts = ManageProductsPage(self.driver)
        if not self.utils.urlPresent(self.driver, self.url):
            ManageProductsUtils.loginWithAdmin(self.driver, manageProducts)
        rows = ManageProductsUtils.getAllTableRows(manageProducts)
        self.noOfRows = len(rows)
        self.utils.getTableData(self.driver, self.tableColumns, self.tableDataMap, rows)
        file = open("../output.json", "w")
        file.write(json.dumps(self.tableDataMap, indent=2))
        yield
        Logger.info(
            "#################################################-DONE-##############################################################")
