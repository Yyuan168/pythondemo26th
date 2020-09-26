import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def evaluateCleanFloor():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    test = data.get("test");

    result = solution(test)

    logging.info("My result :{}".format(result))
    return json.dumps(result);

def solution(test):
    result = {}
    for key, l in test.items:
        moves = 0
        

        result[key] = moves

    return result