# import ParmEd module
import parmed as pmd

# load psf file
psf = pmd.load_file('../../prasinezumab_2KKW_mod.psf')

#load coordinate file
#psf.coordinates = pmd.load_file('step3_input.crd').coordinates

# strip ions and water
psf.strip(':POT, CLA, TIP3, LIT, SOD, RUB, CES, BAR')

# load Charmm Parameter Set. Make sure to include all the necessary force field files in this list
params = pmd.charmm.CharmmParameterSet('/anvil/projects/x-chm210013/mharrison/toppar_c36_jul22/par_all36m_prot.prm',
                                        '/anvil/projects/x-chm210013/mharrison/toppar_c36_jul22/par_all36_lipid.prm',
                                        '/anvil/projects/x-chm210013/mharrison/toppar_c36_jul22/par_all36_na.prm', 
                                        '/anvil/projects/x-chm210013/mharrison/toppar_c36_jul22/par_all36_carb.prm',
                                        '/anvil/projects/x-chm210013/mharrison/toppar_c36_jul22/par_all36_cgenff.prm',
                                        '/anvil/projects/x-chm210013/mharrison/toppar_c36_jul22/toppar_water_ions_namd.str',
                                        '/anvil/projects/x-chm210013/mharrison/toppar_c36_jul22/stream/carb/toppar_all36_carb_glycopeptide.str')
psf.load_parameters(params)

# save GROMACS topology file
psf.save('gromacs.top')
