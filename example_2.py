import numpy as np

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
print("products_ids",products_ids)
print("---------------------------")
print("total_sales",total_sales)
print(f"total_revenue: {total_revenue: .2f}")
print(f"average_check: {average_check: .2f}")

print(f"best product ID: {products_ids[best_product_index]} sales amount : {total_sales[best_product_index]}")
print(f"worts product ID: {products_ids[worts_product_index]} sales amount : {total_sales[worts_product_index]}")


