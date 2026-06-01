import seaborn as sns

import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

#------------------------------------------------------------- Стовпчата діаграма
# sns.histplot(df['sepal_length'], kde=True)
# plt.title('Розподіл довжин чисел')

#------------------------------------------------------------- Точкова діаграма
# sns.regplot(x='sepal_length', y='sepal_width', data=df)
# plt.title('Лінійна залежність довжини від ширини')

#------------------------------------------------------------- Коробочна діаграма
# sns.boxplot(x='species', y='petal_length', data=df)
# plt.title('Розподіл довжини пелюстків')

#------------------------------------------------------------- Кореляція - ступінь взаємозв'язку між двома зміними
#------------------------------------------------------------- Теплова діагарама
# corr = df.corr(numeric_only=True)
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Кореляційна матриця')
#

#--------------------------------------------------------
sns.pairplot(df,hue='species')
plt.title("Взаэмозв'язок всіх ознак")


plt.show()