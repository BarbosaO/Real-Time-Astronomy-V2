from flask import Flask, render_template, jsonify, request
from calculations.tester import calc, getAllData, getMiDistances, getKmDistances, getAuDistances
from flask_cors import CORS, cross_origin
from datetime import datetime
from time import gmtime
import time
import json

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True

@app.route('/api/calculations/all', methods=['GET'])
def retrieve_all():
    calculations = calc()
    return getAllData(calculations)

@app.route('/api/calculations/distances/mi', methods=['GET'])
def retrieve_distances_mi():
    calculations = calc()
    return getMiDistances(calculations)

@app.route('/api/calculations/distances/km', methods=['GET'])
def retrieve_distances_km():
    calculations = calc()
    return getKmDistances(calculations)


@app.route('/api/calculations/distances/au', methods=['GET'])
def retrieve_distances_au():
    calculations = calc()
    return getAuDistances(calculations)
    

if __name__ == '__main__':
    app.run(debug=True)
