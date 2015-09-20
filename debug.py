__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"

import logging
from app import app

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
