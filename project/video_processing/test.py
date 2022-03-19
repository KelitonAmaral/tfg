import numpy as np
import matplotlib.pyplot as plt


coordinates = [[1, 2],[1, 4],[1, 6],[1, 8]]
x = []
y = []
for a,b in coordinates:
    x.append(a)
    y.append(b)
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# # print(x)
# # print(y)
plt.plot(x, y)
plt.show()
# The explicit (object-oriented) API is recommended for complex plots, 
# though pyplot is still usually used to create the figure and often 
# the axes in the figure. 
# See .pyplot.figure, .pyplot.subplots, and .pyplot.subplot_mosaic 
# to create figures, and Axes API <../axes_api> for the plotting methods on an axes:

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)
# # ax.show()