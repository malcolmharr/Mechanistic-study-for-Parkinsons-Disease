# Mechanistic-study-for-Parkinsons-Disease

## Description
This repository includes references and files necessary to perform protein-protein docking, molecular dynamics (MD) simulations and analysis of hydrogen bonding, free energy, and RMSD.


## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Setup

1. Create and setup a conda environment with the packages indicated in requirements.txt. If you do not have conda, donwload Miniconda from the following link: https://docs.conda.io/en/latest/miniconda.html

	'''sh
	conda create -n <name-of-env> python=3.8
	pip install -r requirements.txt
	'''

2. Download and install VMD 1.9.3, NAMD 2.14, and NAMD 3.0b. Instructions to download them can be found at https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD and https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=NAMD. Once you have installed these, export the paths to your .bashrc for ease of use

	'''sh
	vim ~/.bashrc
	export PATH=$PATH:/your/install/directory/vmd-1.9.3/build/bin
	export PATH=$PATH:/your/install/directory/NAMD_2.14_Linux-x86_64-multicore-CUDA
	export PATH=$PATH:/your/install/directory/NAMD_3.0alpha9_Linux-x86_64-multicore-CUDA
	'''

3. Download youe protein of interest from rcsb.org. 

	'''sh	
	vim ~/.basrhc
	export SILCSBIODIR=/anvil/projects/x-bio220114/username/directory/silcsbio.2024.1
	export GMXDIR=/anvil/projects/x-bio220114/username/directory/gromacs/bin
	source ~/.bashrc
	'''
	
4. Set up a conda environment for silcsbio. This allows you to make sure that all of the packages work correctly and do not conflict with any other programs you use. If you do not have conda, donwload Miniconda from the following link: https://docs.conda.io/en/latest/miniconda.html

	'''sh
	conda create -n silcs python=3
	conda activate silcs
	pip install -r $SILCSBIODIR/utils/python/requirements.txt
	'''

## Usage

Using SilcsBio to study antibody excipient interactions is very useful, however a lot of the scripts that they use create SLURM jobs that do not work properly with Anvil's system. To circumnavigate these issues, the following bash files can be used to run SilcsBio jobs autonomously. Please reference /anvil/projects/x-bio220114/mharrison/nist-fab to see all of the specific files. 

1. Run SILCS and generate FragMaps

	



Run the script using:
    ```sh
    python script.py
    ```
Example:
    ```sh
    python script.py --arg1 value1 --arg2 value2
    ```

## Contact

Reach out to Malcolm Harrison at mharriso1@stevens.edu with any questions about the setup and execution
