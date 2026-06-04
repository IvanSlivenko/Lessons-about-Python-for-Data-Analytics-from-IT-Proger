import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

df = pd.read_csv('monthly_sales.csv')

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# print(df.head())

result = seasonal_decompose(df['Sales'], model='additive', period=12)
result.plot()
plt.show()

quartely_data = df['Sales'].resample('QE').sum()
quartely_data.plot()
plt.show()

df['RollingMean'] = df['Sales'].rolling(window=3).mean()
df[['Sales','RollingMean']].plot()
plt.show()







