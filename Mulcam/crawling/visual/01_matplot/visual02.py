import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [1,2,3,4,5]
y01 = list(map(lambda x : x**2, x))
y02 = list(map(lambda x : x**3, x))

ax.plot(x, y01, color='red', label='pow2')
ax.plot(x, y02, color='blue', label='pow3')

plt.legend()

plt.show()