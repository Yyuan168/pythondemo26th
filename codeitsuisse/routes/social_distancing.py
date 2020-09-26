import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def evaluateSocialDistancing():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    test = data.get("test");

    result = solution(test)

    logging.info("My result :{}".format(result))
    return json.dumps(result);

def solution(test):
    result = {}
    for i in range(len(test)):
        num = 0
        
    
    return 1
                
                

