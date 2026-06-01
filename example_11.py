import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

plt.plot(x,  y1, label='Squares', color= 'blue', linestyle='-', marker='o' )
plt.plot(x,  y2, label='Back Squares', color= 'red', linestyle='--', marker='s' )

plt.xlabel('Вісь X', fontsize=12)
plt.ylabel('Вісь Y', fontsize=12)
plt.title('Приклад комбінування графіка', fontsize=14)

plt.legend(loc='upper right')

plt.grid(True, linestyle='--', color='grey')

plt.savefig('combined.png', dpi=300)


# plt.show()