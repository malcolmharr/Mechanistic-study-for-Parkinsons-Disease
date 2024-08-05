# import ParmEd module
import parmed as pmd

# load psf file
psf = pmd.load_file('../../prot_mod.psf')

# strip ions and water
psf.strip(':POT, CLA, TIP3, LIT, SOD, RUB, CES, BAR')

# load Charmm Parameter Set. Make sure to include all the necessary force field files in this list
params = pmd.charmm.CharmmParameterSet('/your/topology/directory/toppar_c36_jul22/par_all36m_prot.prm',
                                        '/your/topology/directory/toppar_c36_jul22/par_all36_lipid.prm',
                                        '/your/topology/directory/toppar_c36_jul22/par_all36_na.prm', 
                                        '/your/topology/directory/toppar_c36_jul22/par_all36_carb.prm',
                                        '/your/topology/directory/toppar_c36_jul22/par_all36_cgenff.prm',
                                        '/your/topology/directory/toppar_c36_jul22/toppar_water_ions_namd.str',
                                        '/your/topology/directory/toppar_c36_jul22/stream/carb/toppar_all36_carb_glycopeptide.str')
psf.load_parameters(params)

# save GROMACS topology file
psf.save('gromacs.top')
