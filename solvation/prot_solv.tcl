mol load psf ../prot_mod.psf namdbin ../min/prot_min.coor
[atomselect top "all"] writepdb prot_min.pdb

package require solvate
solvate ../prot_mod.psf prot_min.pdb -t 10 -o prot_solv

package require autoionize
autoionize -psf prot_solv.psf -pdb prot_solv.pdb -neutralize -o prot_ion

exit
