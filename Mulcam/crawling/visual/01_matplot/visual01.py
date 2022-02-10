import matplotlib.pyplot as plt
# pip install matplotlib

# 도화지 만들기
fig = plt.figure()

# 도화지 나누기
ax = fig.subplots()

ax.plot([1,2,3,4,5])

plt.show()