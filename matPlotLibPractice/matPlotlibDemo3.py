import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, y, color="orange", lw=4, alpha=0.2)
#ax.plot(x, y, color="orange", lw=4, linestyle="--")  # also RGB hex code
#ax.plot(x, y, color="orange", lw=4, linestyle="-.")  # also RGB hex code
#ax.plot(x, y, color="orange", lw=4, ls="steps")  # also RGB hex code

# ax.plot(x, y, color="orange", lw=1, marker="o", markersize=20,
#         markerfacecolor="blue", markeredgewidth=4,markeredgecolor="green")

ax.plot(x, y, color="orange", lw=2, linestyle="--")

# ax.set_xlim([0,2])
# ax.set_ylim([0,2])
plt.scatter(x,y)
plt.show()