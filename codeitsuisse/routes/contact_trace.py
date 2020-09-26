import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def evaluateContectTrace():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    infected = data.get("infected");

    result = infected

    logging.info("My result :{}".format(result))
    return json.dumps(result);



