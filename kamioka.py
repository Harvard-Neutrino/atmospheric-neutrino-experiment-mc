from experiment import Experiment
import numpy as np


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

        self.experiment = "SK"

        self.variable_names = {
            'ipnu': ['neutrino', 'nu'],
            'pnu': ['Enu', 'E'],
            'dirnuX': ['dirnu_x', 'nudir_x'],
            'dirnuY': ['dirnu_y', 'nudir_y'],
            'dirnuZ': ['dirnu_z', 'nudir_z', 'cos_zen', 'cos_zentih'],
            'azi': ['azi', 'azimuth'],
            'plep': ['Plep', 'plepton', 'lepton_mom'],
            'dirlepX': ['dirlep_x', 'lepton_dir_x'],
            'dirlepY': ['dirlep_y', 'lepton_dir_y'],
            'dirlepZ': ['dirlep_z', 'lepton_dir_z'],
            'mode': ['interaction', 'int_mode', 'mode'],
            'imass': ['inv_mass'],
            'pmax': ['mom_reco_mer'],
            'evis': ['reco_energy'],
            'recodirX': ['recodir_x', 'reco_dir_x'],
            'recodirY': ['recodir_y', 'reco_dir_y'],
            'recodirZ': ['recodir_z', 'reco_dir_z', 'reco_coszen'],
            'ip': ['ring_ip', 'reco_ring_ip', 'ip'],
            'nring': ['number_of_rings', 'nring'],
            'muedk': ['muedk', 'reco_decay_e'],
            'neutron': ['number_neutrons', 'neutrons'],
            'itype': ['itype', 'event_type']}

        self.variable_labels = {
            'ipnu': r'Neutrino flavor',
            'pnu': r'$E_{\nu}$ (GeV)',
            'dirnuX': r'$u_{x}^{\nu}$',
            'dirnuY': r'$u_{x}^{\nu}$',
            'dirnuZ': r'$\cos \theta_{zen}^{\nu}$',
            'azi': 'Azimuth',
            'plep': r'$p_{lep}$',
            'dirlepX': r'$u_{x}^{lep}$',
            'dirlepY': r'$u_{y}^{lep}$',
            'dirlepZ': r'$u_{z}^{lep}$',
            'mode': 'Interaction mode (NEUT)',
            'imass': r'$\pi^{0}$ invariant mass',
            'pmax': 'Reco. momentum of most energetic ring (GeV/c)',
            'evis': 'Reco. Energy (GeV)',
            'recodirX': r'$u_{x}^{reco}$',
            'recodirY': r'$u_{x}^{reco}$',
            'recodirZ': r'$\cos \theta_{zen}^{reco}$',
            'ip': 'Ring ID',
            'nring': 'Number of rings',
            'muedk': 'Number of tagged decay electrons',
            'neutron': 'Number of tagged neutrons',
            'itype': 'Event ID'}

        self.variable_logscale = {
            'ipnu': False,
            'pnu': True,
            'dirnuX': False,
            'dirnuY': False,
            'dirnuZ': False,
            'azi': False,
            'plep': True,
            'dirlepX': False,
            'dirlepY': False,
            'dirlepZ': False,
            'mode': False,
            'imass': True,
            'pmax': True,
            'evis': True,
            'recodirX': False,
            'recodirY': False,
            'recodirZ': False,
            'ip': False,
            'nring': False,
            'muedk': False,
            'neutron': False,
            'itype': False}

        ''' Auxiliary variables'''
        self.aux_variables = [
            'weightSim',
            'weightOsc_SKpaper',
            'weightOsc_SKbest',
            'weightReco']

        ''' SuperK samples '''
        self.samples = [
            'SingleRingSubGeV Elike 0dcy-e',
            'SingleRing SubGeV Elike 1dcy-e',
            'SingleRing Pi0like',
            'SingleRing SubGeV Mulike 0dcy-e',
            'SingleRing SubGeV Mulike 1dcy-e',
            'SingleRing SubGeV Mulike 2dcy-e',
            'Double Ring Pi0like',
            'SingleRing MultiGeV Elike Nulike',
            'SingleRing MultiGeV Elike NuBarlike',
            'SingleRing MultiGeV Mulike',
            'MultiRing MultiGeV Elike Nulike',
            'MultiRing MultiGeV Elike NuBarlike',
            'MultiRing Mulike',
            'MultiRing MultiGeV Elike Other']
        self.print_samples()

    def get_CC(self):
        return [r"CC ", np.abs(self.fdata["mode"])<30]

    def get_NC(self):
        return [r"NC ", np.abs(self.fdata["mode"])>30]

    def get_numu(self):
        return [r"$\nu_{\mu}$ ", np.abs(self.fdata["ipnu"])==14]

    def get_nue(self):
        return [r"$\nu_{e}$ ", np.abs(self.fdata["ipnu"])==12]

    def get_nutau(self):
        return [r"$\nu_{\tau}$ ", np.abs(self.fdata["ipnu"])==16]

    def get_neutrino(self):
        return ["", self.fdata["ipnu"] > 0]

    def get_antineutrino(self):
        return ["anti-", self.fdata["ipnu"] <0 ]

    def get_alltrue(self):
        return ["", self.fdata["ipnu"]==self.fdata["ipnu"]]

    def get_sample(self, index):
        return self.fdata["itype"]==index
