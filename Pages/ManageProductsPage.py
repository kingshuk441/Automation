from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Utilities.utilityFn import Utility


class ManageProductsPage:
    utils = Utility()

    def __init__(self, driver):
        self.driver = driver

    manageBtn = (By.CSS_SELECTOR, 'div.uwf-navbar__menu-item-container')
    productOpt = (By.XPATH, "//div[contains(text(),'Products')]")
    addUserBtn = (By.CSS_SELECTOR, "button.uwf-btn.uwf-grid-action-buttons__button.uwf-btn_info")
    modal = (By.CSS_SELECTOR, "div.uwf-modal")
    selectAll = (By.XPATH, "(//div[@class='uwf-checkbox uwf-checkbox_light'])[1]")
    table = (By.CSS_SELECTOR, "div.uwf-grid")
    allRows = (By.XPATH, "(//div[@class='uwf-grid__main_table'])[1]//section")
    tableCheckBox = (By.XPATH,
                     "(//div[@class='uwf-grid__main'])[1]//div[@class='uwf-checkbox uwf-checkbox_light'] | (//div["
                     "@class='uwf-grid__main'])[1]//div[@class='uwf-checkbox uwf-checkbox_dark']  ")
    editOptions = (By.XPATH, "//div[@class='uwf-grid']/div/div[4]//button")
    label = (By.XPATH, "(//div[@class='uwf-grid__header_selection_label'])[1]")
    userNameSort = (By.XPATH, "//div[contains(text(),'User Name')][1]/parent::div/parent::div")
    firstNameSort = (By.XPATH, "//div[contains(text(),'First Name')][1]/parent::div/parent::div")
    lastNameSort = (By.XPATH, "//div[contains(text(),'Last Name')][1]/parent::div/parent::div")
    emailSort = (By.XPATH, "//div[contains(text(),'Email')][1]/parent::div/parent::div")
    roleSort = (By.XPATH, "(//div[contains(text(),'Role')][1])[3]/parent::div/parent::div")
    userName = (By.ID, "userName")
    firstName = (By.ID, "firstName")
    lastName = (By.ID, "lastName")
    email = (By.ID, "email")
    password = (By.ID, "password")
    reTypePassword = (By.ID, "retypePassword")
    role = (By.CSS_SELECTOR, "div.uwf-modal div.uwf-select-trigger-button__selected-text")
    roleChoice = (By.CSS_SELECTOR, "div.uwf-select-option__label")
    addNewUserBtn = (By.XPATH, "//button[contains(text(),'Add user')]")
    cancelBtn = (By.XPATH, "//button[contains(text(),'Cancel')]")
    updateBtn = (By.XPATH, "//button[contains(text(),'Update user')]")
    disabled = (By.CSS_SELECTOR, "div.uwf-form-field_disabled")
    loginUser = (By.CSS_SELECTOR, "div.uwf-navbar__settings-user")
    changePassword = (By.XPATH, "//button[contains(text(),'Change password')]")
    allUsers = (By.XPATH, "(//div[@class='uwf-filter-bar-item'])[2]//button[@type = 'button']")
    allRoles = (By.XPATH, "(//div[@class='uwf-filter-bar-item'])[1]//button[@type = 'button']")
    dropdownOptions = (By.CSS_SELECTOR, "li.uwf-select-option")
    deleteModalBtns = (By.CSS_SELECTOR, "div.cdk-overlay-pane button")
    filter = (By.CSS_SELECTOR, "div input[placeholder='Filter']")
    filterCheckBox = (By.CSS_SELECTOR, "div.uwf-select-overlay div.uwf-checkbox")
    filterController = (By.CSS_SELECTOR, "div.uwf-filter-bar__global-controls-container div.uwf-svg-icon")
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
        return self.utils.waitForElements(self.driver, ManageProductsPage.manageBtn)[1]

    def getProductOption(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.productOpt)

    def getAddUser(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.addUserBtn)

    def getModal(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.modal)

    def getSelectAll(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.selectAll)

    def getTable(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.table)

    def getAllRows(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.allRows)

    def getTableCheckbox(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.tableCheckBox)

    def getEditOptions(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.editOptions)

    def getLabelText(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.label).text

    def UserNameClick(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.userNameSort)

    def FirstNameClick(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.firstNameSort)

    def LastNameClick(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.lastNameSort)

    def EmailClick(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.emailSort)

    def RoleNameClick(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.roleSort)

    def getUsername(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.userName)

    def getFirstname(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.firstName)

    def getLastname(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.lastName)

    def getEmail(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.email)

    def getPassword(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.password)

    def getReTypePassword(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.reTypePassword)

    def getRole(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.role)

    def getRoleChoice(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.roleChoice)

    def getAddNewUser(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.addNewUserBtn)

    def getCancel(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.cancelBtn)

    def getUpdate(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.updateBtn)

    def getDisabled(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.disabled)

    def getLoggedInUser(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.loginUser).text

    def getChangePassword(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.changePassword)

    def getSortedArrow(self, element):
        return element.find_element(By.CSS_SELECTOR, "uwf-icon")

    def getAllUsersDropDown(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.allUsers)

    def getAllRolesDropDown(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.allRoles)

    def getDropdownOptions(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.dropdownOptions)

    def getDeleteModalBtns(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.deleteModalBtns)

    def getFilterBar(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.filter)

    def getFilterCheckBox(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.filterCheckBox)

    def getFilterController(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.filterController)

    def getClearTool(self):
        return self.utils.waitForElement(self.driver, ManageProductsPage.clearTool)

    def getResetTool(self):
        return self.utils.waitForElements(self.driver, ManageProductsPage.resetTool)

    def isModalPresent(self, css=''):
        try:
            if css == '':
                css = ".cdk-overlay-pane.uwf-dialog-panel"

            element = self.driver.find_element(By.CSS_SELECTOR, css)
            return True
        except NoSuchElementException as e:
            return False
