mol load psf ../../prasinezumab_2KKW_mod.psf
mol addfile ../dehydrate/nw_prasinezumab_2KKW_prod.dcd waitfor all

pbc wrap -center com -centersel "chain A H L" -compound res -all
pbc wrap -center com -centersel "chain H L" -compound res -all
pbc join fragment -sel "chain A" -bondlist -all

set reference [atomselect top "chain H and resid 52 to 57" frame 0]

set compare [atomselect top "chain H and resid 52 to 57"]

set num_steps [molinfo top get numframes]

set outfile [open hcdr2rmsd3.csv w]

for {set frame 0} {$frame < $num_steps} {incr frame} {
$compare frame $frame
set trans_mat [measure fit $compare $reference]
$compare move $trans_mat
set rmsd [measure rmsd $compare $reference]
puts $outfile "$rmsd"
}
close $outfile
