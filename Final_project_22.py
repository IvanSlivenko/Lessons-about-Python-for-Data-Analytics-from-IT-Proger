import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data.csv')

print(df.head())
print(df.isnull().sum())
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Date'] = pd.to_datetime(df['Date'])
# df.drop(columns=['Unnamed: 0'], inplace=True)
df.drop(columns=['Unnamed: 0'], errors='ignore', inplace=True)
print(df.describe())

sales_by_category = df.groupby('Category')['Sales'].sum()
print('----------------------------- Sales_by_category')
print(sales_by_category)

sales_by_date = df.groupby('Date')['Sales'].sum()
print('---------------------------- Sales_by_date')
print(sales_by_date)

sales_by_category.plot(kind='bar', title = 'Продажі за категоріями')
plt.ylabel('Загальні продажі')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sales_by_date, marker='o', linestyle='-')
plt.title('Продажі по періодам')
plt.xlabel('Дата')
plt.ylabel('Продажі')
plt.grid(True)
plt.show()









# df['Date'] = pd.to_datetime(df['Date'])
# df.set_index('Date', inplace=True)
#
#
#
# result = seasonal_decompose(df['Sales'], model='additive', period=12)
# result.plot()
# plt.show()
#
# quartely_data = df['Sales'].resample('QE').sum()
# quartely_data.plot()
# plt.show()
#
# df['RollingMean'] = df['Sales'].rolling(window=3).mean()
# df[['Sales','RollingMean']].plot()
# plt.show()
#






