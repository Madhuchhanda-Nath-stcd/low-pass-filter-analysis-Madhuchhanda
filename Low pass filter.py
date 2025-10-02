import matplotlib.pyplot as plt
import numpy as np

# Data from table
frequency = np.array([100, 500, 1000, 2000, 5000, 10000])  # Hz
gain_db = np.array([-3.63, -16.83, -22.61, -28.36, -35.51, -41.16])  # dB

# Plot
plt.figure(figsize=(8,5))
plt.semilogx(frequency, gain_db, marker="o", linewidth=2, label="Measured Gain")
plt.axhline(-3, color="red", linestyle="--", label="-3 dB cutoff reference")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.title("Low-Pass Filter Frequency Response")
plt.grid(True, which="both", ls="--", lw=0.7)
plt.legend()
plt.show()
