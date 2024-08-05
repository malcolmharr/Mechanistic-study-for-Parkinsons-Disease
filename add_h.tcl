package require psfgen

topology /path/to/topology/

pdbalias residue HIS HSE
pdbalias atom ILE CD1 CD

coordpdb prot.pdb
guesscoord

writepdb prot_h.pdb
writepsf prot_h.psf
