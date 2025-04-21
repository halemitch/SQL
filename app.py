from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

app = Flask(__name__)
API_TOKEN = "supersecrettoken123"

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

@app.route('/api/time')
@token_required
def returns_capital():
    capital = request.args.get('capital', None)
    if not capital:
        return jsonify({"error": "No capital provided"}), 400

    try:
        with open('timezones.json', 'r') as f:
            data = json.load(f)
        timezones = pd.DataFrame(data)
        timezones['city'] = timezones['name'].str.split('/', expand=True)[1]

        with open('capitals.json', 'r') as f:
            data = json.load(f)
        capitals = pd.DataFrame(data)

        if capital not in capitals['city'].values:
            return jsonify({"error": "This capital does not exist in this data frame. Please try another capital or check your spelling"}), 404

        merged = pd.merge(timezones, capitals, on='city', how='inner')
        merged['hours'] = merged['offset'].astype(int) / 60

        city_time = merged.loc[merged['city'].str.lower() == capital.lower(), 'hours']
        if city_time.empty:
            return jsonify({"error": "Capital not found in timezones data"}), 404

        formatted_utc = datetime.utcnow()
        local_time = formatted_utc + timedelta(hours=city_time.iloc[0])
        return jsonify({
            "capital": capital,
            "local_time": local_time.strftime("%Y-%m-%d %H:%M:%S")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
