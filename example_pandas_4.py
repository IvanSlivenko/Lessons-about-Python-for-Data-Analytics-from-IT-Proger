import pandas  as pd

data = {
    'Name' : ['Jon', 'Anna', 'Peter', 'Alex'],
    'Age' : [10,20,30,40],
    'City' : ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

#------------------------------------- Заміна пусто на 0
df.fillna(0,inplace=True)

#----------------------------------------------- Видалити пусті ряди
df.dropna(inplace=True)


#----------------------------------------------- Видалити дублікати
df.drop_duplicates(inplace=True)

#----------------------------------------------- Зміна типів
df['Age'] = df['Age'].astype(int)

#----------------------------------------------- Групування
grouped = df.groupby('Age').sum()

print(df)
print('----------------------------------')
print(grouped)



