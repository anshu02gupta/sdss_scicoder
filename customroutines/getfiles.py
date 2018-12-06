
import argparse
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from plot import plot as pl #Giulia
from read_fits import Read_fits as rf #Anshu
from read_fits import Galaxy_info as gal_info #Anshu
#parsing the file to be plotted from the user. -- STEP-1
parser = argparse.ArgumentParser(description = "This program reads sdss spectrum and plots them", usage = "final_module_name --foldername <foldername> ")
parser.add_argument("-f","--foldername", help = "Path to the folder containing spectrum fits files")
args = parser.parse_args()

ew,ew_err,line_wave =[[]],[[]],[[]]

#getting all the spectra in the folder and the galaxy properties for each spectra

for file in glob(args.foldername+"/*.fits",recursive=True):
    name  = (file.split("/")[8]).rstrip(".fits")
    #Reading file to get wavelength and flux and error spectrum
    galaxy = rf(file)
    wavelength = galaxy.wavelength
    flux_spectrum = galaxy.flux
    error_spectrum = galaxy.error
    
    #Getiing galaxy properties-- provide filename to the gal_info
    gal_props = gal_info(file)
    line_names =(list(gal_props.spectral_lines["linename"]))
    line_wave.append(list(gal_props.spectral_lines["linewave"]))
    ew.append(list(gal_props.spectral_lines["ew"]))
    ew_err.append(list(gal_props.spectral_lines["ew_err"]))
    redshift  = gal_props.redshift["z"]
    redshift_err = gal_props.redshift["z_err"]
    redshift=[ x for x in redshift if x != 0.0]
    
    mean_redshift = np.mean(np.array(redshift))
    
    #plotting and saving all spectra
    pl(wavelength,flux_spectrum,r"$Wavelength\  (\AA)$", r"$flux (10^{-17} ergs/s/cm^2/\AA)$","plot",error_spectrum,"/Users/z5189882/Documents/confandstuff/scicoder2018/sdss_scicoder/customroutines/test_spectra/"+name,mean_redshift)

color=iter(cm.rainbow(np.linspace(0,1,)))
for i in range(3):
    c=next(color)
    plt.errorbar(line_wave[i], ew[i], ew_err[i], marker = 'o', mfc = c, mec ='black', mew=2, ls ='None', ecolor= c, capsize = 4,markersize=5)
plt.xlabel("lines")
plt.ylabel("equivalent widths")
plt.ylim(-100,500)
plt.savefig("/Users/z5189882/Documents/confandstuff/scicoder2018/sdss_scicoder/customroutines/test_spectra/equivalent_width.pdf")
    #ploting eq_widths vs linenames for each galaxy
#    eq_width_plot = pl(line_wave,ew,"lines","equivalent widths", "scatter",ew_err)


#eq_width_plot.savefig("/Users/z5189882/Documents/confandstuff/scicoder2018/sdss_scicoder/customroutines/test_spectra/equivalent_width.pdf")
