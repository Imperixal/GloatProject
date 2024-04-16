import time
from test_configs.WebDriverSingleton import WebDriverSingleton
from test_configs.WebActions import WebActions


def test_temperature_conversion():
    try:
        temp_in_c = "100"
        temp_in_f = "212.00"
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
