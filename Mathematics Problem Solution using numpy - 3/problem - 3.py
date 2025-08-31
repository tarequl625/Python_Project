import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Flower Petal Curve Analysis
# Polar curve: r(theta) = 1 + 3/4 * sin(3*theta)
# Range: 0 <= theta <= 2*pi
# -------------------------------------------------------

# Task 1: Plot the flower
# - Convert polar coordinates (r, theta) to Cartesian (x, y)
# - x = r * cos(theta), y = r * sin(theta)
# - Plot the curve using matplotlib

theta = np.linspace(0, 2*np.pi, 10000)  # 10,000 points for smooth curve
r = 1 + 3/4 * np.sin(3*theta)           # Polar function r(theta)
x = r * np.cos(theta)                    # Convert to Cartesian x
y = r * np.sin(theta)                    # Convert to Cartesian y

plt.plot(x, y)
plt.title("Flower Petal Curve: r = 1 + 3/4*sin(3*theta)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# -------------------------------------------------------
# Task 2: Compute the area enclosed by the flower petal
# - Use polar area formula: A = 1/2 * ∫ r^2 dtheta from 0 to 2*pi
# - Two numerical methods shown:
#   1. Simple Riemann sum approximation: sum(r**2) * delta_theta
#   2. Trapezoidal rule using np.trapz
# -------------------------------------------------------

# Delta theta between points
delta_theta = theta[1] - theta[0]

# Area using simple sum (Riemann sum)
area_sum = 1/2 * sum(r**2) * delta_theta
print("Area (Riemann sum):", area_sum)

# Area using trapezoidal integration (more accurate)
area_trapz = 0.5 * np.trapz(r**2, theta)
print("Area (Trapezoidal rule):", area_trapz)

# -------------------------------------------------------
# Task 3: Compute the arclength of the curve
# - Use polar arclength formula: 
#   L = ∫ sqrt(r^2 + (dr/dtheta)^2) dtheta from 0 to 2*pi
# - dr/dtheta is computed numerically using np.gradient
# - Multiply by delta_theta for numerical integration
# -------------------------------------------------------

dr_dtheta = np.gradient(r, theta)                 # Numerical derivative
arc_length = sum(np.sqrt(r**2 + dr_dtheta**2)) * delta_theta
print("Arclength of the flower petal curve:", arc_length)