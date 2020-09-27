import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    

    result = solution(data)

    logging.info("My result :{}".format(result))
    return jsonify("result: " + result);

def solution(data):
    zero = []
    one = []
    cluster = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] != "*":
                if len(cluster) == 0:
                    cluster.append([(row, col)])
                # else:
                #     if abs(cluster[-1][1] - col):

                if data[row][col] == '0':
                    zero.append((row,col))
                else:
                    one.append((row, col))
    
    return 1
                
                

