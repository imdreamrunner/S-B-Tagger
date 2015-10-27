# -*- coding: utf-8 -*-

__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"


import sys
import os
import logging
from flask import Flask, render_template, request, session, url_for, redirect
from . import helper
from . import db
from . import config


log = logging.getLogger(__name__)

STATIC_FOLDER = os.path.abspath(os.path.join(__file__, "../../static"))
TEMPLATE_FOLDER = os.path.abspath(os.path.join(__file__, "../../view"))
app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)

app.secret_key = config.get_config("secret")


@app.route("/login", methods=['GET'])
def login_page():
    return render_template('login.jinja2')


@app.route("/login", methods=['POST'])
def login_action():
    username = request.form['username'].lower()
    password = request.form['password']
    log.info('User ' + username + ' tries to login with password ' + password + '.')
    login_result = helper.login(username, password)
    if login_result:
        session['user'] = username
        return redirect(url_for('vote_page'))
    else:
        return render_template('login.jinja2', message="Username or password is incorrect.")


@app.route("/logout", methods=['GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login_page'))


@app.route("/")
def vote_page():
    if 'user' not in session:
        return redirect(url_for('login_page'))

    options = helper.get_options()
    item = helper.get_random_item(session['user'])
    if item is None:
        return render_template("vote.jinja2", message='All done.')
    item = list(item)
    item[1] = unicode(item[1], errors='replace')
    return render_template("vote.jinja2", item=item, options=options)


@app.route("/vote/<int:item>", methods=['POST'])
def accept_vote(item):
    if 'user' not in session:
        return redirect(url_for('login_page'))
    choice = int(request.form['choice'])
    log.info("Receive vote for item " + str(item) + " with option " + str(choice))
    if helper.get_item(item) is None:
        return "Wrong Item ID"
    helper.vote(item, choice, session['user'])
    return "OK"


@app.before_request
def before_request():
    log.info("Connect to the database.")
    db.connect()


@app.teardown_request
def after_request(exception):
    log.info("Disconnect to the database.")
    db.disconnect()