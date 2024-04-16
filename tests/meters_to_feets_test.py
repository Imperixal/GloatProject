import time
from test_configs.WebDriverSingleton import WebDriverSingleton
from test_configs.WebActions import WebActions
import pytest


@pytest.mark.selenium
@pytest.mark.meters_to_feets
def test_meters_to_feets():
    try:
        meters = "100"
        feets = str(round(float(meters) * 3.28084, 2))
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
