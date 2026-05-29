import pandas  as pd

# https://youtu.be/iX28sWsAT4Y

# ----------------------------------------------
# 00 : 03 : 14

data = {
    'Name' : ['Jon', 'Anna', 'Peter', 'Alex'],
    'Age' : [10,20,30,40],
    'City' : ['New York', 'Paris', 'Berlin', 'London']
}

# ds = pd.Series(data)
#
# print("------------------------------- Series")
# print("ds",ds)

df = pd.DataFrame(data)

print("------------------------------- DataFrame")
print(df)

print("------------------------------- DataFrame['key']")
print(df['Name'])
print('------------------------------ df.loc[0]')
print(df.loc[0])

print("------------------------------ df[df['Age']>10]")
print(df[df['Age']>10])

print("------------------------------ df.head()")
print(df.head())

print("------------------------------ df.tail()")
print(df.tail())

print("------------------------------ df.describe()")
print(df.describe())

print("------------------------------ df.info()")
print(df.info())






