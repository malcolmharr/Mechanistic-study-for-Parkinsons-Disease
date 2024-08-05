# Mechanistic-study-for-Parkinsons-Disease

## Description
This repository includes references and files necessary to perform protein-protein docking, molecular dynamics (MD) simulations and analysis of hydrogen bonding, free energy, and RMSD.


## Table of Contents
- [Setup](#setup)
- [Docking](#docking)
- [MD Simulation](#md-simulation)
- [Analysis](#analysis)
- [Contact](#contact)

## Setup

### 1.	Create and set up a conda environment with the packages indicated in requirements.txt. If you do not have conda, download Miniconda from the following link: https://docs.conda.io/en/latest/miniconda.html

	conda create -n <name-of-env> python=3.8
	pip install -r requirements.txt

### 2.	Download and install [VMD](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) and [NAMD](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=NAMD). NAMD versions 2.14 and 3.0b should be installed, as the former will run on CPU for minimization and heating, while the latter will run on GPU for equilibration and production. Once you have installed these, export the paths to your .bashrc for ease of use

	vim ~/.bashrc
	export PATH=$PATH:/your/install/directory/vmd-1.9.3/build/bin
	export PATH=$PATH:/your/install/directory/NAMD_2.14_Linux-x86_64-multicore-CUDA
	export PATH=$PATH:/your/install/directory/NAMD_3.0alpha9_Linux-x86_64-multicore-CUDA

### 3.	Download the [CHARMM 36m forcefield](http://mackerell.umaryland.edu/charmm_ff.shtml). This will be used for topology and parameter files for all MD simulations

### 4.	Download your protein of interest from the [Protein Data Bank](https://www.kegg.jp/), and obtain the sequence for the antibody you wish to model. In this study, Prasinezumab's sequence was obtained from the [Kyoto Encyclopedia of Genes and Genomes](https://www.kegg.jp/).

## Docking

Before running MD simulations, you must first use a protein-protein docking tool to obtain the structure of the complex. If you are using BioLuminate for antibody homology modeling, protein preparation, and docking, please see the [documentation from Schrödinger](https://learn.schrodinger.com/private/edu/release/current/Documentation/html/bioluminate/maestro-bioluminate-homepage.htm?tocpath=Biologics%20Drug%20Discovery%7CMaestro%20BioLuminate%7C_____0) for detailed instructions. To allow and encourage reproducibility for those without licenses to Schrödinger software, you can use the following tools to obtain the same effect. 

### 1. Antibody Homology modeling.

You can use [ABodyBuilder2](https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/sabpred/abodybuilder2/) to produce a structure of the Fv region of your target antibody.

### 2. Adding hydrogens

Use the add_h.tcl script to add hydrogens to your protein. Execute the following command to do so.

 	vmd -dispdev text -e add_h.tcl

### 3. Protein Docking

Visit either [HDOCK](http://hdock.phys.hust.edu.cn/) or [ZDOCK](https://zdock.wenglab.org/) to run protein-protein docking on their web server. 

## MD Simulation

The rest of this repository contains all of the files necessary to perform molecular dynamics simulations of your docked protein structure. An example antibody-antigen complex is provided for this tutorial

### 1. Protein modification

Edit prot_mod.tcl to change the $protein variable to the path to your pdb file. Change the topology section to reference your topology files. Make sure you have identified all disulfide bonds present in your protein in the patch DISU area. Run this command using:

	vmd -dispdev text -e prot_mod.tcl

### 2. Minimization

Use the following commands to run the minimization of your protein

	cd min
 	namd2 +p10 +setcpuaffinity +devices 0 prot_min.conf > prot_min.out &

### 3. Solvation

Use the following command to run solvation and ionization. Edit prot_solv.tcl to change the thickness of the water box and change the concentration of your ionized system. This script will only neutralize the system, so add the flag -sc <salt concentration> in units of mol/L. For more information on how to use the autoionize package, see the [documentation on VMD](https://www.ks.uiuc.edu/Research/vmd/plugins/autoionize/).

	'''sh
 	cd ../solvation
	vmd -dispdev text -e prot_solv.tcl
 	'''

### 4. Production

Use the following commands to set up and run production MD simulations of your antibody-antigen complex. Edit each configuration file to make sure your topology and parameter directory is correctly identified, and edit any parameters of the MD simulation run as needed. 

 	cd ../namd
  	namd2 +p10 +setcpuaffinity +devices 0 prot_ion_min.conf > prot_ion_min.out

   	vmd -dispdev text -e gen_restraints_heat.tcl

    	namd2 +p10 +setcpuaffinity +devices 0 prot_ion_heat.conf > prot_ion_min.out

     	srun --smpi=pmi2 -n 1 namd3 +p1 +setcpuaffinity +devices 0 prot_ion_eq.conf > prot_ion_eq.out

	srun --smpi=pmi2 -n 1 namd3 +p1 +setcpuaffinity +devices 0 prot_ion_prod.conf > prot_ion_prod.out

The prot_ion_prod.conf file is set to run a 100ns simulation. If you want to run longer simulations, feel free to either edit the "run 50000000" line at the end of the file, or create a new configuration file with the following lines:

	set inputname prot_ion_prod
 	set outputname prot_ion_prod2

This is a convenient way to run longer simulations if you are on a HPC that has maximum run time hours set.

## Analysis

### 1. Remove water from trajectories

Removing waters from trajectories allows the rest of the analysis to be performed much faster. 

	cd dehydrate
 	vmd -dispdev text -e nw.tcl
### 2. Hydrogen bonding analysis

This method uses MDAnalysis to obtain hydrogen bond information from the MD trajectories, and creates a CSV file with all hydrogen bond information, as well as a text file with all hydrogen bonds sorted by prevalency. 

	cd ../hbond
 	./run-hbond.sh &
### 3. RMSD

Inside the rmsd folder, there are Tcl scripts for each CDR region of the antibody. Edit these files for whichever regions of the Fab/Fv region you wish to study. Edit plot-rmsd.py to change the name of your figure and to edit any subplots created. 

	cd ../rmsd
 	./run-rmsd.sh
  	python plot-rmsd.py
### 4. Binding affinity calculation with gmx_MMPBSA

First, visit the [gmx_MMPBSA documentation](https://valdes-tresanco-ms.github.io/gmx_MMPBSA/dev/) to install all required packages for this analysis.

If you're using MPI, run the following command:
	
	mpirun -np [num_processors] gmx_MMPBSA -O -i mmpbsa.in -cs ../../prot_mod.pdb -ct ../convert/gmx_MMPBSA_input.xtc -ci index.ndx -cg 10 11 -cp ../convert/gromacs.top -o FINAL_RESULTS_MMPBSA.dat -eo FINAL_RESULTS_MMPBSA.csv -nogui
To run the analysis in serial instead, run this following command:

	gmx_MMPBSA -O -i mmpbsa.in -cs ../../prot_mod.pdb -ct ../convert/gmx_MMPBSA_input.xtc -ci index.ndx -cg 10 11 -cp ../convert/gromacs.top -o FINAL_RESULTS_MMPBSA.dat -eo FINAL_RESULTS_MMPBSA.csv -nogui

## Contact

Reach out to Malcolm Harrison at mharriso1@stevens.edu with any questions about the setup and execution
