from page_objects.element import BasePageElement
from page_objects.locators import MainPageLocators


class InputAmountElement(BasePageElement):
    locator = 'amountinput'


class CoinsInputElement(BasePageElement):
    locator = 'coinsinput'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    # Declares a variable that will contain the retrieved text
    input_amount_element = InputAmountElement()
    coins_input_element = CoinsInputElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Minimal coins" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        element.click()

    def coins_input_element(self):
        element = self.driver.find_element(*MainPageLocators.COINS_INPUT_FIELD)
        return element

    def amount_input_element(self):
        element = self.driver.find_element(*MainPageLocators.AMOUNT_INPUT_FIELD)
        return element

    def submit_button_element(self):
        element = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        return element

    def fill_coins_field(self, data):
        element = self.driver.find_element(*MainPageLocators.COINS_INPUT_FIELD)
        element.send_keys(data)
        return element

    def fill_amount_field(self, data):
        element = self.driver.find_element(*MainPageLocators.AMOUNT_INPUT_FIELD)
        element.send_keys(data)
        return element

    def coins_label_element(self):
        element = self.driver.find_element(*MainPageLocators.COINS_LABEL)
        return element

    def amount_label_element(self):
        element = self.driver.find_element(*MainPageLocators.AMOUNT_LABEL)
        return element


class ResultsPage(BasePage):
    def is_results_with_reachable_sum_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "3" in self.driver.page_source

    def result_page_has_error_message(self):
        return 'Internal Server Error' in self.driver.page_source
