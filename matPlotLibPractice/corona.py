# import matplotlib.pyplot as plt
#
# x = ["April","May","June"]
# y = [100,120,130]
#
# plt.plot(x,y)
# plt.show()

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, .8, .8])
x = ["April", "May", "June"]
y = [100, 120, 130]
ax.bar(x, y)
plt.show()
