from app import app
from flask import jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
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



@app.route('/historywaves')
def historywaves():
  data = {}

  # DUMMY STATS DATA --------------------
  history_stats = {

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


  # DUMMY HISTORY DATA  ---------------------


  # isolate cott data
  CottHeaders = ['CottHeight', 'CottPeakPeriod', 'CottDirection']
  CottData = df[CottHeaders]

  # add noise to Cott data
  mu, sigma = 0, 0.1 
  noise = np.random.normal(mu, sigma, CottData.shape)
  signal = CottData + noise

  signal.rename(columns={'CottHeight': 'CottHeightHistory', 'CottPeakPeriod': 'CottPeakPeriodHistory', 'CottDirection': 'CottDirectionHistory'}, inplace=True)
  df_horizontal_stack = pd.concat([df, signal], axis=1)

  history_data = df_horizontal_stack.to_dict(orient='records')


  # ----------------------------------------



  data['data'] = { 'history': history_data, 'summary_history': history_stats }
  data['status'] = 200

  return jsonify(data)