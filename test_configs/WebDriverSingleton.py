# webdriver_singleton.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from test_configs.LoggerSetup import log_function_call
from test_configs.LoggerSetup import log_class_method_call
from test_configs.LoggerSetup import logging


@log_function_call
class WebDriverSingleton:
    _instance = None

    @log_class_method_call
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            options = Options()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            cls._instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return cls._instance

    @log_class_method_call
    @classmethod
    def close_driver(cls):
        if cls._instance is not None:
            cls._instance.quit()
            cls._instance = None
