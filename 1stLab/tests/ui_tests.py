from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page_objects import page


class TestSeleniumBasic():
    def test_main_page_loads_with_expected_title(self, browser):
        browser.get('http://localhost:5000')
        main_page = page.MainPage(browser)
        assert main_page.is_title_matches()

    def test_main_page_has_coins_input_field(self, browser):
        browser.get('http://localhost:5000')
        main_page = page.MainPage(browser)
        assert main_page.coins_input_element()

    def test_main_page_has_amount_input_field(self, browser):
        browser.get('http://localhost:5000')
        main_page = page.MainPage(browser)
        assert main_page.amount_input_element()

    def test_main_page_has_submit_button(self, browser):
        browser.get('http://localhost:5000')
        main_page = page.MainPage(browser)
        assert main_page.submit_button_element()

    def test_main_page_coin_change_with_reachable_sum(self, browser):
        browser.get('http://localhost:5000')
        main_page = page.MainPage(browser)
        main_page.fill_amount_field('8')
        main_page.fill_coins_field('1 2 5')
        main_page.click_go_button()
        results_page = page.ResultsPage(browser)
        assert results_page.is_results_with_reachable_sum_found()
    def test_main_page_has_coins_label(self, browser):
        browser.get('http://localhost:5000')
        main_page = page.MainPage(browser)
        assert main_page.coins_label_element()

    def test_main_page_has_amount_label(self, browser):
        browser.get('http://localhost:5000')
        main_page = page.MainPage(browser)
        assert main_page.amount_label_element()

    def test_result_page_has_error_message(self, browser):
        browser.get('http://localhost:5000')
        main_page = page.MainPage(browser)
        main_page.fill_amount_field('8')
        main_page.fill_coins_field('1 2 3 4 5 6 7 8 9 10 11 12 13')
        main_page.click_go_button()
        results_page = page.ResultsPage(browser)
        assert results_page.result_page_has_error_message()