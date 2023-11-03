# Monte Carlo Simulations
We provide the MC simlation files of atmospheric neutrinos for the following experiments in [HDF5](https://www.hdfgroup.org/solutions/hdf5 /) format. All of them can be downloaded from the [Harvard Dataverse]()
- SuperK: No neutron tagging covering the first 3 phases of the experiment.
- SuperK with neutron tagging on Hydrogen: For phases 4 and 5 of SuperK and also used as HyperK's simulation file.
- SuperK with neutron tagging on Gd: Assumes the SuperK detector is loaded with Gd at the goal concentration of 0.1 % .
- IceCube - Upgrade: Copied from publibly available simulation from the[IceCube Collaboration](https://icecube.wisc.edu/data-releases/2020/04/icecube-upgrade-neutrino-monte-carlo-simulation/) converted into .hdf5 format for completeness.
- ORCA: Projected simulation based on IceCube - Upgrade's upgrade Monte Carlo applying reported detector response.

# Plotting some variables
We provide a simple python code to plot variables from these Monte Carlo files with different option to get you started.
The code uses pretty standard requirements which can be intalled via `pip3`:
- h5py
- matplotlib
- numpy
``` 
pip3 install -r requirements.txt
```

Follow the instruction below to produce your first plots:
**usage:**
```
plot_sim.py [-h] --experiment [{SK,SK-Htag,SK-Gd,ORCA,ICUp,HK}] --fname [FNAME]
				[--variables VARIABLES [VARIABLES ...]] [--flavor [{e,mu,e+mu,tau}]] [--CP [{nu,antinu,both}]]
               [--interaction [{CC,NC,ALL,False}]] [--samples [SAMPLES]]
```
**required arguments:**
```
  --experiment [{SK,SK-Htag,SK-Gd,ORCA,ICUp,HK}] Experiment you would like to use.
  --fname [FNAME] Path to simulation file of the experiment you would like to use (SK, SK-Htag, SK-Gd, ORCA, ICUp or HK).
```
**options:**
```
  -h, --help show this help message and exit
  --variables VARIABLES [VARIABLES ...] Set of variables you want to plot. Deault variables are the true neutrino energy, the reconstructed cosine of zenith angle and the reconstructed neutrino energy.
  --flavor [{e,mu,e+mu,tau}] Flavor cut and breakdown. Default is break down of $\nu_{e}$ and $\nu_{\mu}$.
  --CP [{nu,antinu,both}] Flavor cut and breakdown. Default is break down of both.
  --interaction [{CC,NC,ALL,False}] Interaction mode(s) cut and breakdown. Dafult is no breakdown or cut.
  --samples [SAMPLES] Comma separated set of event samples you want to plot (for IC: tracks or cascades; for ORCA: tracks, intermediate or cascades; for SK and HK numerical indeces (displayed when calling these detectors)). Default is plotting all samples.
```

# SuperK and HyperK files

| Variable name(s)                            | Description                                   | Name in file |
| ------------------------------------------- | --------------------------------------------- | ------------ |
| `neutrino`,`nu`                             | Neutrino flavor                               | ipnu         |
| `Enu`,`E`                                   | Neutrino energy (GeV)                         | pnu          |
| `dirnu_x`,`nudir_x`                         | Direction of neutrino, x                      | dirnuX       |
| `dirnu_y`,`nudir_y`                         | Direction of neutrino, y                      | dirnuY       |
| `dirnu_z`,`nudir_z`,`cos_zen`,`cos_zentih`  | Neutrino cosine zenith                        | dirnuZ       |
| `azi`,`azimuth`                             | Neutrino azimuth angle                        | azi          |
| `Plep`,`plepton`,`lepton_mom`               | True lepton momentum (GeV/c)                  | plep         |
| `dirlep_x`,`lepton_dir_x`                   | True lepton direction, x                      | dirlepX      |
| `dirlep_y`,`lepton_dir_y`                   | True lepton direction, y                      | dirlepY      |
| `dirlep_z`,`lepton_dir_z`                   | True lepton direction, z                      | dirlepZ      |
| `interaction`,`int_mode`,`mode`             | Interaction mode                              | mode         |
| `inv_mass`                                  | Invariant mass of pi0                         | imass        |
| `mom_reco_mer`                              | Reco. momentum of most energetic ring (GeV/c) | pmax         |
| `reco_energy`                               | Reconstructed energy (GeV)                    | evis         |
| `recodir_x`,`reco_dir_x`                    | Reconstructed direction, x                    | recodirX     |
| `recodir_y`,`reco_dir_y`                    | Reconstructed direction, y                    | recodirY     |
| `recodir_z`,`reco_dir_z`,`reco_coszen`      | Reconstructed direction, z (zenith)           | recodirZ     |
| `ring_ip`,`reco_ring_ip`,`ip`               | Reco. ring ID                                 | ip           |
| `number_of_rings`,`nring`                   | Number of reconstructed rings                 | nring        |
| `muedk`,`reco_decay_e`                      | Number of tagged decay electrons              | muedk        |
| `number_neutrons`,`neutrons`                | Number of tagged * neutrons                   | neutron      |
| `itype`,`event_type`                        | Event ID (sample index)                       | itype        |
| ------------------------------------------- | --------------------------------------------- | ------------ |

* *The number of tagged neutrons is only available in SK-Htag, SK-Gd and HK.*

> [!INFO]
> There are more variables in these files that may be useful for the user, please look at their usage in [kamioka.py](https://github.com/Harvard-Neutrino/atmospheric-neutrino-experiment-mc/blob/main/kamioka.py).


# IceCube-Upgrade files

| Variable name(s)                            | Description                                          | Name in file     |
| ------------------------------------------- | ---------------------------------------------------- | ---------------- |
| `neutrino`,`nu`                             | Neutrino flavor                                      | pdg              |
| `Enu`,`E`                                   | Neutrino energy (GeV)                                | true_energy      |
| `dirnu_z`,`nudir_z`,`cos_zen`,`cos_zentih`  | Neutrino cosine zenith (cos_zenith derived from)     | true_zenith      |
| `azi`,`azimuth`                             | Neutrino azimuth angle                               | true_azimuth     |
| `interaction`,`int_mode`,`mode`             | Interaction mode: QE (0), RES (1), DIS (2), other (3)| interaction_type |
| `current`,`current_type`                    | Neutral (0) or charged (1) current interaction       | interaction_type |
| `reco_energy`                               | Reconstructed energy (GeV)                           | reco_energy      |
| `reco_azi`,`reco_azimuth`                   | Reconstructed azimuth                                | reco_azimuth     |
| `recodir_z`,`reco_dir_z`,`reco_coszen`      | Reconstructed direction, z (cos_zenith derived from) | reco_zenith      |
| `itype`,`event_type`,`ip`                   | Event ID (sample index)                              | pid              |
| `Q2`,`mom_transf`                           | Momentum transfer Q^2 (GeV^2/c^2)                    | Q2               |
| `W`,`inv_mass_had`                          | Hadronic invariant mass (GeV/c^2)                    | W                |
| `x_bjorken`,`x`                             | Bjorken x variable                                   | x                |
| `y`,`inelasticity`                          | Inelasticity of interaction                          | y                |
| `cross_section`,`xsec`                      | Cross section                                        | xsec             |
| `diff_cross_section`,`dxsec`                | Differential cross section                           | dxsec            |
| ------------------------------------------- | ---------------------------------------------------- | ---------------- |

> [!INFO]
> There are more variables in these files that may be useful for the user, please look at their usage in [kamioka.py](https://github.com/Harvard-Neutrino/atmospheric-neutrino-experiment-mc/blob/main/south_pole.py).


# ORCA file

The simulation file for ORCA follows the same notation and contains the same variables as the IceCube Upgrade one.

[]



# Simple plotting code
To use it, make sure you meet all the requirements by doing:
> pip install - r requirements.txt


# Other
For further questions and details, please check [paper](https://journals.aps.org/prx/accepted/49070K6bLa71ff0936b49c35c8a36649585379947) or reach out to the authors.