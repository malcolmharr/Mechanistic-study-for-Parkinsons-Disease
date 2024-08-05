set selText "(not water and not ion)"
set outPrefix "nw_";
set structName "prot_ion_prod"

mol load psf ../../solvation/prot_ion.psf pdb ../../solvation/prot_ion.pdb
set sel [atomselect top $selText]

$sel writepsf nw_${structName}.psf
$sel writepdb nw_${structName}.pdb

animate delete all
for {set i 1} {$i <= 10} {incr i} {
	set dcdName "../${structName}${i}.dcd"
	mol addfile $dcdName waitfor all
	set last [expr {[molinfo top get numframes]-1}]
}

animate write dcd "nw_${structName}.dcd" beg 0 end $last waitfor all sel $sel top
mol delete top
exit
