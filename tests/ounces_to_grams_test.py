import time
from test_configs.WebDriverSingleton import WebDriverSingleton
from test_configs.WebActions import WebActions
import pytest


@pytest.mark.selenium
@pytest.mark.ounces_to_grams
def test_ounces_to_grams():
    try:
        ounces = "100"
        formula = (float(ounces) * 28.34952)

        # The result on the page is always .000 of decimals
        grams = f"{formula:.3f}"

        actions = WebActions()

        # Connect to the page
        actions.navigate_to_page("https://www.metric-conversions.org/weight/ounces-to-grams.htm")

        time.sleep(2)
        actions.accept_cookies()

        actions.set_value_into_conversion_input_field(ounces)

        # They actually have a bug on their site. The usual result format is:
        # 100oz = 2834.952g
        # but they are showing:
        # 100oz= 2834.952g
        # I am asserting the current state, meaning without the space before '=' sign
        actions.assert_conversion_result(f"{ounces}oz= {grams}g")

    finally:
        # Close the browser
        WebDriverSingleton.close_driver()
