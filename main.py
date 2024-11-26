import numpy as np
import matplotlib.pyplot as plt


def radioactive_decay(N0, half_life, time_points):
    """
    Simulates radioactive decay over time.
    
    Parameters:
    - N0: Initial number of radioactive particles
    - half_life: Half-life of the substance
    - time_points: Array of time values to evaluate
    
    Returns:
    - N: Array of remaining radioactive particles at each time point
    """
    decay_constant = np.log(2) / half_life  # Calculate decay constant
    N = N0 * np.exp(-decay_constant * time_points)  # General solution
    return N

# Parameters
N0 = 1000  # Initial number of radioactive particles
half_life = 5  # Half-life in the same time units as 'time_points'
time_points = np.linspace(0, 20, 100)  # Time points from 0 to 20 in 100 steps

# Compute decay
N = radioactive_decay(N0, half_life, time_points)

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(time_points, N, label="Radioactive Decay", color="blue")
plt.axhline(N0 / 2, color="red", linestyle="--", label="Half-life Level")
plt.title("Radioactive Decay Curve")
plt.xlabel("Time")
plt.ylabel("Number of Radioactive Particles (N)")
plt.legend()
plt.grid()
plt.show()