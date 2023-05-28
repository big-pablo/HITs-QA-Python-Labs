from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SUBMIT_BUTTON = (By.ID, 'send')
    COINS_INPUT_FIELD = (By.ID, 'coinsinput')
    AMOUNT_INPUT_FIELD = (By.ID, 'amountinput')
    COINS_LABEL = (By.ID, 'coinslabel')
    AMOUNT_LABEL = (By.ID, 'amountlabel')

