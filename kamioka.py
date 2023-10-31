from experiment import Experiment
import numpy as np

""" Class for the Super-Kamiokande experiment with no neutron tagging. """


class SK(Experiment):
    def __init__(self, fname, variables, flavors, cp, interaction, samples):
        super(
            SK,
            self).__init__(
            fname,
            variables,
            flavors,
            cp,
            interaction,
            samples)

        """ Name of the experiment. """
        self.experiment = "SK"

        """ Dictionary linking the name of variables in the simulation file and their
        callable names.
        """
        self.variable_names = {
            "ipnu": ["neutrino", "nu"],
            "pnu": ["Enu", "E"],
            "dirnuX": ["dirnu_x", "nudir_x"],
            "dirnuY": ["dirnu_y", "nudir_y"],
            "dirnuZ": ["dirnu_z", "nudir_z", "cos_zen", "cos_zentih"],
            "azi": ["azi", "azimuth"],
            "plep": ["Plep", "plepton", "lepton_mom"],
            "dirlepX": ["dirlep_x", "lepton_dir_x"],
            "dirlepY": ["dirlep_y", "lepton_dir_y"],
            "dirlepZ": ["dirlep_z", "lepton_dir_z"],
            "mode": ["interaction", "int_mode", "mode"],
            "imass": ["inv_mass"],
            "pmax": ["mom_reco_mer"],
            "evis": ["reco_energy"],
            "recodirX": ["recodir_x", "reco_dir_x"],
            "recodirY": ["recodir_y", "reco_dir_y"],
            "recodirZ": ["recodir_z", "reco_dir_z", "reco_coszen"],
            "ip": ["ring_ip", "reco_ring_ip", "ip"],
            "nring": ["number_of_rings", "nring"],
            "muedk": ["muedk", "reco_decay_e"],
            "itype": ["itype", "event_type"]}

        """ Dictionary linking the name of variables in the simulation file and their
        fancy names for plots.
        """
        self.variable_labels = {
            "ipnu": r"Neutrino flavor",
            "pnu": r"$E_{\nu}$ (GeV)",
            "dirnuX": r"$u_{x}^{\nu}$",
            "dirnuY": r"$u_{x}^{\nu}$",
            "dirnuZ": r"$\cos \theta_{zen}^{\nu}$",
            "azi": "Azimuth",
            "plep": r"$p_{lep}$",
            "dirlepX": r"$u_{x}^{lep}$",
            "dirlepY": r"$u_{y}^{lep}$",
            "dirlepZ": r"$u_{z}^{lep}$",
            "mode": "Interaction mode (NEUT)",
            "imass": r"$\pi^{0}$ invariant mass",
            "pmax": "Reco. momentum of most energetic ring (GeV/c)",
            "evis": "Reco. Energy (GeV)",
            "recodirX": r"$u_{x}^{reco}$",
            "recodirY": r"$u_{x}^{reco}$",
            "recodirZ": r"$\cos \theta_{zen}^{reco}$",
            "ip": "Ring ID",
            "nring": "Number of rings",
            "muedk": "Number of tagged decay electrons",
            "itype": "Event ID"}

        """ Dictionary defining which variables will be plotted with vertical axis
        log-scale.
        """
        self.variable_logscale = {
            "ipnu": False,
            "pnu": True,
            "dirnuX": False,
            "dirnuY": False,
            "dirnuZ": False,
            "azi": False,
            "plep": True,
            "dirlepX": False,
            "dirlepY": False,
            "dirlepZ": False,
            "mode": False,
            "imass": True,
            "pmax": True,
            "evis": True,
            "recodirX": False,
            "recodirY": False,
            "recodirZ": False,
            "ip": False,
            "nring": False,
            "muedk": False,
            "itype": False}

        """ Auxiliary variables for computing the weights. """
        self.aux_variables = [
            "weightSim",
            "weightReco",
            "weightOsc_SKpaper",
            "weightOsc_SKbest"]

        """ Compute the weights. """
        self.weights = self.get_weights()
        # self.flux_weights = self.get_flux_weights()
        # self.osc_weights = self.get_osc_weights()

        """ Compute number of events in the MC file
        sk_rate_yr = # events / days * days_per_year
        Extracted from https://doi.org/10.1103/PhysRevD.97.072001
        """
        sk_rate_yr = 36437.9607 / 5326 * 365.25
        number_of_events = np.sum(self.weights)
        mc_years = number_of_events / sk_rate_yr
        self.normalization = 1 / mc_years  # events / SK / year

        """ Names of the SuperK event samples. """
        self.samples = [
            "SingleRingSubGeV Elike 0dcy-e",
            "SingleRing SubGeV Elike 1dcy-e",
            "SingleRing Pi0like",
            "SingleRing SubGeV Mulike 0dcy-e",
            "SingleRing SubGeV Mulike 1dcy-e",
            "SingleRing SubGeV Mulike 2dcy-e",
            "Double Ring Pi0like",
            "SingleRing MultiGeV Elike Nulike",
            "SingleRing MultiGeV Elike NuBarlike",
            "SingleRing MultiGeV Mulike",
            "MultiRing MultiGeV Elike Nulike",
            "MultiRing MultiGeV Elike NuBarlike",
            "MultiRing Mulike",
            "MultiRing MultiGeV Elike Other"]

    def get_CC(self):
        """ Method for getting charged-current events. """
        return [r"CC ", np.abs(self.fdata["mode"]) < 30]

    def get_NC(self):
        """ Method for getting neutral-current events. """
        return [r"NC ", np.abs(self.fdata["mode"]) > 30]

    def get_numu(self):
        """ Method for getting muon neutrinos. """
        return [r"$\nu_{\mu}$ ", np.abs(self.fdata["ipnu"]) == 14]

    def get_nue(self):
        """ Method for getting electron neutrinos. """
        return [r"$\nu_{e}$ ", np.abs(self.fdata["ipnu"]) == 12]

    def get_nutau(self):
        """ Method for getting tau neutrinos. """
        return [r"$\nu_{\tau}$ ", np.abs(self.fdata["ipnu"]) == 16]

    def get_neutrino(self):
        """ Method for getting neutrinos. """
        return ["", self.fdata["ipnu"] > 0]

    def get_antineutrino(self):
        """ Method for getting antineutrinos. """
        return ["anti-", self.fdata["ipnu"] < 0]

    def get_alltrue(self):
        """ Method for getting a vector of Trues. """
        return ["", self.fdata["ipnu"] == self.fdata["ipnu"]]

    def get_sample(self, index):
        """ Method for getting a given sample. """
        return self.fdata["itype"] == index

    def get_weights(self):
        """ Method for getting the weights based on the simulation. """
        return self.fdata["weightReco"]

    def get_flux_weights(self):
        """ Method for getting the inverse of the HKKM atmospheric neutrino
        flux used in the simulation.
        """
        return self.fdata["weightSim"]

    def get_osc_weights(self):
        """ Method for getting the pre-computed oscillation weights.
          a) Oscillation parameters as in table II
          of https://doi.org/10.1103/PhysRevD.97.072001
          b) Oscillation parameters as the best fit result
          in https://doi.org/10.1103/PhysRevD.97.072001
        """
        # a)
        return self.fdata["weightOsc_SKpaper"]
        # b)
        # return self.fdata["weightOsc_SKbest"]


