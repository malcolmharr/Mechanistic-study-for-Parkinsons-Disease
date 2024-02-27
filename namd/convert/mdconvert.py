import mdtraj 

#nw_dcd = '../dehydrate/insert_dcd_name'
#topology = '/path/to/pdb'

nw_dcd = '../dehydrate/nw_prasinezumab_2KKW_ion_prod.dcd'
topology = '../../prasinezumab_2KKW_mod.pdb'

/home/malcolm/anaconda3/envs/md/bin/mdconvert ../dehydrate/nw_prasinezumab_2KKW_ion_prod.dcd -o gmx_MMPBSA_input.xtc -t ../../prasinezumab_2KKW_mod.pdb
