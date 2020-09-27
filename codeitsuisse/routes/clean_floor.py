import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def evaluateCleanFloor():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    tests = data.get("tests");

    result = solution(json.loads(tests))


    logging.info("My result :{}".format(result))
    return json.dumps(result)

def solution(tests):
    result = {}
    for key, l in tests.items():
        moves = 0
        j = 0
        l = l["floor"]
        while sum(l) > 0:

            if l[-1] == 0 and len(l) > 2:
                l.pop()

            if j < len(l) - 1:
                j += 1
            else:
                j -= 1

            if l[j] > 0:
                l[j] -= 1
            else:
                l[j] += 1

            moves += 1

        result[key] = moves

    return result