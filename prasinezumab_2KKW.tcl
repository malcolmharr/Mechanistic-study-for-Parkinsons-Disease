mol load pdb prasinezumab_2KKW.pdb 

set H [atomselect top "chain H"]
$H set chain H
$H writepdb H.pdb

set L [atomselect top "chain L"]
$L set chain L
$L writepdb L.pdb

set A [atomselect top "chain A"]
$A set chain A
$A writepdb A.pdb

package require psfgen
topology /your/topology/files/toppar_c36_jul22/top_all36_prot.rtf

pdbalias residue HIS HSD
pdbalias atom ILE CD1 CD
pdbalias atom ILE H HN
pdbalias atom ILE HG12 HG11
pdbalias atom ILE HG13 HG12
pdbalias atom ILE HD11 HD1
pdbalias atom ILE HD12 HD2
pdbalias atom ILE HD13 HD3

pdbalias residue NAG BGLCNA
pdbalias atom NAG N2 N
pdbalias atom NAG C7 C
pdbalias atom NAG O7 O
pdbalias atom NAG C8 CT

pdbalias residue BMA BMAN
pdbalias residue AMA AMAN
pdbalias residue FUC AFUC

segment H {
first NTER
pdb H.pdb
last CTER
}
coordpdb H.pdb H

segment L {
first NTER
pdb L.pdb
last CTER
}
coordpdb L.pdb L

segment A {
first NTER
pdb A.pdb
last CTER
}
coordpdb A.pdb A

patch DISU H:22 H:96
patch DISU H:143 H:199
patch DISU H:219 L:220
patch DISU L:23 L:94
patch DISU L:140 L:200

guesscoord

regenerate angles dihedrals

writepsf -cmap prasinezumab_2KKW_mod.psf
writepdb prasinezumab_2KKW_mod.pdb

exit
