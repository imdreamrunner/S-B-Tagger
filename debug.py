__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"


import sys
import logging
from app import app

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    port = 5000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', debug=True, port=port)
