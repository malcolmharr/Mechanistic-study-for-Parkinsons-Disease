set selText "(not water and not ion)"
set outPrefix "nw_";

mol load psf ../../solvation/prasinezumab_2KKW_ion.psf pdb ../../solvation/prasinezumab_2KKW_ion.pdb
set sel [atomselect top $selText]
#set dcdName [trimPath $dcd]
set structName "prasinezumab_2KKW_prod"

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
