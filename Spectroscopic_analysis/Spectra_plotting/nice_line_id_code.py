
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
import lineid_plot

spec = fits.open('finalspecmedian.fits')

hdr = spec[0].header
data = spec[0].data

crval1 = hdr['CRVAL1']
cd11 = hdr['CD1_1']

wave = crval1 + np.arange(len(data))*cd11
flux = data/(1e-15)

line_wave = [3729.875, 3868.65, 3889, 3969.588, 4103,  4341.68, 4364.44, 4862.68, 4960,  5007 , 6564.61, 6585.27]
line_wave = [(1+0.0063)*x for x in line_wave]
line_label1 = ['O II', 'NaII', 'He I', 'Ca H', 'H$\\delta$', 'H$\\gamma$', 'OIII', 'H$\\beta$', 'O III',  'OIII', "H$\\alpha$", 'NII']

ak = lineid_plot.initial_annotate_kwargs()
ak
{'arrowprops': {'arrowstyle': '-', 'relpos': (0.5, 0.0)},
'horizontalalignment': 'center',
'rotation': 90,
'textcoords': 'data',
'verticalalignment': 'center',
'xycoords': 'data'}
ak['arrowprops']['arrowstyle'] = "-"

pk = lineid_plot.initial_plot_kwargs()
pk
{'color': 'k', 'linestyle': '--'}
pk['color'] = "black"

lineid_plot.plot_line_ids(wave, flux, line_wave, line_label1, color='black', annotate_kwargs=ak, plot_kwargs=pk)
plt.title('Final Data Reduction Product: Median scombined Spectrum for Galaxy UM285', pad=60, fontsize=16)
plt.xlabel(u'Wavelength $\lambda$ [\u212b]', fontsize=13)
plt.ylabel(u'Calibrated Flux [ 1e-15 erg/s/cm$^{2}$/\u212b]', fontsize=13)
plt.show()

lambda_obs = [3756.98, 3893.78, 3913.66, 3993.62, 4127.53, 4367.78, 4390.65, 4891.89, 4989.78, 5038.01, 6604.07, 6624.85]
lambda_obs_u = [2.78, 2.34,2.02, 2.55, 2.39, 2.54, 2.52, 2.44, 2.47, 2.48, 2.49, 2.35]
lambda_rest = [3732.135, 3871.26, 3888.648, 3968.47, 4101.734, 4340.472, 4363.209, 4861.283363, 4958.911, 5006.843, 6562.70970, 6583.45]
lambda_rest_u = [0.001, 0.01, 0.001, 0.01, 0.006, 0.006, 0.001, 0.000024, 0.001, 0.001, 0.00004, 0.01]


z = [(x - y)/y for x,y in zip(lambda_obs, lambda_rest)]


u_z = [((x-y)/y)*(((u_x/x)**2 + (u_y/y)**2)**(1/2)) for x, u_x, y, u_y in zip(lambda_obs, lambda_obs_u, lambda_rest, lambda_rest_u)]

for red, u_red in zip(z, u_z):
    print(np.round(red,7) , np.round(u_red,7))