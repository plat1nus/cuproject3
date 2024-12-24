from flask import Flask, render_template, request, jsonify
import requests

from check_weather import check_bad_weather

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_weather', methods=['POST'])
def check_weather():
    try:
        temperature = float(request.form['temperature'])
        wind_speed = float(request.form['wind_speed'])
        precipitation_probability = float(request.form['precipitation_probability'])
        humidity = float(request.form['humidity'])

        result = check_bad_weather(temperature, wind_speed, precipitation_probability, humidity)

        return render_template('index.html', result=result)

    except ValueError:
        return render_template('index.html', result='Ошибка: введены некорректные данные.')

if __name__ == '__main__':
    app.run(debug=True)    

