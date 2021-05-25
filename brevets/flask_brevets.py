"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import os
import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
from pymongo import MongoClient

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevetdb
###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


@app.route("/_submit_route", methods=['POST'])
def insert():
    vals = request.form.get('vals')
    print(vals)
    for i in vals:
        control_point = {
            'km': vals[i][0],
            'open_time': vals[i][1],
            'close_time': vals[i][2]
        }
        db.timestable.insert_one(control_point)
    return vals


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    brev_distance = request.args.get('brev_distance', type=float)
    begin_date = request.args.get('begin_date', type=str)
    app.logger.debug("km={}".format(km))
    app.logger.debug("distance={}".format(brev_distance))
    app.logger.debug("begin date={}".format(begin_date))
    app.logger.debug("request.args: {}".format(request.args))
    open_time = acp_times.open_time(km, brev_distance, arrow.get(begin_date)).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brev_distance, arrow.get(begin_date)).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
