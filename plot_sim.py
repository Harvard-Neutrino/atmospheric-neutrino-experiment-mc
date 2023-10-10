import h5py
import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    'fname',
    type=str,
    nargs='?',
    default='NULL',
    help='Experiment or experiments you would like to use (SK, SK-Htag, \
    SK-Gdtag, ORCA, ICUp or HK).')
parser.add_argument(
    'variable',
    type=str,
    nargs='?',
    default='NULL',
    help='Set of variables you want to plot.')
args = parser.parse_args()
input_file = args.fname
variables = args.variable

''' Require at least one input experiment '''
if input_file == 'NULL':
    sys.exit('Please introduce the name of the experiment.')

''' Telling which variables the program is about to plot.'''
if variables == 'NULL':
    print('NOTE: Using default variables.')
    variables = default_variables
print('Variables to be plotted:')
for variable in variables:
    print(f' - {variable}')

r''' Calling each experiment's plotting module. One-dimensional variable \
distributions will be displayed and saved split in analysis samples and break \
down by interaction mode group and neutrino species:
 - CC $\nu_{e}$
 - CC $\overline{\nu_{e}}$
 - CC $\nu_{\mu}$
 - CC $\overline{\nu_{\mu}}$
 - CC $\nu_{\tau} + \overline{\nu_{\tau}}$
 - NC
 Alternative and more detailed breakdowns require code modifications at each \
 experiments module.'''








# if var != 'ALL':
#     f1 = h5py.File(input_file, 'r')
#     ds = f1[var]
#     data = np.array(ds[()])
#     typ = np.array(f1['itype'][()])
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
#             plt.savefig('../figs/'+key+'_'+str(i-1)+'.png')
#             print('Histogram saved to ', 'figs/'+key+'.png')
#             # plt.yscale('log')
#             # plt.savefig('figs/'+key+'_'+str(i-1)+'_log.png')
#             plt.clf()
