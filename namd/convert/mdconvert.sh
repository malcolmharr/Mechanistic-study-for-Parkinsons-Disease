nw_dcd='../dehydrate/nw_prot_ion_prod.dcd'
topology='../../prot_mod.pdb'

conda activate md

mdconvert $nw_dcd -o gmx_MMPBSA_input.xtc -t $topology

python psf2top.py
