import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

# Parameters
# Parameters
N = 1_000_000           # hypothetical total addressable users
P_CS = 1000             # upgrade price paid by CS customers every 24 months
P_CC = 50               # monthly CC price → $600/year → $1200 over 24 months
T = 24                  # time horizon in months

# Grids
x_vals = np.linspace(0, N, 100)
y_vals = np.linspace(0, N, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Revenue calculations (in $ over 24 months)
R_CS = Y * P_CS
R_CC = X * P_CC * T

# Revenue difference surface (CC revenue minus old CS upgrade revenue)
Z = (R_CC - R_CS) / 1e6  # in millions of dollars

# Convert to millions of users for nicer axes
X_millions = X / 1e6
Y_millions = Y / 1e6

# Create the 3D figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
surf = ax.plot_surface(X_millions, Y_millions, Z, cmap='viridis', alpha=0.85, linewidth=0, antialiased=True)

# Intersection line: where CC revenue = CS upgrade revenue → Z = 0
# Solved: X * 50 * 24 = Y * 1000  →  Y = 1.2 * X
x_line = np.linspace(0, N, 200)
y_line = 1.2 * x_line
z_line = np.zeros_like(x_line)  # Z = 0 on the break-even plane

ax.plot(x_line/1e6, y_line/1e6, z_line,
        color='red', linewidth=4, label='Break-even line (CC revenue = CS revenue)')

# Formatting
ax.set_xlabel('CC Subscribers (millions)', fontsize=12, labelpad=10)
ax.set_ylabel('CS Upgraders (millions per 24-month cycle)', fontsize=12, labelpad=10)
ax.set_zlabel('Revenue Difference (CC − CS) over 24 months [$M]', fontsize=12, labelpad=10)
ax.set_title('Adobe Revenue Trade-off: Creative Cloud vs. Perpetual Upgrades\n'
             'Red line = point of revenue indifference', fontsize=14, pad=20)

ax.legend(loc='upper left')
ax.view_init(elev=25, azim=135)

# Color bar
fig.colorbar(surf, shrink=0.5, aspect=15, label='Revenue Advantage to CC [$M]')

plt.tight_layout()
plt.show()
