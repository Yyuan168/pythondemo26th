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
    for row in S:
        i = 0
        j = 0
        Min = []
        while j < len(row) - 1:
            if row[i] == "X":
                i += 1
                if j < i:
                    j = i
            else:
                j += 1
                if row[j] == "X":
                    i = j + 1
                else:
                    if j - i == n - 1:
                        tmp = row[i:j+1]
                        tmp = [int(m) for m in tmp]
                        Min.append(sum(tmp))
                        i += 1
        if len(Min):
            cost.append(min(Min))
        
    
    return min(cost) if len(cost) != 0 else 0




