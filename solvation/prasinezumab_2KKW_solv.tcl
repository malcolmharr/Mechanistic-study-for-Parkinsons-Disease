mol load psf ../prasinezumab_2KKW_mod.psf namdbin ../minimization/prasinezumab_2KKW_min.coor
[atomselect top "all"] writepdb prasinezumab_2KKW_min.pdb

package require solvate
solvate ../prasinezumab_2KKW_mod.psf prasinezumab_2KKW_min.pdb -t 10 -o prasinezumab_2KKW_solv

package require autoionize
autoionize -psf prasinezumab_2KKW_solv.psf -pdb prasinezumab_2KKW_solv.pdb -neutralize -o prasinezumab_2KKW_ion

exit
