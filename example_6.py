import pandas as pd

data= {'Age' : [34,37,13,64,37,47,24,38, 26, 41,19, 51,44]}

df = pd.DataFrame(data)
print(df)
print("------------")

mean_age = df['Age'].mean()
print(f"Average : {mean_age}")

#--------------------------------------- median - центральне значення в данних
median_age = df["Age"].median()
print(f"Median  : {median_age}")

#---------------------------------------mode - значення, що зустрічається найчастіше
mode_age = df['Age'].mode()[0]
print(f"Mode: {mode_age}")

#--------------------------------------- var - розброс
variance_age = df['Age'].var()
print(f"Variance : {variance_age}")

#--------------------------------------- standart - корінь з  розброса
std_age = df['Age'].std()
print(f"Variance: {variance_age} and Standart: {std_age}")

#--------------------------------------- quantile - належність данних до сегментів , percentile - значення, що перебувають нижче певного відсотка
quantiles_age = df['Age'].quantile([0.25,0.5,0.75])
percentile_age = df['Age'].quantile(0.9)
print(f"quantiles_age:   {quantiles_age}" )
print(f"Pecentile_age {percentile_age}" )