""" Class for the Super-Kamiokande experiment with H-neutron tagging. """


class SK_Htag(SK):
    def __init__(self, fname, variables, flavors, cp, interaction, samples):
        super(
            SK_Htag,
            self).__init__(
            fname,
            variables,
            flavors,
            cp,
            interaction,
            samples)

        """ Name of the experiment. """
        self.experiment = "SK w/ H-neutron tagging"

        """ Dictionary linking the name of variables in the simulation file and their
        callable names.
        """
        self.variable_names["neutron"] = ["number_neutrons", "neutrons"]

        """ Dictionary linking the name of variables in the simulation file and their
        fancy names for plots.
        """
        self.variable_labels["neutron"] = "# of tagged neutrons on hydrogen"

        """ Dictionary defining which variables will be plotted with vertical axis
        log-scale.
        """
        self.variable_logscale["neutron"] = False

        """ Names of the SuperK event samples. """
        self.samples = [
            'SingleRing SubGeV NuElike',
            'SingleRing SubGeV Elike',
            'SingleRing SubGeV NuEBarlike',
            'SingleRing Pi0like',
            'SingleRing SubGeV NuMulike',
            'SingleRing SubGeV NuMuBarlike',
            'Double Ring Pi0like',
            'MultiGeV NuElike',
            'SingleRing MultiGeV Elike',
            'SingleRing MultiGeV NuEBarlike',
            'SingleRing MultiGeV NuMulike',
            'SingleRing MultiGeV NuMuBarlike',
            'MultiRing MultiGeV Elike Nulike',
            'MultiRing MultiGeV Elike NuBarlike',
            'MultiRing Mulike',
            'MultiRing MultiGeV Elike Other']


""" Class for the Super-Kamiokande experiment with Gd-neutron tagging. """


class SK_Gdtag(SK_Htag):
    def __init__(self, fname, variables, flavors, cp, interaction, samples):
        super(
            SK_Gdtag,
            self).__init__(
            fname,
            variables,
            flavors,
            cp,
            interaction,
            samples)

        """ Name of the experiment. """
        self.experiment = "SuperK-Gd"

        """ Dictionary linking the name of variables in the simulation file and their
        fancy names for plots.
        """
        self.variable_labels["neutron"] = "# of tagged neutrons on gadolinium"


""" Class for the Hyper-Kamiokande experiment assuming H-neutron tagging. """


class HK(SK_Htag):
    def __init__(self, fname, variables, flavors, cp, interaction, samples):
        super(
            HK,
            self).__init__(
            fname,
            variables,
            flavors,
            cp,
            interaction,
            samples)

        """ Name of the experiment. """
        self.experiment = "HyperK"

        """ Assuming HK will have 8.3 times larger volume than SK. """
        self.normalization = 1 / mc_years  # events / SK / year
