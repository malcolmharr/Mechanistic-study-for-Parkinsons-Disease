package require pbctools

mol load psf ../../solvation/prasinezumab_2KKW_ion.psf
set structName "prasinezumab_2KKW_ion_prod"
for {set i 1} {$i <= 10} {incr i} {
        set dcdName "../${structName}${i}.dcd"
        mol addfile $dcdName waitfor all
        set last [expr {[molinfo top get numframes]-1}]
}

pbc wrap -center com -centersel "chain A H L" -compound res -all
pbc wrap -center com -centersel "chain H L" -compound res -all
pbc join fragment -sel "chain A" -bondlist -all

set reference [atomselect top "chain L and resid 56 to 62" frame 0]

set compare [atomselect top "chain L and resid 56 to 62"]

set num_steps [molinfo top get numframes]

set outfile [open lcdr2rmsd1.csv w]

for {set frame 0} {$frame < $num_steps} {incr frame} {
$compare frame $frame
set trans_mat [measure fit $compare $reference]
$compare move $trans_mat
set rmsd [measure rmsd $compare $reference]
puts $outfile "$rmsd"
}
close $outfile
