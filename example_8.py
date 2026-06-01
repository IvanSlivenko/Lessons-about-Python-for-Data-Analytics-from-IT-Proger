from scipy import stats

group1 = [23,25,31,35,45]
group2 = [45,51,61,35,23]

stat, p_value = stats.mannwhitneyu(group1, group2)

print(f"U-stats: {stat}, P-value: {p_value}")

# Якщо P_value маленьке, то різниця між вибірками - значне.

