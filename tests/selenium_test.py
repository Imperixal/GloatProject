from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Assuming WebDriverSingleton and LoggerSetup are properly set up
from test_configs.WebDriverSingleton import WebDriverSingleton
from test_configs.LoggerSetup import logging  # If needed
from test_configs.WebActions import WebActions


def test_convert_temperatures():
    try:

        temp_in_c = 100
        temp_in_f = 212.00
        actions = WebActions()

        # Get WebDriver instance from Singleton
        driver = WebDriverSingleton.get_instance()

        # Connect to the page
        actions.navigate_to_page("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")

        time.sleep(2)
        #actions.print_title()
        actions.accept_cookies()

        actions.set_value_into_conversion_input_field(temp_in_c)
        actions.assert_conversion_result(input_value=temp_in_c, output_value=temp_in_f)

    finally:
        # Close thce browser
        WebDriverSingleton.close_driver()
