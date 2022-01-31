import copy
import time

from selenium.webdriver.common.keys import Keys

from Pages.LoginPage import LoginPage
from Utilities import Logger
from Utilities.utilityFn import Utility

utils = Utility()


def loginWithAdmin(driver, manageProducts, uName='admin', pwd='admin'):
    currUrl = utils.currentUrl(driver)
    res = True
    if not ("manage-products" in currUrl):
        if "login" in currUrl:
            loginPage = LoginPage(driver)
            loginPage.enterCredentials(uName, pwd)
            Logger.info(f"Enter details for Login As userName : {uName}")
        time.sleep(2)
        res = utils.isElementPresent(driver, manageProducts.addProduct)
        manageProducts.getManageBtn().click()
        Logger.info("Manage Button Clicked")
        manageProducts.getProductOption().click()
        Logger.info("Manage Products option clicked")
        time.sleep(2)
        currUrl = utils.currentUrl(driver)
        Logger.info("Current Url is " + utils.currentUrl(driver))
    return res and ("manage-products" in currUrl)


def loginWithNonAdmin(driver, manageProducts, uName, pwd):
    currUrl = utils.currentUrl(driver)
    res = True
    if not ("manage-products" in currUrl):
        if "login" in currUrl:
            loginPage = LoginPage(driver)
            loginPage.enterCredentials(uName, pwd)
            Logger.info(f"Enter details for Login As userName : {uName}")
        time.sleep(2)
        res = not utils.isElementPresent(driver, manageProducts.addProduct)
        Logger.info(f"{res}")
        currUrl = utils.currentUrl(driver)
        Logger.info("Current Url is " + utils.currentUrl(driver))
    return res and ("dashboard" in currUrl)


def selectAll(manageProducts):
    selectAllCheckBox = manageProducts.getSelectAll()
    selectAllCheckBox.click()
    Logger.info("clicked on selectAll CheckBox")


# changed
def selectOne(driver, manageProducts, index):
    checkbox = getAllRowCheckBox(manageProducts)
    selectedCheckBox = checkbox[index]
    utils.scrollToElement(driver, selectedCheckBox)
    Logger.info(f"getting checkBox {index} and click")
    selectedCheckBox.click()
    Logger.info("checkbox clicked")


def getAllRowCheckBox(manageProducts):
    checkboxes = manageProducts.getTableCheckbox()
    Logger.info("getting all checkboxes of all rows of table")
    return checkboxes


# changed
def getOneRowCheckBox(driver, manageProducts, index):
    checkBoxes = getAllRowCheckBox(manageProducts)
    Logger.info(f"getting checkbox of {index}th index row")
    utils.scrollToElement(driver, checkBoxes[index])
    return checkBoxes[index]


def getAllTableRows(manageProducts):
    Logger.info("getting all rows")
    rows = manageProducts.getAllRows()
    return rows


# changed
def getTableOneRow(driver, manageProducts, index):
    Logger.info(f"getting row : {index}")
    rows = manageProducts.getAllRows()
    utils.scrollToElement(driver, rows[index])
    return rows[index]
