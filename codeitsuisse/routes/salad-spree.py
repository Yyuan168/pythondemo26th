import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSaladSpree():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("number_of_salads");
    S = data.get("salad_prices_street_map");

    result = saladspree(n, S)

    logging.info("My result :{}".format(result))
    return json.dumps(result);

def saladspree(n, S):
    cost = []
    select = []
    for i in S:
        for j in i:
            if len(select) < n:
                if j != "X":
                    select.append(int(j))
                else:
                    select = []
            if len(select) == n:
                cost.append(sum(select))
                select = []
        select = []
    
    return min(cost) if len(cost) != 0 else 0




