import numpy as np
import matplotlib.pyplot as plt

# Parameters (same as before)
P_CS = 1000
P_CC_monthly = 50
P_CC_24mo = P_CC_monthly * 24

# Create a range of CC subscribers (0 to 1 million)
cc_subs = np.linspace(0, 1_000_000, 500)

# Revenue from CC over 24 months
rev_cc = cc_subs * P_CC_24mo

# Revenue from old CS model over the same 24 months
# (how many full-price upgrades Adobe would need to match CC revenue)
cs_upgraders_needed = rev_cc / P_CS

# Plot
plt.figure(figsize=(10, 6.5))

plt.plot(cc_subs / 1e6, cs_upgraders_needed / 1e6, 
         color='#E63946', linewidth=4.5, label='Break-even line')

# Fill the two regions for instant visual impact
plt.fill_between(cc_subs / 1e6, cs_upgraders_needed / 1e6, 1.0, 
                 color='#457B9D', alpha=0.7, label='Old CS model wins (higher revenue)')
plt.fill_between(cc_subs / 1e6, 0, cs_upgraders_needed / 1e6, 
                 color='#A8DADC', alpha=0.6, label='CC wins (higher revenue)')

# Labels & title
plt.xlabel('Creative Cloud Subscribers (millions)', fontsize=13)
plt.ylabel('CS Upgraders \n(millions per 24-month cycle)', fontsize=13)
plt.title('Adobe Revenue Trade-off: Creative Cloud vs. Perpetual License Upgrades\n', 
          fontsize=15, pad=20)

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12, loc='upper left')

# Key insight annotation
'''
plt.annotate('Adobe only needs ~417k CC subscribers\n'
             '(out of ~1M total users) to break even.\n'
             'Everything above this line = pure profit upside',
             xy=(0.42, 0.52), xytext=(0.55, 0.75),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
             fontsize=12, bbox=dict(boxstyle="round,pad=0.4", facecolor="wheat", alpha=0.8))
'''
plt.tight_layout()
plt.show()
