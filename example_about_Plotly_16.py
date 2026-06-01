import plotly.express as px


df = px.data.gapminder()

fig = px.scatter(
    df,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    color='continent',
    hover_name='country',
    log_x=True,
    size_max=60,
    animation_frame='year',
    animation_group='country',
    title='Назва графіка',
    labels={'gdpPercap':'GDP', 'lifeExp':'Life'}
)

fig.show()


