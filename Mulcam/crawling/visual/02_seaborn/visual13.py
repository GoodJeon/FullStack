import seaborn as sns
import matplotlib.pyplot as plt


penguins = sns.load_dataset('penguins')
# print(penguins)


"""
species : 종
island : 서식지
bill_length_mm : 부리의 길이
bill_depth_mm : 부리의 깊이
flipper_length_mm : 날개의 길이
body_mass_g : 체질량
sex : 성별
"""

fig = plt.figure(figsize=(10, 7))

ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(2, 2, 2)
ax03 = fig.add_subplot(2, 2, 4)

sns.histplot(data=penguins, x='body_mass_g', ax=ax01)
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', ax=ax02)

ax03.boxplot(penguins['body_mass_g'].fillna(penguins['body_mass_g'].mean()))

plt.tight_layout()


plt.show()

