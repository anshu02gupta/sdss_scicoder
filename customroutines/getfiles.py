
import argparse
from glob import glob
from plot import plot as pl #Giulia
from read_fits import Read_fits as rf #Anshu
from read_fits import Galaxy_info as gal_info #Anshu
#parsing the file to be plotted from the user. -- STEP-1
parser = argparse.ArgumentParser(description = "This program reads sdss spectrum and plots them", usage = "final_module_name --foldername <foldername> ")
parser.add_argument("-f","--foldername", help = "Path to the folder containing spectrum fits files")
args = parser.parse_args()


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
    line_names = gal_props.spectral_lines["linename"]

    ew = gal_props.spectral_lines["ew"]
    ew_err = gal_props.spectral_lines["ew_err"]
    redshift  = gal_props.redshift["z"]
    redshift_err = gal_props.redshift["z_err"]

    #print(line_names) # galaxy props works so far

    #plotting and saving all spectra
    pl(wavelength,flux_spectrum,r"$Wavelength (\AA)$", r"$flux (10^(-17) ergs/s/cm^2/ \AA)$","plot",error_spectrum,name)

    #ploting eq_widths vs linenames for each galaxy
    pl(line_names,ew,ew_err)
