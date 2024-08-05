# Mechanistic-study-for-Parkinsons-Disease

## Description
This repository includes references and files necessary to perform protein-protein docking, molecular dynamics (MD) simulations and analysis of hydrogen bonding, free energy, and RMSD.


## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Setup

### 1.	Create and set up a conda environment with the packages indicated in requirements.txt. If you do not have conda, download Miniconda from the following link: https://docs.conda.io/en/latest/miniconda.html

	'''sh
	conda create -n <name-of-env> python=3.8
	pip install -r requirements.txt
	'''

### 2.	Download and install [VMD](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) and [NAMD](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=NAMD). NAMD versions 2.14 and 3.0b should be installed, as the former will run on CPU for minimization and heating, while the latter will run on GPU for equilibration and production. Once you have installed these, export the paths to your .bashrc for ease of use

	'''sh
	vim ~/.bashrc
	export PATH=$PATH:/your/install/directory/vmd-1.9.3/build/bin
	export PATH=$PATH:/your/install/directory/NAMD_2.14_Linux-x86_64-multicore-CUDA
	export PATH=$PATH:/your/install/directory/NAMD_3.0alpha9_Linux-x86_64-multicore-CUDA
	'''

### 3.	Download the [CHARMM 36m forcefield](http://mackerell.umaryland.edu/charmm_ff.shtml). This will be used for topology and parameter files for all MD simulations

### 4.	Download your protein of interest from the [Protein Data Bank](https://www.kegg.jp/), and obtain the sequence for the antibody you wish to model. In this study, Prasinezumab's sequence was obtained from the [Kyoto Encyclopedia of Genes and Genomes](https://www.kegg.jp/).

## Docking

Before running MD simulations, you must first use a protein-protein docking tool to obtain the structure of the complex. If you are using BioLuminate for antibody homology modeling, protein preparation, and docking, please see the [documentation from Schrödinger](https://learn.schrodinger.com/private/edu/release/current/Documentation/html/bioluminate/maestro-bioluminate-homepage.htm?tocpath=Biologics%20Drug%20Discovery%7CMaestro%20BioLuminate%7C_____0) for detailed instructions. To allow and encourage reproducibility for those without licenses to Schrödinger software, you can use the following tools to obtain the same effect. 

### 1. Antibody Homology modeling.

You can use [ABodyBuilder2](https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/sabpred/abodybuilder2/) to produce a structure of the Fv region of your target antibody.

### 2. Adding hydrogens

Use the add_h.tcl script to add hydrogens to your protein. Execute the following command to do so.

	'''sh
 	vmd -dispdev text -e add_h.tcl
 	'''

### 3. Protein Docking

Visit either [HDOCK](http://hdock.phys.hust.edu.cn/) or [ZDOCK](https://zdock.wenglab.org/) to run protein-protein docking on their web server. 

## MD Simulation

The rest of this repository contains all of the files necessary to perform molecular dynamics simulations of your docked protein structure. An example antibody-antigen complex is provided for this tutorial

### 1. Protein modification

Edit prot_mod.tcl to change the $protein variable to the path to your pdb file. Change the topology section to reference your topology files. Make sure you have identified all disulfide bonds present in your protein in the patch DISU area. Run this command using:

	'''sh
	vmd -dispdev text -e prot_mod.tcl
  	'''

### 2. Minimization

Use the following commands to run the minimization of your protein

	'''sh
	cd min
 	namd2 +p10 +setcpuaffinity +devices 0 prot_min.conf > prot_min.out &
 	'''

### 3. Solvation

Use the following command to run solvation and ionization. Edit prot_solv.tcl to change the thickness of the water box and change the concentration of your ionized system. This script will only neutralize the system, so add the flag -sc <salt concentration> in units of mol/L. For more information on how to use the autoionize package, see the [documentation on VMD](https://www.ks.uiuc.edu/Research/vmd/plugins/autoionize/).

	'''sh
 	cd ../solvation
	vmd -dispdev text -e prot_solv.tcl
 	'''
  
### 4. Production

## Analysis

### 1. Hydrogen Bonding

### 2. 

## Contact

Reach out to Malcolm Harrison at mharriso1@stevens.edu with any questions about the setup and execution
