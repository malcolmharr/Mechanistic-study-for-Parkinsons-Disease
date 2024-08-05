import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import MDAnalysis as mda
from MDAnalysis.analysis.hydrogenbonds import HydrogenBondAnalysis as hba
import pandas as pd
from matplotlib.ticker import MultipleLocator
import os
import glob

# Set variables for psf and dcd files
psf_path = '../../prot_2KKW_mod.psf'
dcd_path = '../dehydrate/nw_prot_ion_prod.dcd'

# Load your universe (example file path, replace with your actual file)
u = mda.Universe(psf_path, dcd_path)

# Perform hydrogen bond analysis

hbonds = hba(
    universe=u,
    between=[['segid A and (resid 100:140)', 'segid H'], ['segid A and (resid 100:140)', 'segid L']])

chainA_hydrogens_sel = hbonds.guess_hydrogens("segid A and (resid 100:140)")
chainA_acceptors_sel = hbonds.guess_acceptors("segid A and (resid 100:140)")

chainH_hydrogens_sel = hbonds.guess_hydrogens("segid H")
chainH_acceptors_sel = hbonds.guess_acceptors("segid H")

chainL_hydrogens_sel = hbonds.guess_hydrogens("segid L")
chainL_acceptors_sel = hbonds.guess_acceptors("segid L")

hbonds.hydrogens_sel = f"({chainA_hydrogens_sel}) or ({chainH_hydrogens_sel}) or ({chainL_hydrogens_sel})"
hbonds.acceptors_sel = f"({chainA_acceptors_sel}) or ({chainH_acceptors_sel}) or ({chainL_acceptors_sel})"
hbonds.run()

# Extract the results into a DataFrame
results = hbonds.results['hbonds']

dataframes_list = []
for entry in results:
    df = pd.DataFrame([entry], columns=['Frame', 'Donor', 'Hydrogen', 'Acceptor', 'Distance', 'Angle'])
    dataframes_list.append(df)

print(dataframes_list[0])
num_entries = len(dataframes_list)
print("Number of entries in list: ",num_entries)

hbond_df = pd.concat(dataframes_list, ignore_index=True)
hbond_df.to_csv("hbonds.csv", index=False)
print("All dataframes have been saved to hbonds.csv")

# Function to reverse lookup residue, chain, residue number, and atom name information for a given atom index
def get_atom_info(atom_index):
    atom = u.atoms[atom_index]
    residue = atom.residue
    return residue.resname, residue.segid, residue.resnum

# Function to get donor and acceptor information for each row in the DataFrame
def get_donor_acceptor_info(row):
    donor_residue, donor_chain, donor_residue_number = get_atom_info(int(row['Donor']))
    acceptor_residue, acceptor_chain, acceptor_residue_number = get_atom_info(int(row['Acceptor']))
    donor_info = f"{donor_residue}:{donor_chain}:{donor_residue_number}"
    acceptor_info = f"{acceptor_residue}:{acceptor_chain}:{acceptor_residue_number}"
    return donor_info, acceptor_info

# Add donor and acceptor columns to the DataFrame
hbond_df['Donor_Info'], hbond_df['Acceptor_Info'] = zip(*hbond_df.apply(get_donor_acceptor_info, axis=1))

hbond_df['Donor_Acceptor'] = dataframe['Donor_Info'] + ' - ' + dataframe['Acceptor_Info']
    
# Find the most common donor-acceptor pairs
most_common_entries = hbond_df['Donor_Acceptor'].value_counts()

output_file = "hbonds.txt"
with open(output_file, 'w') as f:
	f.write("Most Common Hydrogen Bonds:\n")
	for entry, count in most_common_entries.items():
		f.write(f"{entry}: {count}\n")
print(f"Most common hydrogen bonds saved to {output_file}")
