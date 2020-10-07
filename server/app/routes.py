from app import app
from flask import jsonify, request
from flask_cors import CORS
import pandas as pd
import json

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
@app.route('/index')
def index():
  message = {}
  data = {}

  message['message'] = 'Hello World from Flask!'
  data['status'] = 200
  data['data'] = message

  return jsonify(data)


@app.route('/d3')
def d3():
  data = {}

  df = pd.read_csv('data/d3DemoData/cities.csv')
  chart_data = df.to_dict(orient='records')

  data['data'] = chart_data
  data['status'] = 200

  return jsonify(data)


@app.route('/oceanwaves')
def oceanwaves():
  data = {}

  # DUMMY STATS DATA --------------------
  stats = {
    'day': {
      'confidence': 92,
      'maxWaveHeight': 1.16,
      'maxWavePeriod': 27.1
      },
    'week': {
      'confidence': 92,
      'maxWaveHeight': 0.98,
      'maxWavePeriod': 19.0
    },
    'month': {
      'confidence': 92,
      'maxWaveHeight': 1.1,
      'maxWavePeriod': 23.23
    },
    'confidence': {
        'waveHeight': 92.3,
        'peakPeriod': 89.60,
        'direction': 87.3
    }
  }
  # -------------------------------------

  df = pd.read_csv('data/ocean-waves.csv')
  chart_data = df.to_dict(orient='records')

  data['data'] = { 'data': chart_data, 'summary': stats }
  data['status'] = 200

  return jsonify(data)