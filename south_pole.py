from experiment import Experiment
import numpy as np

""" Class for the IceCube Upgrade experiment. """
class IC(Experiment):
    def __init__(self, fname, variables, flavors, cp, interaction, samples):
        super(
            IC,
            self).__init__(
            fname,
            variables,
            flavors,
            cp,
            interaction,
            samples)

        """ Name of the experiment. """
        self.experiment = "IceCube Upgrade"

        """ Dictionary linking the name of variables in the simulation file and their
        callable names.
        """
        self.variable_names = {
            "pdg": ["neutrino", "nu"],
            "true_energy": ["Enu", "E"],
            "true_zenith": ["dirnu_z", "nudir_z", "cos_zen", "cos_zentih"],
            "true_azimuth": ["azi", "azimuth"],
            "interaction_type": ["interaction", "int_mode", "mode"],
            "current_type": ["current", "current_type"],
            "reco_energy": ["reco_energy"],
            "reco_azimuth": ["reco_azi", "reco_azimuth"],
            "reco_zenith": ["recodir_z", "reco_dir_z", "reco_coszen"],
            "Q2": ["Q2", "mom_transf"],
            "W": ["W", "inv_mass_had"],
            "x": ["x_bjorken", "x"],
            "y": ["y", "inelasticity"],
            "xsec": ["cross_section", "xsec"],
            "dxsec": ["diff_cross_section", "dxsec"],
            "pid": ["itype", "event_type", "ip"]}

        """ Dictionary linking the name of variables in the simulation file and their
        fancy names for plots.
        """
        self.variable_labels = {
            "pdg": r"Neutrino flavor",
            "true_energy": r"$E_{\nu}$ (GeV)",
            "true_zenith": r"$\cos \theta_{zen}^{\nu}$",
            "true_azimuth": "Azimuth",
            "interaction_type": "Interaction mode",
            "current_type": "Neutral or charged current",
            "reco_energy": "Reco. Energy (GeV)",
            "reco_azimuth": "Reco. Azimuth",
            "reco_zenith": r"$\cos \theta_{zen}^{reco}$",
            "Q2": r"Momentum transfer $Q^2$ ($GeV^2/c^2$)",
            "W": r"Hadronic invariant mass ($GeV/c^2$)",
            "x": "Bjorken x",
            "y": "Inelasticity",
            "xsec": "Cross section ($10^{-38}$ $cmm^{2}$)",
            "dxsec": "Differential cross section",
            "pid": "Event ID"}

        """ Dictionary defining which variables will be plotted with vertical axis
        log-scale.
        """
        self.variable_logscale = {
            "pdg": False,
            "true_energy": True,
            "true_zenith": False,
            "true_azimuth": False,
            "interaction_type": False,
            "current_type": False,
            "reco_energy": True,
            "reco_azimuth": False,
            "reco_zenith": False,
            "Q2": True,
            "W": True,
            "x": True,
            "y": False,
            "xsec": True,
            "dxsec": True,
            "pid": False}

        """ Auxiliary variables for computing the weights. """
        self.aux_variables = ["weight"]

        """ Apply cosine to zeniht """
        self.apply_cos2zenith()

        """ MC file assumes 5 years of exposure. """
        mc_years = 5
        self.normalization = 365.25 * 24 * 3600 * 1e4 / mc_years  # events / IC / year

        """ Names of the IC event samples. """
        self.samples = ["Cascades", "Tracks"]

        # self.weights = self.get_weights()
        self.weights = np.ones(self.fdata["true_energy"].size)

    def get_CC(self):
        """ Method for getting charged-current events. """
        return [r"CC ", self.fdata["current_type"] == 1]

    def get_NC(self):
        """ Method for getting neutral-current events. """
        return [r"NC ", self.fdata["current_type"] == 0]

    def get_numu(self):
        """ Method for getting muon neutrinos. """
        return [r"$\nu_{\mu}$ ", np.abs(self.fdata["pdg"]) == 14]

    def get_nue(self):
        """ Method for getting electron neutrinos. """
        return [r"$\nu_{e}$ ", np.abs(self.fdata["pdg"]) == 12]

    def get_nutau(self):
        """ Method for getting tau neutrinos. """
        return [r"$\nu_{\tau}$ ", np.abs(self.fdata["pdg"]) == 16]

    def get_neutrino(self):
        """ Method for getting neutrinos. """
        return ["", self.fdata["pdg"] > 0]

    def get_antineutrino(self):
        """ Method for getting antineutrinos. """
        return ["anti-", self.fdata["pdg"] < 0]

    def get_alltrue(self):
        """ Method for getting a vector of Trues. """
        return ["", self.fdata["pdg"] == self.fdata["pdg"]]

    def get_sample(self, index):
        """ Method for getting a given sample. """
        return self.fdata["pid"] == index

    def get_weights(self):
        """ Method for getting the weights based on the simulation. """
        return self.fdata["weight"]

    def apply_cos2zenith(self):
        """ Apply cosine to zenith angle from input MC file. """
        self.fdata["true_zenith"] = np.cos(self.fdata["true_zenith"])
        self.fdata["reco_zenith"] = np.cos(self.fdata["reco_zenith"])
