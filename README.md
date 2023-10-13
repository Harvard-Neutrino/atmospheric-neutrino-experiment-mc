# Monte Carlo Simulations
We provide the MC simlation files of atmospheric neutrinos for the following experiments in [HDF5](https://www.hdfgroup.org/solutions/hdf5/) format. All of them can be downloaded from the [Harvard Dataverse]()
 - SuperK: No neutron tagging covering the first 3 phases of the experiment.
 - SuperK with neutron tagging on Hydrogen: For phases 4 and 5 of SuperK and also used as HyperK's simulation file.
 - SuperK with neutron tagging on Gd: Assumes the SuperK detector is loaded with Gd at the goal concentration of 0.1%.
 - IceCube-Upgrade: Copied from publibly available simulation from the [IceCube Collaboration](https://icecube.wisc.edu/data-releases/2020/04/icecube-upgrade-neutrino-monte-carlo-simulation/) converted into .hdf5 format for completeness.
 - ORCA: Projected simulation based on IceCube-Upgrade's upgrade Monte Carlo applying reported detector response.

## SuperK and HyperK files

<img src="/figures/SK_Ntag_variables.png" width="600" />


## IceCube-Upgrade files

<img src="/figures/IC_variables.png" width="400" />


## ORCA file

<img src="/figures/ORCA_variables.png" width="400" />


# Simple plotting code
To use it, make sure you meet all the requirements by doing:
> pip install -r requirements.txt


# Other
Further questions and details can be addressed to the [paper](https://journals.aps.org/prx/accepted/49070K6bLa71ff0936b49c35c8a36649585379947) authors.
