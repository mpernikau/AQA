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
    REQ_CHECKBOX = (By.CSS_SELECTOR, 'input[data-id = "checkbox-terms"')
    RECAPTCHA_FRAME = (By.CSS_SELECTOR, '#g-recaptcha > div > div > iframe')
    RECAPTCHA_SOLVE = (By.ID, 'recaptcha-anchor')


class MainPageLocators():
    ALERT_GUIDE = (By.ID, 'g1-userlane-tut-slide-content-launcher-undefined')
    ALERT_GUIDE_PASS_BTN = (By.ID, 'g1-userlane-slide-btn-0')
    NOTIF_CLOSE = (By.CLASS_NAME, 'Notification-module__closeButton--1dBwr components-module__transparent-button--3mzKp')
    BURGER_MENU = (By.XPATH, '//*[@id="pbw-react-root"]/main/aside/nav/ul/li[1]')
    PROPOSAL_PAGE = (By.CLASS_NAME, 'yygpdi-0.iGUYFO')
    ORDER_CONFORMATION_PAGE = (By.CSS_SELECTOR, 'a[data-id="orderConfirmation"]')
    OUTGOING_INVOICE_PAGE = (By.CLASS_NAME, 'yygpdi-0.ivxxJA')
    CREATE_PROPOSAL_BUTTON = (By.CSS_SELECTOR, "button[dataid = 'Proposals:button-new']")
    CREATE_ORDER_CONFORMATION_BUTTON = (By.CSS_SELECTOR, 'button[data-id = "OrderConfirmation:button-new"]')
    BUTTON_BANK_ALERT = (By.CSS_SELECTOR, "button[data-id = 'ConfirmationModal:button-confirm']")


class ProposalPageLocators():
    SUBJECT_INPUT = (By.CSS_SELECTOR, 'input[data-id = "ProposalPage:input-subject"]')
    CLIENT_INPUT = (By.NAME, 'client')
    CLIENT_MENU_CHOICE = (By.CSS_SELECTOR, 'li[data-id = "option-1"]')
    VALID_UNTIL_PROPOSAL = (By.CSS_SELECTOR, "input[data-id = 'ProposalPage:container-valid-unit']")

    CATEGORY_INPUT = (By.CSS_SELECTOR, "input[data-id = 'ProposalPage:select-category']")
    CATEGORY_OTHER_CATEGORY = (By.XPATH, '/html/body/div[1]/main/div/div[2]/form/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[8]')
    CHANGE_CATEGORY_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'changedCategoryConfirmationButton']")
    CHANGE_CATEGORY_HINT = (By.XPATH, '/html/body/div[1]/main/div/div[2]/form/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[2]/p')

    LINE_ITEM_INPUT = (By.CSS_SELECTOR, 'input[data-id = "LineItems:input-position"')
    LINE_ITEM_QUANTITY = (By.CSS_SELECTOR, 'input[data-id = "LineItem:input-quantity"')
    UNIT_PROPOSAL_FIELD = (By.NAME, 'unit')
    UNIT_MENU_CHOICE = (By.CSS_SELECTOR, 'div[data-id = "UnitSelect:items-menu"]')
    LINE_ITEM_NET_GROSS = (By.CSS_SELECTOR, 'input[data-id = "LineItem:input-net-gross"]')
    CONFIRM_LINE_ITEM = (By.CSS_SELECTOR, "button[data-id = 'LineItem:button-submit']")

    DOWNLOAD_OR_SAVE_PROPOSAL_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'ProposalPage:button-download-or-save']")
    DOWNLOAD_PDF_PROPOSAL_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'download-pdf']")

    SEND_BY_EMAIL_PROPOSAL_BUTTON = (By.CSS_SELECTOR, "button[data-id='ProposalPage:button-send-email']")
    EMAIL_INPUT_ON_EMAIL_SENDING_MODAL = (By.CSS_SELECTOR, "input[data-id ='input-email']")
    EMAIL_SEND_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'send-button']")

    PROPOSAL_PAGE_TO_INVOICE_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'ProposalPage:button-transform']")

    PROPOSAL_PAGE_TO_ORDER_CONFORMATION = (By.CSS_SELECTOR, "button[data-id='proposal-into-order-confirmation-button']")

    SAVE_BEFORE_CONTINUE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'ConfirmationModal:button-confirm']")

    SAVE_AS_DRAFT_BUTTON = (By.CSS_SELECTOR, "button[data-id = 'ProposalPage:button-save']")


