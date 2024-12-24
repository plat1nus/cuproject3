import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import requests

app = dash.Dash(__name__)

# Пример данных о погоде
data = {
    'date': ['2024-12-20', '2024-12-21', '2024-12-22'],
    'temperature': [5, 7, 3],
    'wind_speed': [10, 15, 20],
    'precipitation_probability': [20, 50, 80]
}
df = pd.DataFrame(data)

# Создание графиков
fig_temp = px.line(df, x='date', y='temperature', title='Температура по дням')
fig_wind = px.line(df, x='date', y='wind_speed', title='Скорость ветра по дням')
fig_precip = px.line(df, x='date', y='precipitation_probability', title='Вероятность осадков по дням')

app.layout = html.Div(children=[
    html.H1(children='Прогноз погоды'),

    dcc.Graph(
        id='temperature-graph',
        figure=fig_temp
    ),

    dcc.Graph(
        id='wind-speed-graph',
        figure=fig_wind
    ),

    dcc.Graph(
        id='precipitation-graph',
        figure=fig_precip
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
