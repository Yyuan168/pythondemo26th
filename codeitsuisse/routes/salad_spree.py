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
        flag = False
        for j in range(len(i) - n + 1):
            select = i[j:j+n]
            if "X" not in select:
                tmp = [int(i) for i in select]
                if not flag:
                   Min = sum(tmp)
                else:
                    Min = min(Min, sum(tmp))
                flag = True
        if flag:
            cost.append(Min)
    
    return min(cost) if len(cost) != 0 else 0




