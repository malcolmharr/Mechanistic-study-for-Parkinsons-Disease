package require pbctools

mol load psf ../../solvation/prot_ion.psf
set structName "prot_ion_prod"
for {set i 1} {$i <= 10} {incr i} {
        set dcdName "../${structName}${i}.dcd"
        mol addfile $dcdName waitfor all
        set last [expr {[molinfo top get numframes]-1}]
}

pbc wrap -center com -centersel "chain A H L" -compound res -all
pbc wrap -center com -centersel "chain H L" -compound res -all
pbc join fragment -sel "chain A" -bondlist -all

set reference [atomselect top "chain H and resid 26 to 32" frame 0]

set compare [atomselect top "chain H and resid 26 to 32"]

set num_steps [molinfo top get numframes]

set outfile [open hcdr1rmsd1.csv w]

for {set frame 0} {$frame < $num_steps} {incr frame} {
$compare frame $frame
set trans_mat [measure fit $compare $reference]
$compare move $trans_mat
set rmsd [measure rmsd $compare $reference]
puts $outfile "$rmsd"
}
close $outfile
