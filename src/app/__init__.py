__version__ = "1.0.0"

import logging.config
import pathlib
import sys
from dotenv import load_dotenv
import tomllib

import configparser
# import yaml
import os.path

abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)

load_dotenv()  # take environment variables from .env

# local imports

# LOGGING_CONFIG = pathlib.Path(__file__).parent / "logger_config.yaml"
# with open(LOGGING_CONFIG) as f:
#     config_dict = yaml.safe_load(f)
#     logging.config.dictConfig(config_dict)


LOGGING_CONFIG_TOML = pathlib.Path(__file__).parent / "logger_config.toml"
with open(LOGGING_CONFIG_TOML, 'rb') as f:
    config_dict = tomllib.load(f)
    logging.config.dictConfig(config_dict)


# get root logger
def log():
    logger = logging.getLogger(__name__)
    # the __name__ resolve to "main" since we are at the root of the project
    # This will get the root logger since no logger in the configuration has
    # this name.

    if sys.gettrace() is not None:  # returns True if we are in the debugger
        logger.level = 20  # Debug level for logging while debugging

    return logger


def log_config():
    return config_dict


# read the config file
def config():
    # home = os.path.expanduser('~')
    config_file = pathlib.Path(__file__).parent / "app_settings.ini"
    config = configparser.ConfigParser()
    config.read(config_file)
    return config