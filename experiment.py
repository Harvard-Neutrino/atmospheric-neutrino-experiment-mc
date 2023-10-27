import h5py
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
from itertools import product, repeat


class Experiment:
    def __init__(self, fname, variables, flavors, cp, interaction, samples):
        r"""Method for modifying the atmospheric flux normalization.
        Args:
            fname (str): Name of simulation file.
            variables ([str]): List of variables to be plotted.
            flavors (str or [str]): Flavors to be plotted.
            cp (str): Neutrinos, antineutrinos or both.
            interaction (str): Interaction modes to be plotted.
            samples ([str]): List of samples to be plotted
        """

        self.fdata = {}
        with h5py.File(fname, 'r') as hf:
            for var in hf.keys():
                self.fdata[var] = np.array(hf[var])

        self.plotting_variables = variables
        self.plotting_flavors = flavors
        self.plotting_cp = cp
        self.plotting_interaction = interaction
        self.plotting_samples = samples

        self.variable_names = {}
        self.variable_labels = {}
        self.aux_variables = {}

        self.samples = []

    def find_variable(self, variable_name):
        """ Find variable in file given the name.
        Args:
            variable_name (str): Name of the variable

        Returns:
            str with the name of the variable in simulation file or False if
            the variable was not found
        """
        for k, names in enumerate(self.variable_names.values()):
            if variable_name in names:
                return list(self.variable_names.keys())[k]
        print(f'Variable {variable_name} not found.')
        return False

    def plot_variable(self, variable_name, cuts, cut_labels):
        """ Find and plot a given variable. """
        variable = self.find_variable(variable_name)
        if variable:
            """ Select variable data """
            array = self.fdata[variable]
            """ Setup plots """
            rows, cols = self.grid_plots()
            fig, axes = plt.subplots(
                nrows=rows, ncols=cols, figsize=(
                    3 * cols, 2.75 * rows))
            axis = axes.flat
            for i,s in enumerate(self.plotting_samples):
                bins = 20
                for k, (c, ctag) in enumerate(zip(cuts, cut_labels)):
                    c_and_sample = c * self.get_sample(s)
                    __, bins, __ = axis[i].hist(array[c_and_sample], bins=bins, stacked=True, label=ctag)
                axis[i].set_title(self.samples[s], fontsize=11)
                axis[i].set_xlabel(self.variable_labels[variable], fontsize=10)
                axis[i].legend(loc="best")
                ymin, ymax = axis[i].get_ylim()
                axis[i].set_ylim([0, 1.4 * ymax])

            fig.tight_layout()
            plt.show()
            plt.clf()

    def grid_plots(self):
        nsamples = len(self.plotting_samples)
        if nsamples < 4:
            return 1, nsamples
        else:
            sq = sqrt(nsamples)
            return int(sq), int(round(sq)) + 1

    def plot(self):
        """ Plot all the variables requested. """
        cuts, cut_labels = self.cuts_and_breakdown()
        for var in self.plotting_variables:
            self.plot_variable(var, cuts, cut_labels)


    def cuts_and_breakdown(self):
        """ Computes the cuts and breakdowns for the plots based on the
        input parameters.
        Returns:
            [Name of cut, List of cuts]
        """
        cuts = []
        cut_labels = []

        """ Samples """
        if self.plotting_samples == "All":
            self.plotting_samples = range(len(self.samples))
        else:
            if "tracks" in self.plotting_samples:
                i = self.plotting_samples.index("tracks")
                self.plotting_samples[i] = 0
            elif "cascades" in self.plotting_samples:
                i = self.plotting_samples.index("cascades")
                if len(self.samples) == 3:
                    self.plotting_samples[i] = 2
                else:
                    self.plotting_samples[i] = 1
            elif "intermediate" in self.plotting_samples:
                i = self.plotting_samples.index("intermediate")
                self.plotting_samples[i] = 1
            else:
                self.plotting_samples = list(map(int, self.plotting_samples))

        """ Flavors """
        if self.plotting_flavors == "e":
            self.plotting_flavors = [self.get_nue()]
        elif self.plotting_flavors == "mu":
            self.plotting_flavors = [self.get_numu()]
        elif self.plotting_flavors == "e+mu":
            self.plotting_flavors = [self.get_numu(), self.get_nue()]
        elif self.plotting_flavors == "tau":
            self.plotting_flavors = [self.get_nutau()]

        """ (Anti)neutrinos """
        if self.plotting_cp == "nu":
            self.plotting_cp = [self.get_neutrino()]
        elif self.plotting_cp == "antinu":
            self.plotting_cp = [self.get_antineutrino()]
        elif self.plotting_cp == "both":
            self.plotting_cp = [self.get_neutrino(), self.get_antineutrino()]

        """ Interactions """
        if self.plotting_interaction == "CC":
            self.plotting_interaction = [self.get_CC()]
        elif self.plotting_interaction == "NC":
            self.plotting_interaction = [self.get_NC()]
        elif self.plotting_interaction == "ALL":
            self.plotting_interaction = [self.get_CC(), self.get_NC()]
        elif not self.plotting_interaction:
            self.plotting_interaction = [self.get_alltrue()]

        for fl, cp, mode in product(self.plotting_flavors, self.plotting_cp, self.plotting_interaction):
            cuts.append(mode[1] * cp[1] * fl[1])
            cut_labels.append(mode[0] + cp[0] + fl[0])

        return cuts, cut_labels


    def print_samples(self):
        print(
            f"\nList of event samples for {self.experiment}\n---------------------------------------------\nIndex  -  Name")
        for i, name in enumerate(self.samples):
            print(f"  {i}  ---  {name}")
        print("\n")


    def get_CC(self):
        pass

    def get_NC(self):
        pass

    def get_numu(self):
        pass

    def get_nue(self):
        pass

    def get_nutau(self):
        pass

    def get_neutrino(self):
        pass

    def get_antineutrino(self):
        pass

    def get_alltrue(self):
        pass

    def get_sample(self):
        pass