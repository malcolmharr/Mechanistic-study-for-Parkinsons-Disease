#topology = '/path/to/pdb'

nw_dcd='../dehydrate/nw_prasinezumab_2KKW_ion_prod.dcd'
topology='../../prasinezumab_2KKW_mod.pdb'

mdconvert $nw_dcd -o gmx_MMPBSA_input.xtc -t $topology
