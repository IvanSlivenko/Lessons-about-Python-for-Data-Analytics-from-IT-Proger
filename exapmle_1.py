import numpy as np

salaries = np.array([10,20,30,40,50,60,70,80])

# average salary
mean_salaries = np.mean(salaries)

print("salaries", salaries)
print("----------------------")
print("mean_salaies", mean_salaries)

# max and min

max_salary = np.max(salaries)
print("max_salary",max_salary)

min_salaries = np.min(salaries)
print("min_salaries",min_salaries)

std_salary = np.std(salaries)
print("std_salary",std_salary)

above_mean = salaries[salaries > mean_salaries]
print("above_mean",above_mean)
