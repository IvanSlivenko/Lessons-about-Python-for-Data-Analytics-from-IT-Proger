import matplotlib.pyplot as plt

# plt.plot(
#     [1, 2, 3, 4],
#     [10, 20, 25, 30],
#     label='Example line',
#     color='blue',
#     linestyle='--',
#     marker='o'
# )


# fig = plt.figure(figsize=(8, 6), dpi=100, facecolor='grey')

# plt.scatter([1,2,3,4], [10, 20, 25, 30], color='gray', s=100, alpha=0.5)

# plt.bar(['A', 'B', 'C', 'D'], [10, 20, 26, 36], color='grey',width=0.5 )

# plt.hist([10,20,30,30,30,40,50], bins=5, color='purple', alpha = 0.7)

# plt.boxplot([10,20,30,30,30,40,50], vert=True, patch_artist=True)
# plt.xlabel('Вісь X', fontsize=14)
# plt.ylabel('Вісь Y', fontsize=14)
# plt.title('Заголовок діагарми', fontsize=16)

plt.plot([1,2,3],[4,5,6], label = 'Line 1')
plt.plot([1,2,3],[4,5,6], label = 'Line 2')
plt.legend(loc='upper right')

plt.grid(True, which = 'both', linestyle = '--', color = 'grey')
plt.xlim(0, 2)
plt.ylim(0, 10)


# plt.show()
plt.savefig('plot.png',dpi=300 )