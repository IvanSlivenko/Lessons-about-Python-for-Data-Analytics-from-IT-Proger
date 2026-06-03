from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

data = {
    'Country': ['USA', 'Canada', 'Mexico'],
    'Population' : [331, 38, 128]
}

df = pd.DataFrame(data)

fig = px.bar(df, x='Country', y='Population', title='Population by country')

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello App'),

    html.Div(children='''
        A web app framework
    '''),

    dcc.Dropdown(
      options=[
          {'label': 'USA', 'value': 'USA'},
          {'label': 'Canada', 'value': 'Canada'},
          {'label': 'Mexico', 'value': 'Mexico'}
      ],
        value='USA'
    ),

    dcc.Graph(
        id='my-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)