class ProposalPageListLocators():
    PROPOSAL_PAGE_SEARCH = (By.CSS_SELECTOR, 'input[data-id="Proposals:input-search"]')
    PROPOSAL_PAGE_FILTERS_BUTTON = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]')
    PROPOSAL_PAGE_FILTERS_CLEAN_BUTTON = (By.XPATH, '//*[@id="pbw-react-root"]/main/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]')
    PROPOSAL_PAGE_FILTERS_MORE_THAN_AMOUNT_FIELD = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/input[1]')
    PROPOSAL_PAGE_CSV_EXPORT = (By.CSS_SELECTOR, '[data-id="CSVExport:button"]')

    TYPE_OF_PROPOSAL = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/div/div/span/span')
    SUBJECT_ON_PROPOSAL_PAGE = (By.CSS_SELECTOR, 'span[data-id = "ProposalRow:subject"]')
    AMOUNT_ON_PROPOSAL_PAGE = (By.CSS_SELECTOR, 'span[data-id="ProposalRow:amount"]')
    TABLE_OF_PROPOSALS = (By.XPATH, "//*[@id='pbw-react-root']/main/div/div[2]/div/div/div[2]/div/table/tbody/tr")
    PROPOSAL_VIEW_BUTTON = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div[1]/a')
    PROPOSAL_EDIT_BUTTON = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div[2]/a')
    PROPOSAL_DUPLICATE_BUTTON = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div[3]/button')
    PROPOSAL_MORE_OPTIONS_BUTTON = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div[4]/div')
    PROPOSAL_TO_INVOICE_BUTTON = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div[4]/div[2]/div[1]/button')
    PROPOSAL_TO_ORDER_CONFORMATION_BUTTON = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[8]/div/div[4]/div[2]/div[2]/button')
    PROPOSAL_DELETE_BUTTON = (By.CSS_SELECTOR, 'button[data-id="ProposalRow:button-delete"]')
    PROPOSAL_DELETION_ALERT_BUTTON_YES = (By.CSS_SELECTOR, "button[data-id = 'ConfirmationModal:button-confirm']")

    PROPOSAL_PAGE_PAGINATION = (By.CSS_SELECTOR, 'nav[data-id="pagination"]')
    PROPOSAL_PAGE_NAVIGATION_ARROW_RIGHT = (By.CSS_SELECTOR, 'button[data-id = "next-page"]')
    PROPOSAL_PAGE_NAVIGATION_ARROW_LEFT = (By.CSS_SELECTOR, 'button[data-id="previous-page"]')
    PROPOSAL_PAGE_NAVIGATION_CURRENT_PAGE_FIELD = (By.XPATH, '//*[@id="pbw-react-root"]/main/div/div[2]/div/div/div[3]/div/nav/div/input')
    PROPOSAL_PAGE_NAVIGATION_TOTAL_PAGES = (By.CSS_SELECTOR, 'button[data-id = "total-pages"]')
    PROPOSAL_PAGE_10_PER_PAGE = (By.CSS_SELECTOR, 'button[data-id = "10-per-page"]')
    PROPOSAL_PAGE_25_PER_PAGE = (By.CSS_SELECTOR, 'button[data-id = "25-per-page"]')
    PROPOSAL_PAGE_50_PER_PAGE = (By.CSS_SELECTOR, 'button[data-id = "50-per-page"]')

class OutgoingInvoiceLocators():
    INVOICE_STATUS = (By.CSS_SELECTOR, 'span[data-id = "InvoiceStatus"]')
    DOWNLOAD_OR_SAVE_INVOICE_BUTTON = (By.CSS_SELECTOR, 'button[data-id = "OutgoingInvoicePage:button-actions-dropdown"]')
    DOWNLOAD_PDF_INVOICE_BUTTON = (By.CSS_SELECTOR, 'button[data-id = "OutgoingInvoicePage:button-download-pdf"]')

class OrderConfromationLocators():

    SUBJECT_ON_ORDER_CONFORMATION_DOCUMENT = (By.CSS_SELECTOR, 'input[data-id = "OrderConfirmationPage:input-subject"]')
    CLIENT_INPUT_ON_ORDER_CONFORMATION_DOCUMENT = (By.ID, '[id="downshift-1-input"]')
    VALID_UNTIL_ORDER_CONFORMATION = (By.CSS_SELECTOR, 'input[data-id = "OrderConfirmationPage:container-valid-unit"]')

    LINE_ITEM_NAME_INPUT_ORDER_CONFORMATION = (By.CSS_SELECTOR, 'input[data-id = "LineItems:input-position"]')
    LINE_ITEM_QUANTITY_ORDER_CONFORMATION = (By.CSS_SELECTOR, 'input[data-id = "LineItem:input-quantity"]')
    LINE_ITEM_UNITS_ORDER_CONFORMATION = (By.CSS_SELECTOR, 'input[data-id = "UnitSelect:input-unitSelectInput"]')

    ORDER_CONFORMATION_TO_INVOICE_BUTTON = (By.CSS_SELECTOR, 'button[data-id = "OrderConfirmationPage:button-transform"]')
    ORDER_CONFORMATION_TO_INVOICE_SAVE_BEFORE_CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button[data-id="ConfirmationModal:button-confirm"]')
    DOWNLOAD_OR_SAVE_ORDER_CONFORMATION_BUTTON = (By.CSS_SELECTOR, 'button[data-id="OrderConfirmationPage:button-download-or-save"]')
    DOWNLOAD_PDF_ORDER_CONFORMATION = (By.CSS_SELECTOR, 'button[data-id="download-pdf"]')
    SEND_BY_EMAIL_BUTTON_ORDER_CONFORMATION = (By.CSS_SELECTOR, 'button[data-id = "OrderConfirmationPage:button-send-email"]')
    SAVE_AS_DRAFT_ORDER_CONFORMATION_BUTTON = (By.CSS_SELECTOR, 'button[data-id = "OrderConfirmationPage:button-save"]')

class OrderConformationPageLocators():
    TYPE_OF_ORDER_CONFORMATION = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]/div/div/span')
    SUBJECT_ON_ORDER_CONFORMATION_PAGE = (By.CSS_SELECTOR, 'span[data-id = "OrderConfirmationRow:subject"]')
