import matplotlib.pyplot as plt
from random import randint


fig = plt.figure()

ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(1, 2, 2)

x = [1,2,3,4,5]
y = list(randint(1, 100) for i in range(5))

ax01.bar(x, y, color='r')
ax02.barh(x, y, color='b')

plt.show()