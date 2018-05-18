import os
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, jsonify, request
import dill as pickle

float_var_list = ['x1','x2']
cat_var_list = ['x3']
var_list = float_var_list + cat_var_list

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def apicall():
    
    #get json input correctly
    try:
        test_json = request.get_json()
    except Exception as e:
        raise e    
    
    #check for errors in data, first create an error response dict
    error_response = {}
    
    #loops over the keys list defined above. check if it's float for x1 and x2
    # and checks if x3 is 0 or 1. If a key error exception occurs, it's because a variable is missing
    for key in var_list:
        try:
            if (type(test_json[key]) != float) and (key in float_var_list):
                error_response[key] = '{} should be float'.format(key)
            if (test_json[key] != 0) and (test_json[key] != 1) and (key in cat_var_list):
                error_response[key] = '{} should be int'.format(key)
        except KeyError:
            error_response[key] = '{} is missing'.format(key)
    
    #if found and error, the dict is not empty, and then the API responds with appropriate error code
    if error_response:
        response = jsonify(error_response)
        response.status_code = 422
        return response
    
    #if no error found, creates a test dataframe
    test = pd.DataFrame([list(test_json.values())], columns=['x1', 'x2', 'x3'])

    if test.empty:
        return(bad_request())
    else:
        #Load the saved model
        with open('models/model_v1.pk','rb') as f:
            loaded_model = pickle.load(f)

        #does the prediction
        predictions = loaded_model.predict(test)

        #prepare the output prediction for response
        responses = jsonify({'y': str(predictions[0])})
        responses.status_code = 200

        return (responses)

#runs api on port 8080
if __name__ == '__main__':
     app.run(port=8080)