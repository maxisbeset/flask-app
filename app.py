# app.py
from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)
pytrends = TrendReq(hl='en-US', tz=360)

@app.route('/trending', methods=['GET'])
def get_trending():
    try:
        # Trending searches worldwide
        trending_searches_df = pytrends.trending_searches(pn='united_states')
        trends = trending_searches_df[0].tolist()
        return jsonify({'trending': trends})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
