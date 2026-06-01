import plotly.express as px
import  pandas as pd

data = {
    'Country': ['USA', 'Canada', 'Mexico'],
    'Population' : [331, 38, 128]
}

#------------------------------------------------------------------------------- Стовпчикова діаграма
# df = pd.DataFrame(data)
# fig = px.bar(df, x='Country', y='Population', title='Popupation in country')

#------------------------------------------------------------------------------- Графік
df = px.data.gapminder().query("country == 'Canada'")
fig = px.line(df, x='year', y='gdpPercap', title='GDP per Canada')

fig.show()



