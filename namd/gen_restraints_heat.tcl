mol load psf ../solvation/prasinezumab_2KKW_ion.psf namdbin prasinezumab_2KKW_ion_min.coor

[atomselect top "chain H I L M G J and noh"] set beta 1.0

[atomselect top all] writepdb constraint_heat.pdb

exit
