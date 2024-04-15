# webdriver_singleton.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging


class WebDriverSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            options = Options()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            cls._instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return cls._instance

    @classmethod
    def close_driver(cls):
        if cls._instance is not None:
            cls._instance.quit()
            cls._instance = None
