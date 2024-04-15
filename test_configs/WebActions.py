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

        :return: None
        :rtype: None
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

    @log_function_call
    def set_value_into_conversion_input_field(self, value):
        # Input the Celsius value into the converter
        input_element = self.driver.find_element(By.NAME, "arg")
        input_element.clear()
        input_element.send_keys(value)
        #input_element.send_keys(Keys.RETURN)

        return self.driver.find_element(By.NAME, "arg")

    @log_function_call
    def assert_conversion_result(self, input_value, output_value):

        # Select the conversion from Celsius to Fahrenheit
        self.driver.find_element(By.CSS_SELECTOR, "#answerDisplay")

        # Get the conversion result
        result = self.driver.find_element(By.CSS_SELECTOR, "#answerDisplay")

        try:
            assert result.text == f"{input_value}°C = {output_value}°F"
        except AssertionError:
            logging.exception("Conversion failed:" + "\n" + f"we expected: {input_value}°C = {output_value}°F" + "\n" +
                              f"but got {result.text} instead")
