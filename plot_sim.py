import argparse
import sys


def main():

    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()  # Edited this line
    required = parser.add_argument_group("required arguments")
    required.add_argument(
        "--experiment",
        type=str,
        nargs="?",
        choices=("SK", "SK-Htag", "SK-Gd", "ORCA", "ICUp", "HK"),
        required=True,
        help="Experiment you would like to use.")
    required.add_argument(
        "--fname",
        type=str,
        nargs="?",
        required=True,
        help="Path to simulation file of the experiment you would \
        like to use (SK, SK-Htag, SK-Gd, ORCA, ICUp or HK).")
    optional.add_argument(
        "--variables",
        type=str,
        nargs="+",
        default=("Enu", "reco_coszen", "reco_energy"),
        help="Set of variables you want to plot.")
    optional.add_argument(
        "--flavor",
        type=str,
        nargs="?",
        choices=("e", "mu", "e+mu", "tau"),
        default="e+mu",
        help="Flavor cut and breakdown.")
    optional.add_argument(
        "--CP",
        type=str,
        nargs="?",
        choices=("nu", "antinu", "both"),
        default="both",
        help="Flavor cut and breakdown.")
    optional.add_argument(
        "--interaction",
        type=str,
        nargs="?",
        choices=("CC", "NC", "ALL", False),
        default=False,
        help="Interaction mode(s) cut and breakdown.")
    optional.add_argument(
        "--samples",
        type=str,
        nargs="?",
        default="All",
        help="Comma separated set of event samples you want to plot \
        (for IC: tracks or cascades; for ORCA: tracks, intermediate or cascades; \
        for SK and HK numerical indeces (displayed when calling these detectors)).")
    parser._action_groups.append(optional)
    args = parser.parse_args()

    input_file = args.fname
    experiment = args.experiment
    variables = args.variables
    flavors = args.flavor
    interaction = args.interaction
    cp = args.CP
    if "," in args.samples:
        samples = [int(item) for item in args.samples.split(',')]
    else:
        samples = args.samples

    """ Telling which variables the program is about to plot."""
    print("\nVariables to be plotted\n-------------------------------------")
    for variable in variables:
        print(f"  + {variable}")

    r""" Calling each experiment"s plotting module. One-dimensional non-oscillated
    variable  distributions will be displayed. For additional plots and breakdowns,
    please look at the experiment module.
    For illustration purposes of how the weights are defined in the MC files, the
    exposure assumed is 1 year with the caveat that tau neutrinos are not produced
    in the atmosphere and in the simulations, they assume the muon neutrino flux.
    """

    if experiment == "ICUp":
        from south_pole import IC
        exp = IC(input_file, variables, flavors, cp, interaction, samples)
        exp.plot()
    elif experiment == "ORCA":
        from mediterranean import ORCA
        exp = ORCA(input_file, variables, flavors, cp, interaction, samples)
        exp.plot()
    elif experiment == "SK":
        from kamioka import SK
        exp = SK(input_file, variables, flavors, cp, interaction, samples)
        exp.plot()
    elif experiment == "SK-Htag":
        from kamioka import SK_Htag
        exp = SK_Htag(input_file, variables, flavors, cp, interaction, samples)
        exp.plot()
    elif experiment == "SK-Gd":
        from kamioka import SK_Gd
        exp = SK_Gd(input_file, variables, flavors, cp, interaction, samples)
        exp.plot()
    elif experiment == "HK":
        from kamioka import HK
        exp = HK(input_file, variables, flavors, cp, interaction, samples)
        exp.plot()


# ------------------------------------------------------- #
if __name__ == "__main__":
    main()


# if var != "ALL":
#     f1 = h5py.File(input_file, "r")
#     ds = f1[var]
#     data = np.array(ds[()])
#     typ = np.array(f1["itype"][()])
#     for i in range(16):
#         plt.hist(data[typ==i], bins=50, density=False, stacked=True)
#         plt.show()
#         plt.clf()
# else:
#     for key in f1.keys():
#     #    print(key)
#         ds = f1[key]
#         dat = np.array(ds[()])
#     #    print(data)
#         for i in range(16):
#             for nu in [-16,-14,-12,12,14,16]:
#                 data = dat[neu==nu]
#                 w = wo[neu==nu]
#                 typ = ityp[neu==nu]
#                 # plt.hist(data[typ==i-1], weights=w[typ==i-1], bins=20, density=False, stacked=True, label=str(nu))
#                 plt.hist(data[typ==i-1], bins=50, density=False, stacked=True, label=str(nu))
#             plt.legend()
#             plt.savefig("../figs/"+key+"_"+str(i-1)+".png")
#             print("Histogram saved to ", "figs/"+key+".png")
#             # plt.yscale("log")
#             # plt.savefig("figs/"+key+"_"+str(i-1)+"_log.png")
#             plt.clf()
