from flask import Flask, render_template, jsonify, request
from calculations.tester import calc, getAllData, getHelioData, getGeoData, getMiDistances, getKmDistances, getAuDistances
from flask_cors import CORS, cross_origin
from datetime import datetime
from time import gmtime
import time
import json

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True

# gets all calculation data
@app.route('/api/calculations/allc', methods=['GET'])
def retrieve_all():
    calculations = calc()
    return getAllData(calculations)

# gets all distances in miles
@app.route('/api/calculations/distances/mi', methods=['GET'])
def retrieve_distances_mi():
    calculations = calc()
    return getMiDistances(calculations)

# gets all distances in kilometers
@app.route('/api/calculations/distances/km', methods=['GET'])
def retrieve_distances_km():
    calculations = calc()
    return getKmDistances(calculations)

# gets all distances in astronomical units
@app.route('/api/calculations/distances/au', methods=['GET'])
def retrieve_distances_au():
    calculations = calc()
    return getAuDistances(calculations)

# gets all heliocentric calcualtion data 
@app.route('/api/calculations/heliocentric', methods=['GET'])
def retrieve_helio_data():
    calculations = calc()
    return getHelioData(calculations)

# get all geocentric calculation data
@app.route('/api/calculations/geocentric', methods=['GET'])
def retrieve_geo_data():
    calculations = calc()
    return getGeoData(calculations)

if __name__ == '__main__':
    app.run(debug=True)
