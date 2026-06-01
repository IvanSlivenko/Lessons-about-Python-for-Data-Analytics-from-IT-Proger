import plotly.express as px


df = px.data.iris()

fig=px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Інформація про iris')

fig.show()



