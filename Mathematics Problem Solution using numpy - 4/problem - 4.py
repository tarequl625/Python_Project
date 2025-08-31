# -------------------------------------------------------
# Question 4: Energy Emitted by a Star
# -------------------------------------------------------
# Description:
# The power emitted by a blackbody star is given by:
#   P = A * sigma * epsilon * T^4
#   where:
#       A       = surface area of the star
#       sigma   = Stefan-Boltzmann constant
#       epsilon = emissivity of the star
#       T       = temperature of the star
#
# The star's temperature varies with time as:
#   T(t) = T0 / (1 + exp(-k*t))
#       T0 = maximum temperature
#       k  = constant
#
# Tasks:
# 1. Compute instantaneous power P(t) as a function of time.
# 2. Compute the total energy emitted up to time t:
#    E(t) = ∫ P(t') dt' from t'=0 to t'=t
# 3. Plot E(t) vs time t.
# -------------------------------------------------------

kt = np.linspace(0, 3, 100)              # Generate 100 points from kt=0 to kt=3
P = (1/(1+np.exp(-kt)))**4               # Instantaneous power (normalized)
E = np.cumsum(P) * (kt[1]-kt[0])         # Cumulative sum for total energy (numerical integration)

plt.figure(figsize=(8,4))
plt.plot(kt, E, label='Total Energy E(kt)')
plt.legend()
plt.show()