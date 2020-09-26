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
    return jsonify(result);

def saladspree(n, S):
    select = []
    Min = 0
    for row in S:
        i = 0
        j = 0
        while j < len(row) - 1:
            if row[i] == "X":
                i += 1
                if j < i:
                    j = i
            else:
                j += 1
                if row[j] == "X":
                    i = j + 1
                    j = i
                else:
                    if j - i == n - 1:
                        tmp = row[i:j+1]
                        tmp = [int(m) for m in tmp]
                        if Min == 0:
                            Min = sum(tmp)
                        else:
                            Min = min(Min, sum(tmp))
                        i += 1
    
    return Min




