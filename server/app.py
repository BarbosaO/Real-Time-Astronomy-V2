from flask import Flask, render_template, jsonify, request
from calculations.tester import (
        calc, 
        getAllData, 
        getHelioData, getGeoData, 
        getMiHelioDistances, 
        getKmHelioDistances, 
        getAuHelioDistances, 
        getMiGeoDistances, 
        getKmGeoDistances, 
        getAuGeoDistances
    )
from flask_cors import CORS, cross_origin
from datetime import datetime
from time import gmtime
import time
import json

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True

# gets all calculation data
@app.route('/api/calculations/all', methods=['GET'])
def retrieve_all():
    calculations = calc()
    return getAllData(calculations)

# gets heliocentric distances in miles
@app.route('/api/calculations/heliocentric/distances/mi', methods=['GET'])
def retrieve_distances_mi():
    calculations = calc()
    return getMiHelioDistances(calculations)

# gets heliocentric distances in kilometers
@app.route('/api/calculations/heliocentric/distances/km', methods=['GET'])
def retrieve_helio_distances_km():
    calculations = calc()
    return getKmHelioDistances(calculations)

# gets heliocentric distances in astronomical units
@app.route('/api/calculations/heliocentric/distances/au', methods=['GET'])
def retrieve_helio_distances_au():
    calculations = calc()
    return getAuHelioDistances(calculations)

# gets geocentric distances in miles
@app.route('/api/calculations/geocentric/distances/mi', methods=['GET'])
def retrieve_helio_distances_mi():
    calculations = calc()
    return getMiGeoDistances(calculations)

# gets geocentric distances in kilometers
@app.route('/api/calculations/geocentric/distances/km', methods=['GET'])
def retrieve_geo_distances_km():
    calculations = calc()
    return getKmGeoDistances(calculations)

# gets geocentric distances in astronomical units
@app.route('/api/calculations/geocentric/distances/au', methods=['GET'])
def retrieve_geo_distances_au():
    calculations = calc()
    return getAuGeoDistances(calculations)

# gets all heliocentric calcualtion data 
@app.route('/api/calculations/heliocentric', methods=['GET'])
def retrieve_geo_helio_data():
    calculations = calc()
    return getHelioData(calculations)

# get all geocentric calculation data
@app.route('/api/calculations/geocentric', methods=['GET'])
def retrieve_geo_data():
    calculations = calc()
    return getGeoData(calculations)

if __name__ == '__main__':
    app.run(debug=True)
