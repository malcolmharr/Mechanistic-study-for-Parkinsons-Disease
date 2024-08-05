#!/usr/bin/env bash

vmd -dispdev text -e hcdr1rmsd1.tcl &

vmd -dispdev text -e hcdr2rmsd1.tcl &

vmd -dispdev text -e hcdr3rmsd1.tcl &

vmd -dispdev text -e lcdr1rmsd1.tcl &

vmd -dispdev text -e lcdr2rmsd1.tcl &

vmd -dispdev text -e lcdr3rmsd1.tcl &
