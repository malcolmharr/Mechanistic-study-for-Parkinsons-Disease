# Mechanistic-study-for-Parkinsons-Disease

## Description
This repository includes references and files necessary to perform protein-protein docking, molecular dynamics (MD) simulations and analysis of hydrogen bonding, free energy, and RMSD.


## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Setup

# 1. Create and set up a conda environment with the packages indicated in requirements.txt. If you do not have conda, download Miniconda from the following link: https://docs.conda.io/en/latest/miniconda.html

	'''sh
	conda create -n <name-of-env> python=3.8
	pip install -r requirements.txt
	'''

# 2. Download and install VMD 1.9.3, NAMD 2.14, and NAMD 3.0b. Instructions to download them can be found at https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD and https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=NAMD. Once you have installed these, export the paths to your .bashrc for ease of use

	'''sh
	vim ~/.bashrc
	export PATH=$PATH:/your/install/directory/vmd-1.9.3/build/bin
	export PATH=$PATH:/your/install/directory/NAMD_2.14_Linux-x86_64-multicore-CUDA
	export PATH=$PATH:/your/install/directory/NAMD_3.0alpha9_Linux-x86_64-multicore-CUDA
	'''

# 3. Download your protein of interest from the Protein Data Bank. (https://rcsb.org) and obtain the sequence for the antibody you wish to model. In this study, Prasinezumab's sequence was obtained from the Kyoto Encyclopedia of Genes and Genomes (https://www.kegg.jp/)

## Docking

Before running MD simulations, you must first use a protein-protein docking tool to obtain the structure of the complex. If you are using BioLuminate for antibody homology modeling, protein preparation, and docking, please see the documentation from Schrödinger for detailed instructions. To allow and encourage reproducibility for those without licenses to Schrödinger software, you can use the following tools to obtain the same effect. 

# 1. Antibody Homology modeling.



## Contact

Reach out to Malcolm Harrison at mharriso1@stevens.edu with any questions about the setup and execution
