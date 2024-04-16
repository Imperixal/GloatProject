from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from test_configs.WebDriverSingleton import WebDriverSingleton
from test_configs.LoggerSetup import log_function_call
from test_configs.LoggerSetup import logging


@log_function_call
class WebActions:
    def __init__(self):
        self.driver = WebDriverSingleton.get_instance()

    @log_function_call
    def navigate_to_page(self, url):
        """
        Navigates to the specified URL.

        :param url: The URL to navigate to.
        :type url: str
        """
        self.driver.get(url)

    @log_function_call
    def print_title(self):
        """
        Print the page title.

        :return: None
        """
        logging.info("The page title is: ", self.driver.title)

    @log_function_call
    def accept_cookies(self):
        """
        Find and click on the cookies button to accept cookies.

        :return: None
        """
        try:
            cookies_button = self.driver.find_element(By.CSS_SELECTOR, "#ez-accept-all")
            cookies_button.click()
        except Exception as e:
            logging.info("Cookie consent button not found: %s", str(e))
            logging.info("Skipping")
            pass


    @log_function_call
    def __find_element_quietly(self, by, value):
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            return None


    @log_function_call
    def set_value_into_conversion_input_field(self, value):

        # there is inconsistency in the page dom objects. The input element field can be on same pages
        # found by name 'arg'
        # on another it can be found by name 'argConv'
        input_element = self.__find_element_quietly(By.NAME, "arg")
        if not input_element:
            logging.info("Input field with name 'arg' not found, trying 'argConv' instead")

            # If 'arg' is not found, try to find the input element by name 'argConv'
            input_element = self.__find_element_quietly(By.NAME, "argumentConv")
            if not input_element:
                logging.error("Alternative input field 'argConv' also not found.")
                raise Exception("Neither 'arg' nor 'argConv' elements found")
            else:
                logging.info("Alternative input field 'argConv' found")

        if input_element:
            input_element.clear()
            input_element.send_keys(value)


    @log_function_call
    def assert_conversion_result(self, expected_result):
        # there is inconsistency in the page dom objects. The input element field can be on same pages
        # found by css selector '#answerDisplay'
        # on another it can be found by id 'answer'

        result_element = self.__find_element_quietly(By.CSS_SELECTOR, "#answerDisplay")
        if not result_element:
            logging.info("Input field with css selector '#answerDisplay' not found, trying by ID 'answer' instead")

            result_element = self.__find_element_quietly(By.ID, "answer")
            if not result_element:
                logging.error("Alternative input field 'answer' also not found.")
                raise Exception("Neither '#answerDisplay' nor 'answer' elements found")
            else:
                logging.info("Alternative input field 'answer' found")

        # do the assertion
        try:
            assert result_element.text == expected_result
            logging.info("\n Conversion passed:" + "\n" + f"we expected: {expected_result}" + "\n" + f"and got {result_element.text}")
        except AssertionError:
            raise Exception("\n Conversion failed:" + "\n" + f"we expected: {expected_result}" + "\n" +
                            f"but got {result_element.text} instead")
