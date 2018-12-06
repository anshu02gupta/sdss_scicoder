
import argparse
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from plot import plot as pl #Giulia
from read_fits import Read_fits as rf #Anshu
from read_fits import Galaxy_info as Gal_Info #Anshu
from emission_line_ratios import Emission_line as Em_Line

#parsing the file to be plotted from the user. -- STEP-1
parser = argparse.ArgumentParser(description = "This program reads sdss spectrum and does following functions: 1) Plot all galaxy spectra 2)Plot equiwalewnt widths for each line for all galaxies 3) plots BPT diagram ", usage = "getfiles.py --foldername <foldername> ")
parser.add_argument("-f","--foldername", help = "Path to the folder containing spectrum fits files")
args = parser.parse_args()

ew,ew_err,line_wave =[[]],[[]],[[]]

#getting all the spectra in the folder and the galaxy properties for each spectra
i=0
for file in glob(args.foldername+"/*.fits",recursive=True):
    name  = (file.split("/")[8]).rstrip(".fits")
    #Reading file to get wavelength and flux and error spectrum
    galaxy = rf(file)
    wavelength = galaxy.wavelength
    flux_spectrum = galaxy.flux
    error_spectrum = galaxy.error
    
    #Getiing galaxy properties-- provide filename to the gal_info
    gal_props = Gal_Info(file)
    line_names =(list(gal_props.spectral_lines["linename"]))
    line_wave.append(list(gal_props.spectral_lines["linewave"]))
    ew.append(list(gal_props.spectral_lines["ew"]))
    ew_err.append(list(gal_props.spectral_lines["ew_err"]))
    redshift  = gal_props.redshift["z"]
    redshift_err = gal_props.redshift["z_err"]
    redshift=[ x for x in redshift if x != 0.0]
    
    mean_redshift = np.mean(np.array(redshift))
    
    #plotting and saving all spectra
    pl(wavelength,flux_spectrum,error_spectrum,r"$Wavelength\  (\AA)$", r"$flux (10^{-17} ergs/s/cm^2/\AA)$","plot","/Users/z5189882/Documents/confandstuff/scicoder2018/sdss_scicoder/customroutines/test_spectra/"+name,mean_redshift)
    O3_Hb=(Em_Line(gal_props.spectral_lines["linename"], gal_props.spectral_lines["ew"], gal_props.spectral_lines["ew_err"], '[O_III] 5007', 'H_beta'))
    O3_Hb_ratio = (O3_Hb.line_ratio())
    N2_Ha=(Em_Line(gal_props.spectral_lines["linename"], gal_props.spectral_lines["ew"], gal_props.spectral_lines["ew_err"], '[N_II] 6583', 'H_alpha'))
    N2_Ha_ratio = (N2_Ha.line_ratio())
    print(O3_Hb_ratio["lineratio"],O3_Hb_ratio["lineratio_err"])
    print(N2_Ha_ratio["lineratio"],N2_Ha_ratio["lineratio_err"])
    

    i=i+1

color=iter(cm.rainbow(np.linspace(0,1,20)))
for i in range(len(ew)):
    c=next(color)
    plt.errorbar(line_wave[i], ew[i], ew_err[i], marker = 'o', mfc = c, mec ='black', mew=2, ls ='None', ecolor= c, capsize = 4,markersize=5)
plt.xlabel("lines")
plt.ylabel("equivalent widths")
plt.ylim(-100,500)
plt.savefig("/Users/z5189882/Documents/confandstuff/scicoder2018/sdss_scicoder/customroutines/test_spectra/equivalent_width.pdf")
    #ploting eq_widths vs linenames for each galaxy
#    eq_width_plot = pl(line_wave,ew,"lines","equivalent widths", "scatter",ew_err)


#eq_width_plot.savefig("/Users/z5189882/Documents/confandstuff/scicoder2018/sdss_scicoder/customroutines/test_spectra/equivalent_width.pdf")
