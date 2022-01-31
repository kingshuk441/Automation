import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Utilities import Logger
from selenium.webdriver.common.keys import Keys


class ManageUsersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    manageBtn = (By.CSS_SELECTOR, 'div.uwf-navbar__menu-item-container')
    userOpt = (By.XPATH, "//div[contains(text(),'Users')]")
    addUserBtn = (
        By.CSS_SELECTOR, "button.uwf-btn.uwf-grid-action-buttons__button.uwf-btn_info")
    modal = (By.CSS_SELECTOR, "div.uwf-modal")
    __selectAll = (
        By.XPATH, "(//div[@class='uwf-checkbox uwf-checkbox_light'])[1]")

    table = (By.CSS_SELECTOR, "div.uwf-grid")
    allRows = (By.XPATH, "(//div[@class='uwf-grid__main_table'])[1]//section")
    tableCheckBox = (By.XPATH,
                     "(//div[@class='uwf-grid__main'])[1]//div[@class='uwf-checkbox uwf-checkbox_light'] | (//div["
                     "@class='uwf-grid__main'])[1]//div[@class='uwf-checkbox uwf-checkbox_dark']  ")
    editOptions = (By.XPATH, "//div[@class='uwf-grid']/div/div[4]//button")
    label = (
        By.XPATH, "//div[@class='uwf-grid']//div[@class='uwf-grid__header_selection_label']")
    userNameSort = (
        By.XPATH, "//div[contains(text(),'User Name')][1]/parent::div/parent::div")
    firstNameSort = (
        By.XPATH, "//div[contains(text(),'First Name')][1]/parent::div/parent::div")
    lastNameSort = (
        By.XPATH, "//div[contains(text(),'Last Name')][1]/parent::div/parent::div")
    emailSort = (
        By.XPATH, "//div[contains(text(),'Email')][1]/parent::div/parent::div")
    roleSort = (
        By.XPATH, "(//div[contains(text(),'Role')][1])[3]/parent::div/parent::div")
    userName = (By.ID, "userName")
    firstName = (By.ID, "firstName")
    lastName = (By.ID, "lastName")
    email = (By.ID, "email")
    password = (By.ID, "password")
    reTypePassword = (By.ID, "retypePassword")
    role = (By.CSS_SELECTOR,
            "div.uwf-modal div.uwf-select-trigger-button__selected-text")
    roleChoice = (By.CSS_SELECTOR, "div.uwf-select-option__label")
    addNewUserBtn = (By.XPATH, "//button[contains(text(),'Add user')]")
    cancelBtn = (By.XPATH, "//button[contains(text(),'Cancel')]")
    updateBtn = (By.XPATH, "//button[contains(text(),'Update user')]")
    disabled = (By.CSS_SELECTOR, "div.uwf-form-field_disabled")
    loginUser = (By.CSS_SELECTOR, "div.uwf-navbar__settings-user")
    changePassword = (By.XPATH, "//button[contains(text(),'Change password')]")
    allUsers = (
        By.XPATH, "(//div[@class='uwf-filter-bar-item'])[2]//button[@type = 'button']")
    allRoles = (
        By.XPATH, "(//div[@class='uwf-filter-bar-item'])[1]//button[@type = 'button']")
    dropdownOptions = (By.CSS_SELECTOR, "li.uwf-select-option")
    deleteModalBtns = (By.CSS_SELECTOR, "div.cdk-overlay-pane button")
    filter = (By.CSS_SELECTOR, "div input[placeholder='Filter']")
    filterCheckBox = (
        By.CSS_SELECTOR, "div.uwf-select-overlay div.uwf-checkbox")
    filterController = (
        By.CSS_SELECTOR, "div.uwf-filter-bar__global-controls-container div.uwf-svg-icon")
    clearTool = (By.CSS_SELECTOR, "form button[uwftooltip='Clear']")
    resetTool = (By.CSS_SELECTOR, 'button.uwf-filter-bar-item__reset-button')
    checkIcon = "div.uwf-grid__header_selection .uwf-checkbox__check-icon"
    partialCheckIcon = ".uwf-checkbox__check-icon.uwf-checkbox__check-icon_partial"
    checkIconRow = "div.uwf-checkbox.uwf-checkbox_dark .uwf-checkbox__check-icon"
    errorFields = "span.uwf-form-field-error"
    deleteDialogBox = "div .uwf-confirmation-dialog__box"
    dropdownCheckIcon = 'div .uwf-checkbox__check-icon'
    noResult = 'div.uwf-select-options-list__filter-no-result'
    addProduct = 'button.uwf-btn.product-bar-add-item-button'

    def getManageBtn(self):
        return self.waitForElements(ManageUsersPage.manageBtn)[1]

    def getUserOption(self):
        return self.waitForElement(ManageUsersPage.userOpt)

    def getAddUser(self):
        return self.waitForElement(ManageUsersPage.addUserBtn)

    def getModal(self):
        return self.waitForElement(ManageUsersPage.modal)

    def getSelectAll(self):
        return self.waitForElement(ManageUsersPage.__selectAll)

    def getTable(self):
        return self.waitForElement(ManageUsersPage.table)

    def getAllRows(self):
        return self.waitForElements(ManageUsersPage.allRows)

    def getTableCheckbox(self):
        return self.waitForElements(ManageUsersPage.tableCheckBox)

    def getEditOptions(self):
        return self.waitForElements(ManageUsersPage.editOptions)

    def getLabelText(self):
        return self.waitForElement(ManageUsersPage.label).text

    def UserNameClick(self):
        return self.waitForElement(ManageUsersPage.userNameSort)

    def FirstNameClick(self):
        return self.waitForElement(ManageUsersPage.firstNameSort)

    def LastNameClick(self):
        return self.waitForElement(ManageUsersPage.lastNameSort)

    def EmailClick(self):
        return self.waitForElement(ManageUsersPage.emailSort)

    def RoleNameClick(self):
        return self.waitForElement(ManageUsersPage.roleSort)

    def getUsername(self):
        return self.waitForElement(ManageUsersPage.userName)

    def getFirstname(self):
        return self.waitForElement(ManageUsersPage.firstName)

    def getLastname(self):
        return self.waitForElement(ManageUsersPage.lastName)

    def getEmail(self):
        return self.waitForElement(ManageUsersPage.email)

    def getPassword(self):
        return self.waitForElement(ManageUsersPage.password)

    def getReTypePassword(self):
        return self.waitForElement(ManageUsersPage.reTypePassword)

    def getRole(self):
        return self.waitForElement(ManageUsersPage.role)

    def getRoleChoice(self):
        return self.waitForElements(ManageUsersPage.roleChoice)

    def getAddNewUser(self):
        return self.waitForElement(ManageUsersPage.addNewUserBtn)

    def getCancel(self):
        return self.waitForElement(ManageUsersPage.cancelBtn)

    def getUpdate(self):
        return self.waitForElement(ManageUsersPage.updateBtn)

    def getDisabled(self):
        return self.waitForElements(ManageUsersPage.disabled)

    def getLoggedInUser(self):
        return self.waitForElement(ManageUsersPage.loginUser).text

    def getChangePassword(self):
        return self.waitForElement(ManageUsersPage.changePassword)

    def getSortedArrow(self, element):
        return element.find_element(By.CSS_SELECTOR, "uwf-icon")

    def getAllUsersDropDown(self):
        return self.waitForElement(ManageUsersPage.allUsers)

    def getAllRolesDropDown(self):
        return self.waitForElement(ManageUsersPage.allRoles)

    def getDropdownOptions(self):
        return self.waitForElements(ManageUsersPage.dropdownOptions)

    def getDeleteModalBtns(self):
        return self.waitForElements(ManageUsersPage.deleteModalBtns)

    def getFilterBar(self):
        return self.waitForElement(ManageUsersPage.filter)

    def getFilterCheckBox(self):
        return self.waitForElement(ManageUsersPage.filterCheckBox)

    def getFilterController(self):
        return self.waitForElements(ManageUsersPage.filterController)

    def getClearTool(self):
        return self.waitForElement(ManageUsersPage.clearTool)

    def getResetTool(self):
        return self.waitForElements(ManageUsersPage.resetTool)

    class NewUser:
        def __init__(self, manageUsers):
            Logger.info("New User Details")
            self.manageUsers = manageUsers
            self.__userName = None
            self.__firstName = None
            self.__lastName = None
            self.__email = None
            self.__password = None
            self.__reTypePassword = None
            self.__role = None

        def userNameInput(self):
            return self.manageUsers.getUsername()

        def firstNameInput(self):
            return self.manageUsers.getFirstname()

        def lastNameInput(self):
            return self.manageUsers.getLastname()

        def emailInput(self):
            return self.manageUsers.getEmail()

        def passwordInput(self):
            return self.manageUsers.getPassword()

        def reTypePasswordInput(self):
            return self.manageUsers.getReTypePassword()

        def roleDropDown(self):
            return self.manageUsers.getRole()

        def setRole(self, role):
            element = self.roleDropDown()
            element.click()
            roleChoice = self.manageUsers.getRoleChoice()
            index = 0
            if role.lower() != 'admin':
                index = 1
            choice = roleChoice[index]
            text = choice.text
            choice.click()
            return text

        def setUserName(self, val):
            self.__userName = val
            element = self.userNameInput()
            self.clear_text(element)
            if self.isEmpty(val):
                self.makeEmptyField(element)
            else:
                element.send_keys(self.__userName)
            Logger.debug(f"username: {self.__userName}")

        def setFirstName(self, val):
            self.__firstName = val
            element = self.firstNameInput()
            self.clear_text(element)
            if self.isEmpty(val):
                self.makeEmptyField(element)
            else:
                element.send_keys(self.__firstName)
            Logger.debug(f"firstname: {self.__firstName}")

        def setLastName(self, val):
            self.__lastName = val
            element = self.lastNameInput()
            self.clear_text(element)
            if self.isEmpty(val):
                self.makeEmptyField(element)
            else:
                element.send_keys(self.__lastName)
            Logger.debug(f"lastname: {self.__lastName}")

        def setEmail(self, val):
            self.__email = val
            element = self.emailInput()
            self.clear_text(element)
            if self.isEmpty(val):
                self.makeEmptyField(element)
            else:
                element.send_keys(self.__email)
            Logger.debug(f"email: {self.__email}")

        def setPassword(self, val):
            self.__password = val
            element = self.passwordInput()
            self.clear_text(element)
            if self.isEmpty(val):
                self.makeEmptyField(element)
            else:
                element.send_keys(self.__password)
            Logger.debug(f"password: {self.__password}")

        def setReTypePassword(self, val):
            self.__reTypePassword = val
            element = self.reTypePasswordInput()
            self.clear_text(element)
            if self.isEmpty(val):
                self.makeEmptyField(element)
            else:
                element.send_keys(self.__reTypePassword)

            Logger.debug(f"retypePassword: {self.__reTypePassword}")

        def isEmpty(self, val):
            val = str(val)
            return len(val) == 0

        def makeEmptyField(self, element):
            element.send_keys(" ")
            self.clear_text(element)

        def clear_text(self, element):
            length = len(element.get_attribute('value'))
            element.send_keys(length * Keys.BACKSPACE)

    def loginWithAdmin(self, manageUsers, uName='admin', pwd='admin'):
        currUrl = self.currentUrl()
        res = True
        if not ("manage-users" in currUrl):
            if "login" in currUrl:
                loginPage = LoginPage.LoginPage(self.driver)
                loginPage.enterCredentials(uName, pwd)
                Logger.info(f"Enter details for Login As userName : {uName}")
            time.sleep(2)
            res = self.isElementPresent(manageUsers.addProduct)
            manageUsers.getManageBtn().click()
            Logger.info("Manage Button Clicked")
            manageUsers.getUserOption().click()
            Logger.info("Manage Users option clicked")
            time.sleep(2)
            currUrl = self.currentUrl()
            Logger.info("Current Url is " + self.currentUrl())
        return res and ("manage-users" in currUrl)

    def loginWithNonAdmin(self, manageUsers, uName, pwd):
        currUrl = self.currentUrl()
        res = True
        if not ("manage-users" in currUrl):
            if "login" in currUrl:
                loginPage = LoginPage.LoginPage(self.driver)
                loginPage.enterCredentials(uName, pwd)
                Logger.info(f"Enter details for Login As userName : {uName}")
            time.sleep(2)
            res = not self.isElementPresent(manageUsers.addProduct)
            Logger.info(f"{res}")
            currUrl = self.currentUrl()
            Logger.info("Current Url is " + self.currentUrl())
        return res and ("dashboard" in currUrl)
