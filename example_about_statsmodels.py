import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df.head())

result = seasonal_decompose(df['Value'], model='additive', period=7)
result.plot()
# plt.show()

monthly_data = df['Value'].resample('ME').sum()

weekly_data = df['Value'].resample('W').sum()

print(monthly_data.head())
print(weekly_data.head())

df['RollingMean'] = df['Value'].rolling(window=7).mean()
df[['Value','RollingMean']].plot()
plt.show()







