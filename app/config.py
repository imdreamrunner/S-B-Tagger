__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"

import os
import yaml


CONFIG_FILE = os.path.abspath(os.path.dirname(__file__) + '/../config.yaml')


def get_config(key):
    settings = yaml.load(open(CONFIG_FILE))
    if key in settings:
        return settings[key]