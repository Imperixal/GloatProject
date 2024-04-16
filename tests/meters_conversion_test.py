import time
from test_configs.WebDriverSingleton import WebDriverSingleton
from test_configs.WebActions import WebActions


def test_meters_conversion():
    try:
        meters = "100"
        feets = "328.08"
        actions = WebActions()

        # Connect to the page
        actions.navigate_to_page("https://www.metric-conversions.org/length/meters-to-feet.htm")

        time.sleep(2)
        actions.accept_cookies()

        actions.set_value_into_conversion_input_field(meters)
        actions.assert_conversion_result(f"{meters}m = {feets}ft")

    finally:
        # Close the browser
        WebDriverSingleton.close_driver()
