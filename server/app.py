from flask import Flask, render_template, jsonify, request
from realtimeastronomy.tester import calc
from flask_cors import CORS, cross_origin
from datetime import datetime
from time import gmtime
import time

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True

@app.route('/api/calculations/all', methods=[GET])
def retrieve_all():
    return calc()

if __name__ == '__main__':
    app.run(debug=True)
