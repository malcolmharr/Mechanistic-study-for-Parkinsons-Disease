import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the RMSD data
hcdr1rmsd = pd.read_csv('hcdr1rmsd1.csv')
hcdr2rmsd = pd.read_csv('hcdr2rmsd1.csv')
hcdr3rmsd = pd.read_csv('hcdr3rmsd1.csv')
lcdr1rmsd = pd.read_csv('lcdr1rmsd1.csv')
lcdr2rmsd = pd.read_csv('lcdr2rmsd1.csv')
lcdr3rmsd = pd.read_csv('lcdr3rmsd1.csv')

# Normalize the x-axis to be in units of nanoseconds as opposed to frames
timens = np.linspace(0, 1000, 4999)

# Create a figure with 2 rows and 3 columns of subplots
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
y_limits = (0,5.0)

# Plot data on each subplot
axes[0, 0].plot(timens, hcdr1rmsd, color='#aaffff')
axes[0, 0].set_title('RMSD of HCDR1')
axes[0, 0].set_xlabel('Time (ns)')
axes[0, 0].set_ylabel('RMSD (Å)')
axes[0 ,0].set_ylim(y_limits)
hcdr1_av = np.mean(hcdr1rmsd)
axes[0, 0].axhline(y=hcdr1_av, color='red', linestyle='--', label='Average')
axes[0, 0].legend()

axes[0, 1].plot(timens, hcdr2rmsd, color='#00a2a0')
axes[0, 1].set_title('RMSD of HCDR2')
axes[0, 1].set_xlabel('Time (ns)')
axes[0, 1].set_ylabel('RMSD (Å)')
axes[0 ,1].set_ylim(y_limits)
hcdr2_av = np.mean(hcdr2rmsd)
axes[0, 1].axhline(y=hcdr2_av, color='red', linestyle='--', label='Average')
axes[0, 1].legend()

axes[0, 2].plot(timens, hcdr3rmsd, color='#c8c8c5')
axes[0, 2].set_title('RMSD of HCDR3')
axes[0, 2].set_xlabel('Time (ns)')
axes[0, 2].set_ylabel('RMSD (Å)')
axes[0 ,2].set_ylim(y_limits)
hcdr3_av = np.mean(hcdr3rmsd)
axes[0, 2].axhline(y=hcdr3_av, color='red', linestyle='--', label='Average')
axes[0, 2].legend()

axes[1, 0].plot(timens, lcdr1rmsd, color='#ebeb00')
axes[1, 0].set_title('RMSD of LCDR1')
axes[1, 0].set_xlabel('Time (ns)')
axes[1, 0].set_ylabel('RMSD (Å)')
axes[1 ,0].set_ylim(y_limits)
lcdr1_av = np.mean(lcdr1rmsd)
axes[1, 0].axhline(y=lcdr1_av, color='red', linestyle='--', label='Average')
axes[1, 0].legend()

axes[1, 1].plot(timens, lcdr2rmsd, color='#6e4900')
axes[1, 1].set_title('RMSD of LCDR2')
axes[1, 1].set_xlabel('Time (ns)')
axes[1, 1].set_ylabel('RMSD (Å)')
axes[1 ,1].set_ylim(y_limits)
lcdr2_av = np.mean(lcdr2rmsd)
axes[1, 1].axhline(y=lcdr2_av, color='red', linestyle='--', label='Average')
axes[1, 1].legend()

axes[1, 2].plot(timens, lcdr3rmsd, color='#7c3600')
axes[1, 2].set_title('RMSD of LCDR3')
axes[1, 2].set_xlabel('Time (ns)')
axes[1, 2].set_ylabel('RMSD (Å)')
axes[1 ,2].set_ylim(y_limits)
lcdr3_av = np.mean(lcdr3rmsd)
axes[1, 2].axhline(y=lcdr3_av, color='red', linestyle='--', label='Average')
axes[1, 2].legend()

# Adjust spacing between subplots
fig.text(0.03, 0.96, "(e)", fontsize=12, color="black", weight="bold")
fig.suptitle('Conformational Changes of Protein', fontsize=16, weight='bold')
plt.subplots_adjust(top=0.85)
plt.tight_layout()

# Save the figure
plt.savefig('prot-rmsd.pdf', format='pdf', dpi=300)

# Create file to store average RMSD values
output_file_path = 'average_values.txt'
with open(output_file_path, 'w') as f:
    # Write the values to the file
    f.write(f"hcdr1_av: {hcdr1_av}\n")
    f.write(f"hcdr2_av: {hcdr2_av}\n")
    f.write(f"hcdr3_av: {hcdr3_av}\n")
    f.write(f"lcdr1_av: {lcdr1_av}\n")
    f.write(f"lcdr2_av: {lcdr2_av}\n")
    f.write(f"lcdr3_av: {lcdr3_av}\n")
print(f"Values saved to {output_file_path}")
