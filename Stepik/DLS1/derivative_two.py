import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 4*x**2 - 3*x + 5


x = np.linspace(-10, 10, 300)
y = list(map(f, x))

plt.figure(figsize=(10, 7))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.scatter([3/8], [f(3/8)], lw=5)
plt.show()
