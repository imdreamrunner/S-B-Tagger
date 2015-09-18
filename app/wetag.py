__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"


import os
import logging
from flask import Flask, render_template, request
from . import helper
from . import db

log = logging.getLogger(__name__)

STATIC_FOLDER = os.path.abspath(os.path.join(__file__, "../../static"))
TEMPLATE_FOLDER = os.path.abspath(os.path.join(__file__, "../../view"))
app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)


@app.route("/")
def vote_page():
    options = helper.get_options()
    item = helper.get_random_item()
    if item is None:
        return 'All done.'
    return render_template("vote.jinja2", item=item, options=options)


@app.route("/vote/<int:item>", methods=['POST'])
def accept_vote(item):
    choice = int(request.form['choice'])
    log.info("Receive vote for item " + str(item) + " with option " + str(choice))
    if helper.get_item(item) is None:
        return "Wrong Item ID"
    helper.vote(item, choice)
    return "OK"


@app.before_request
def before_request():
    log.info("Connect to the database.")
    db.connect()


@app.teardown_request
def after_request(exception):
    log.info("Disconnect to the database.")
    db.disconnect()