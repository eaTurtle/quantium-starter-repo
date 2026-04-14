# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash()

df = pd.read_csv('C:\\dev\\quantium-starter-repo\\data\\task2.csv')

fig = px.line(df, x="date", y="sales", title="Pink morsels sales")

app.layout = html.Div(children=[
    html.H1(children='Soul Food Sales'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
