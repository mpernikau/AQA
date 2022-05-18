from selenium.webdriver.common.by import By


class LoginPageLocators():
    BUTTON_PERSONAL_DATA = (By.CSS_SELECTOR, "[data-id='accept-all']")
    EMAIL_FIELD = (By.NAME, 'email')
    PASS_FIELD = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-id='button-submit']")
    REGISTER_LINK = (By.CLASS_NAME, 'LoginForm-module__link--3_ZMP')

class RegisterPageLocators():
    FIRST_NAME_FIELD = (By.NAME, 'firstName')
    LAST_NAME_FIELD = (By.NAME, 'lastName')
    REGISTRATION_EMAIL_FIELD = (By.ID, 'email')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="pbw-react-root"]/div[1]/div/div[2]/div[2]/form/div[4]/div/button')
    PASSWORD = (By.NAME, 'password')
    REQ_CHECKBOX = (By.NAME, 'termsAcceptance')
    RECAPTCHA = (By.ID, 'recaptcha-anchor')


class MainPageLocators():
    ALERT_GUIDE = (By.ID, 'g1-userlane-tut-slide-content-launcher-undefined')
    ALLERT_GUIDE_PASS_BTN = (By.ID, 'g1-userlane-slide-btn-0')
    NOTIF_CLOSE = (By.CLASS_NAME, 'Notification-module__closeButton--1dBwr components-module__transparent-button--3mzKp')
    BURGER_MENU = (By.XPATH, '//*[@id="pbw-react-root"]/main/aside/nav/ul/li[1]')
    OUTGOING_INVOICE_PAGE = (By.CLASS_NAME, 'yygpdi-0.ivxxJA')
    PROPOSAL_PAGE = (By.CLASS_NAME, 'yygpdi-0.iGUYFO')
    CREATE_PROPOSAL_BUTTON = (By.CSS_SELECTOR,"button[dataid = 'Proposals:button-new']")
    BUTTON_BANK_ALERT = (By.CSS_SELECTOR, "button[data-id = 'ConfirmationModal:button-confirm']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, 'input[data-id = "ProposalPage:input-subject"]')
    CLIENT_INPUT = (By.NAME, 'client')
    CLIENT_MENU_CHOICE = (By.CSS_SELECTOR, 'li[data-id = "option-1"]')
    VALID_UNTIL_PROPOSAL = (By.CSS_SELECTOR, "input[data-id = 'ProposalPage:container-valid-unit']")
    LINE_ITEM_INPUT = (By.CSS_SELECTOR, 'input[data-id = "LineItem:input-position"')
    LINE_ITEM_QUANTITY = (By.CSS_SELECTOR, 'input[data-id = "LineItem:input-quantity"')
    UNIT_PROPOSAL_FIELD = (By.NAME, 'unit')
    UNIT_MENU_CHOICE = (By.CSS_SELECTOR, 'div[data-id = "UnitSelect:items-menu"]')
    LINE_ITEM_NET_GROSS = (By.CSS_SELECTOR, 'input[data-id = "LineItem:input-net-gross"]')
    CONFIRM_LINE_ITEM = (By.CSS_SELECTOR, "button[data-id = 'LineItem:button-submit']")
    DOWNLOAD_OR_SAVE_PROPOSAL_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'ProposalPage:button-download-or-save']")
    DOWNLOAD_PDF_PROPOSAL_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'download-pdf']")