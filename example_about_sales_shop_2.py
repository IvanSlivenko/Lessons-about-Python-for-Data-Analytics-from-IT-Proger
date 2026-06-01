import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# https://youtu.be/VBKzAfG5D0M

products_ids = np.array([101,102,103,104,105])
prices = np.array([10.99, 20.99, 30.99, 40.99, 50.99])
quantities = np.array([10,20,30,40,50])

dates = np.array([
    '10-01-2026',
    '11-01-2026',
    '12-01-2026',
    '13-01-2026',
    '13-01-2026'
])

total_sales = prices * quantities
total_revenue = np.sum(total_sales)
average_check = np.mean(total_sales)

# Best and worts
best_product_index = np.argmax(total_sales)
worts_product_index = np.argmin(total_sales)

# -----------------------------------
# print("products_ids",products_ids)
# print("---------------------------")
# print("total_sales",total_sales)
# print(f"total_revenue: {total_revenue: .2f}")
# print(f"average_check: {average_check: .2f}")
#
# print(f"best product ID: {products_ids[best_product_index]} sales amount : {total_sales[best_product_index]}")
# print(f"worts product ID: {products_ids[worts_product_index]} sales amount : {total_sales[worts_product_index]}")

dates_pd = pd.to_datetime(dates, format='%d-%m-%Y')
# print("--------------------------------------  dates_pd")
# print(dates_pd)

days_of_weeks = dates_pd.day_name()
# print("-------------------------------------- days_of_weeks")

# print(days_of_weeks)

sales_by_day = dict()
for day, sale in zip(days_of_weeks, total_sales) :
    if day in sales_by_day:
        sales_by_day[day] += sale
    else:
        sales_by_day[day] = sale

# print(f"Sales per days: {sales_by_day}")

#-------------------------------------------------------------------------- Visualisation
plt.figure(figsize=(10,6))
sns.barplot(x=products_ids, y=total_sales, palette='Blues_d')
plt.xlabel('ID продукту')
plt.ylabel('Загальні продажі')

plt.title('Загальні продажі по продуктам')
plt.show()

# print(plt)
# print(type(plt))

plt.figure(figsize=(10,6))
sns.barplot(x=sales_by_day.keys(),y=sales_by_day.values(), palette='Greens_d')
plt.xlabel('Дні тижня')
plt.ylabel('Загальні продажі')
plt.title('Загальні продажі по дням тижня')

plt.show()