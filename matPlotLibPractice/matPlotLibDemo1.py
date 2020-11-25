import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

#FUNCTIONAL METHOD
# plt.plot(x,y,'red')
# plt.xlabel("X-Label")
# plt.ylabel("Y-Label")
# plt.title("Title")

# plt.show()

# plt.subplot(1,2,1)
# plt.plot(x,y,'r-')
# plt.subplot(1,2,2)
# plt.plot(y,x,'b-')
# #plt.show()


#CLASS

# fig = plt.figure()
# axes = fig.add_axes([0.15,0.15,.8,.8])
# axes.plot(x,y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# plt.show()

fig = plt.figure()
axes1 = fig.add_axes([0.15,0.15,.8,.8])
axes2 = fig.add_axes([0.2,0.5,.4,.4])

axes1.plot(x,y,'r')
axes1.set_title('LARGER PLOT')
axes2.set_title('SMALLER PLOT')
axes2.plot(y,x,'b')

plt.show()