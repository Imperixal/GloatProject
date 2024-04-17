import json
import logging
import pytest
from datetime import datetime, timedelta
from API_tests_utils.WeatherAPI import WeatherAPI
import pytz

@pytest.fixture
def weather_api():
    return WeatherAPI('20852', 'US')


def find_midday_temperature(forecast_data, target_date_str):
    """
    Find the midday temperature for a given target date in the forecast data.

    :param forecast_data: The forecast data containing the temperature information.
    :param target_date_str: The target date in the format 'YYYY-MM-DD'.
    :return: The midday temperature for the target date, or None if no matching forecast is found.
    """
    for item in forecast_data['list']:
        # Check if the date and time exactly match 'YYYY-MM-DD 12:00:00'
        if item['dt_txt'] == f"{target_date_str} 12:00:00":
            return item['main']['temp']
    return None  # Return None if no matching forecast is found


@pytest.mark.api_tests
def test_midday_temperature_variance(weather_api):
    """
    This method tests the midday temperature variance using the given weather API.

    :param weather_api: An instance of the weather API.
    :return: None

    """
    geo_data = weather_api.get_geolocation()
    forecast_data = weather_api.get_forecast(geo_data['lat'], geo_data['lon'])

    # Format and log the forecast data
    formatted_json = json.dumps(forecast_data, indent=4)
    logging.info("API Response: \n" + formatted_json)

    # Adjust the timezone to Eastern Time, which is the relevant timezone for zip code 20852
    timezone = pytz.timezone('America/New_York')
    today = datetime.now(timezone).date()
    tomorrow = today + timedelta(days=1)

    logging.info(f"Looking for forecasts for today ({today}) and tomorrow ({tomorrow}) at 12:00:00.")

    today_temp = find_midday_temperature(forecast_data, today.strftime('%Y-%m-%d'))
    tomorrow_temp = find_midday_temperature(forecast_data, tomorrow.strftime('%Y-%m-%d'))

    # Ensure we have both temperatures
    assert today_temp is not None, "No midday temperature found for today."
    assert tomorrow_temp is not None, "No midday temperature found for tomorrow."

    # Calculate tolerance based on today's temperature
    tolerance = 0.1 * today_temp

    # Assert tomorrow's temperature is within 10% of today's
    assert abs(today_temp - tomorrow_temp) <= tolerance, (
        f"Tomorrow's temperature {tomorrow_temp}C is not within 10% of today's {today_temp}C."
    )

    logging.info(f"Test Passed: Tomorrow's temperature {tomorrow_temp}C is within 10% of today's {today_temp}C.")



