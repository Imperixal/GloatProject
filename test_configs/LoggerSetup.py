import functools
import logging
import time

# Boolean variable for checking whether the logger function was already initiated in the script or not.
# This is for avoiding creating duplicated logger handlers, which would cause issues with logging itself.
logger_initialized = False


# This is the global logger setup. Every test should use this logger by calling "import logger_setup"
def init_logger():
    global logger_initialized
    if logger_initialized:
        raise Exception(
            """The logger function has already been initiated in the conftest.py file. You don't need to initialize the logger again.
            In your script, do:
            from test_configs.LoggerSetup import logging
            and you can start using the logger function.
            The formatting will be applied according what's shown in logging.basicConfig""")

    format_str = '%(asctime)s %(levelname)s %(filename)s @ %(lineno)d: %(message)s'
    logging.basicConfig(level=logging.INFO, format=format_str, datefmt='%d-%m-%Y %H:%M:%S')
    logger_initialized = True

    logging.info("Logger successfully initiated")


def log_call(func_name, start_time, result, args=None, kwargs=None, is_classmethod=False, cls=None):
    """
    Logs the details of a function call.

    :param func_name: (str) Name of the function.
    :param start_time: (float) Start time of the function call.
    :param result: (any) Result of the function call.
    :param args: (list) List of arguments passed to the function call. Defaults to None.
    :param kwargs: (dict) Dictionary of keyword arguments passed to the function call. Defaults to None.
    :param is_classmethod: (bool) Indicates if the function is a class method. Defaults to False.
    :param cls: (class) Class to which the function belongs. Defaults to None.
    :return: None
    """
    args_repr = [repr(a) for a in args] if args else []
    kwargs_repr = [f"{k}={v!r}" for k, v in (kwargs.items() if kwargs else [])]
    signature = ", ".join(args_repr + kwargs_repr)
    class_info = f"{cls.__name__}." if cls and is_classmethod else ""
    logging.info(f"----- START {class_info}{func_name} ----- \n" + 13*("\t") + f"ARG {signature}")
    end_time = time.time()
    logging.info(f"===== END {class_info}{func_name} in {end_time - start_time:.2f} seconds ===== \n" + 13*("\t") + f"RES {result}")


def log_function_call(func):
    """
    Decorator for instance methods.

    :param func: The instance method to be decorated.
    :return: The decorated instance method.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        log_call(func.__name__, start_time, result, args, kwargs)
        return result

    return wrapper


def log_class_method_call(func):
    """
    Decorates a class method with additional functionality.

    :param func: The class method to be decorated.
    :return: The decorated class method.
    """

    @functools.wraps(func)
    def class_method_wrapper(cls, *args, **kwargs):
        start_time = time.time()
        result = func(cls, *args, **kwargs)
        end_time = time.time()
        logging.info(f"Called {cls.__name__}.{func.__name__} with args {args}, kwargs {kwargs}; Returned {result} in {end_time - start_time:.2f}s")
        return result
    return classmethod(class_method_wrapper)
