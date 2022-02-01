from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ManageProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

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
        return self.waitForElements(ManageProductsPage.manageBtn)[1]

    def getProductOption(self):
        return self.waitForElement(ManageProductsPage.productOpt)

    def getAddUser(self):
        return self.waitForElement(ManageProductsPage.addUserBtn)

    def getModal(self):
        return self.waitForElement(ManageProductsPage.modal)

    def getSelectAll(self):
        return self.waitForElement(ManageProductsPage.selectAll)

    def getTable(self):
        return self.waitForElement(ManageProductsPage.table)

    def getAllRows(self):
        return self.waitForElements(ManageProductsPage.allRows)

    def getTableCheckbox(self):
        return self.waitForElements(ManageProductsPage.tableCheckBox)

    def getEditOptions(self):
        return self.waitForElements(ManageProductsPage.editOptions)

    def getLabelText(self):
        return self.waitForElement(ManageProductsPage.label).text

    def UserNameClick(self):
        return self.waitForElement(ManageProductsPage.userNameSort)

    def FirstNameClick(self):
        return self.waitForElement(ManageProductsPage.firstNameSort)

    def LastNameClick(self):
        return self.waitForElement(ManageProductsPage.lastNameSort)

    def EmailClick(self):
        return self.waitForElement(ManageProductsPage.emailSort)

    def RoleNameClick(self):
        return self.waitForElement(ManageProductsPage.roleSort)

    def getUsername(self):
        return self.waitForElement(ManageProductsPage.userName)

    def getFirstname(self):
        return self.waitForElement(ManageProductsPage.firstName)

    def getLastname(self):
        return self.waitForElement(ManageProductsPage.lastName)

    def getEmail(self):
        return self.waitForElement(ManageProductsPage.email)

    def getPassword(self):
        return self.waitForElement(ManageProductsPage.password)

    def getReTypePassword(self):
        return self.waitForElement(ManageProductsPage.reTypePassword)

    def getRole(self):
        return self.waitForElement(ManageProductsPage.role)

    def getRoleChoice(self):
        return self.waitForElements(ManageProductsPage.roleChoice)

    def getAddNewUser(self):
        return self.waitForElement(ManageProductsPage.addNewUserBtn)

    def getCancel(self):
        return self.waitForElement(ManageProductsPage.cancelBtn)

    def getUpdate(self):
        return self.waitForElement(ManageProductsPage.updateBtn)

    def getDisabled(self):
        return self.waitForElements(ManageProductsPage.disabled)

    def getLoggedInUser(self):
        return self.waitForElement(ManageProductsPage.loginUser).text

    def getChangePassword(self):
        return self.waitForElement(ManageProductsPage.changePassword)

    def getSortedArrow(self, element):
        return element.find_element(By.CSS_SELECTOR, "uwf-icon")

    def getAllUsersDropDown(self):
        return self.waitForElement(ManageProductsPage.allUsers)

    def getAllRolesDropDown(self):
        return self.waitForElement(ManageProductsPage.allRoles)

    def getDropdownOptions(self):
        return self.waitForElements(ManageProductsPage.dropdownOptions)

    def getDeleteModalBtns(self):
        return self.waitForElements(ManageProductsPage.deleteModalBtns)

    def getFilterBar(self):
        return self.waitForElement(ManageProductsPage.filter)

    def getFilterCheckBox(self):
        return self.waitForElement(ManageProductsPage.filterCheckBox)

    def getFilterController(self):
        return self.waitForElements(ManageProductsPage.filterController)

    def getClearTool(self):
        return self.waitForElement(ManageProductsPage.clearTool)

    def getResetTool(self):
        return self.waitForElements(ManageProductsPage.resetTool)
