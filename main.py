import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def g(y, x):
    y0 = y[0]
    y1 = y[1]
    y2 = ((3 * x + 2) * y1 + (6 * x - 8) * y0) / (3 * x - 1)
    return y1, y2


# Initial conditions on y, y' at x=0
init = 2.0, 3.0
# First integrate from 0 to 2
X = np.linspace(0, 2, 100)
sol = odeint(g, init, X)
# Then integrate from 0 to -2
plt.plot(X, sol[:, 0], color='b')
X = np.linspace(0, -2, 100)
sol = odeint(g, init, X)
plt.plot(X, sol[:, 0], color='b')

# The analytical answer in red dots
exact_x = np.linspace(-2, 2, 10)
exact_y = 2 * np.exp(2 * exact_x) - exact_x * np.exp(-exact_x)
plt.plot(exact_x, exact_y, 'o', color='r', label='exact')
plt.legend()

plt.show()
