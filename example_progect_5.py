import pandas  as pd

#--------------------------------------- Читаємо файл
df = pd.read_csv('platforms.csv')

print("-------------------------------- Data from file :")
#--------------------------------------- виводимо в консоль перші стрічки файла
print(df.head())

#--------------------------------------- Заповнюємо пусті значення стовпчика Views середніми значеннями по цьому стовпчику
df['Views'] = df['Views'].fillna(df['Views'].mean())

#--------------------------------------- Заповнюємо пусті значення стовпчика Revenue  значеннями = 0
df['Revenue'] = df['Revenue'].fillna(0)

#----------------------------------------- Видаляємо дублікати
df.drop_duplicates(inplace=True)

#----------------------------------------- Типізуємо значення змінних в стовпчику Views
df['Views'] = df['Views'].astype(int)

#------------------------------------------ Типізуємо колонку Date
df['Date'] = pd.to_datetime(df['Date'])

# print("Describe :")
# print(df.describe())

print("------------------------------------------ filtered : df[df['Platform'] == 'YouTube']")

#-------------------------------------------------- Фільтруємо по колонці "Platform"
filtered = df[df['Platform'] == 'YouTube']
print(filtered)

#--------------------------------------------------- Групуємо по колонці Date
grouped = filtered.groupby('Date').agg({'Views': 'sum','Revenue': 'sum', 'Platform': lambda x: ', '.join(x) }).reset_index()
print("------------------------------------------ grouped")
print(grouped)

#--------------------------------------------------- Обчислюємо та виводимо в Консоль Середні значення
mean_views = grouped['Views'].mean()
mean_revenue = grouped['Revenue'].mean()
print(f"-------------------------------------- Mean views : {mean_views} and  mean revenue : {mean_revenue}")


#----------------------------------------------- Зберігаємо результати обробки данних у файл
grouped.to_csv('new_data.csv', index=False)
