import plotly.express as px
import pandas as pd

data = {

    'Category': ['A','B', 'C', 'D'],
    'Values': [4500, 2500, 1053, 500]
}

#------------------------------------------------------------------------------- Кругова діаграма
df = pd.DataFrame(data)
fig = px.pie(df, values='Values', names='Category', title='Данні по категоріям')

fig.show()



