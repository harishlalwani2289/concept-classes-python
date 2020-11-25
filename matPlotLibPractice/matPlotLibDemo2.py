import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

# fig, axes = plt.subplots(nrows=1, ncols=2)
# plt.tight_layout()
#
# axes[0].plot(x, y)
# axes[0].set_title("First")
# axes[1].set_title("Second")
# axes[1].plot(y, x)
# print(axes)
#plt.show()

# Figure size, Aspect Ratio, DPI

fig = plt.figure(figsize=(8, 2), dpi=200)
ax = fig.add_axes([0.2,0.2,0.7,0.7])
ax.plot(x,x**2, label="X-Squared")
ax.plot(x,x**3, label="X-Cubed")
ax.plot(y,y*7, label="Y-Added")
ax.set_title("Title")
ax.set_ylabel("Y-Label")
ax.set_xlabel("X-Label")

#Adding legend
ax.legend(loc=(.2,.2))
plt.show()

# fig, axes = plt.subplots(nrows=2, ncols=1,figsize=(10,6))
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.show()
#
# fig.savefig('myPicture.jpg',dpi=1000)
