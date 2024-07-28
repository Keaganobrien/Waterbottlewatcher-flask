from flask import Flask, jsonify, render_template
import requests

app = Flask('waterbottlewatch')

def fetch_top_water_bottle():
    # Example of fetching data from a hypothetical API
    response = requests.get('https://api.example.com/top-water-bottle')
    return response.json()

@app.route('/')
def home():
    top_bottle = fetch_top_water_bottle()
    return render_template('index.html', bottle=top_bottle)

@app.route('/api/top-bottle')
def top_bottle():
    top_bottle = fetch_top_water_bottle()
    return jsonify(top_bottle)

if __name__ == '__main__':
    app.run(debug=True)
