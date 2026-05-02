"""
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()


categories = ['A', 'B', 'C']
values = [10, 20, 15]

plt.barh(categories, values)
plt.title("Horizontal Bar Chart")
plt.show()



data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4)
plt.title("Histogram")
plt.show()


x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()
"""


"""
import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]

plt.pie(sizes)
plt.title("Pie Chart")
plt.show()
"""

import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(size=100), np.random.normal(size=100)]

plt.boxplot(data)
plt.title("Box Plot")
plt.show()
