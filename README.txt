This is README for Loadsmart Data Scientist Challenge.

This challenge is divided in two goals:

GOAL 1: Create a prediction model for provided data

- Provided data is saved on folder data/
- loadsmart.ipynb is a Jupyter Notebook that runs all exploratory analysis, creation of the prediction model, and test the API on check_data.csv.
- loadsmart.html is the html version of the Jupyter Notebook, if someone wants to just read my solution
- The predictions for check_data is saved on data/check_data_predicted.csv

GOAL 2: Create an API that checks for data errors and use a trained model for prediction

- To run the API, you just need to run
	python run_api.py
  and create a post request in any language to http://127.0.0.1:8080/ with a json paylod as: {'x1': value, 'x2': value, 'x3': value}
- flask_api.ipynb is the Jupyter Notebook flavor for the API code
