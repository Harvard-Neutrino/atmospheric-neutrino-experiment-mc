from south_pole import IC
import numpy as np

""" Class for the ORCA experiment. """
class ORCA(IC):
    def __init__(self, fname, variables, flavors, cp, interaction, samples):
        super(
            ORCA,
            self).__init__(
            fname,
            variables,
            flavors,
            cp,
            interaction,
            samples)

        """ Name of the experiment. """
        self.experiment = "ORCA"

        """ ORCA MC file was enlarged by 15. """
        self.normalization *= 1 / 15  # events / ORCA / year

        """ Names of the IC event samples. """
        self.samples = ["Cascades", "Tracks", "Itermediate"]
