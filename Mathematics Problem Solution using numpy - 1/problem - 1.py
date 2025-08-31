import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Question 1
# Function: y = e^(-x/10) * sin(x)
# Consider 10,000 equally spaced points for x in [0, 10]
# --------------------------

# --------------------------
# Task 1: Plot y vs x
# --------------------------
N = 10000                     # Number of intervals
x = np.linspace(0, 10, N+1)   # 10,001 points from 0 to 10
y = np.exp(-x/10) * np.sin(x) # Function values

plt.figure(figsize=(8,4))
plt.plot(x, y, label='y=e^(-x/10)*sin(x))')
plt.grid(True)
plt.legend()
plt.show()

# --------------------------
# Task 2: Compute mean and standard deviation for x in [4, 7]
# --------------------------
print(np.mean(y[(x>=4)*(x<=7)]))  # Mean
print(np.std(y[(x>=4)*(x<=7)]))   # Standard deviation

# --------------------------
# Task 3: Find 80th percentile of y in [4,7]
# --------------------------
print(np.percentile(y[(x>=4)*(x<=7)], 80))  # 80th percentile

# --------------------------
# Task 4: Plot dy/dx vs x
# --------------------------
dydx = np.gradient(y, x)  # Numerical derivative of y w.r.t x
plt.plot(x, dydx)

# --------------------------
# Task 5: Find locations where dy/dx = 0 (local maxima and minima)
# --------------------------
# Sign change in derivative indicates a local extremum
print(x[1:][dydx[1:] * dydx[:-1] < 0])