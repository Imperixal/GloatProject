from test_configs.WebDriverSingleton import WebDriverSingleton
from test_configs.LoggerSetup import log_function_call
from test_configs.LoggerSetup import logging

@log_function_call
class WebActions:
    def __init__(self):
        self.driver = WebDriverSingleton.get_instance()

    @log_function_call
    def navigate_to_page(self, url):
        """Navigate to the URL"""
        self.driver.get(url)

    @log_function_call
    def print_title(self):
        """Print the title name"""
        logging.info("The page title is: ", self.driver.title)
