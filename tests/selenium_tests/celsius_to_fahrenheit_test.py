import time
from test_configs.WebDriverSingleton import WebDriverSingleton
from selenium_tests_utils.WebActions import WebActions
import pytest


@pytest.mark.selenium
@pytest.mark.celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    try:
        temp_in_c = "100"
        formula = (float(temp_in_c) * 1.8) + 32

        # we need to add one more zero at the end as the result on the page is always .00 and not .0
        temp_in_f = f"{formula:.2f}"
        actions = WebActions()

        # Connect to the page
        actions.navigate_to_page("https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm")

        time.sleep(2)
        actions.accept_cookies()

        actions.set_value_into_conversion_input_field(temp_in_c)
        actions.assert_conversion_result(f"{temp_in_c}°C = {temp_in_f}°F")

    finally:
        # Close the browser
        WebDriverSingleton.close_driver()
