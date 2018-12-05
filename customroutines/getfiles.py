import argparse
import plot.py as pl #Giulia
import Read_fits from read_fits.py as rf #Anshu
#parsing the file to be plotted from the user. -- STEP-1
parser = argparse.ArgumentParser(description = "This program reads sdss spectrum and plots them", usage = "final_module_name --filename <filename.fits> ")
parser.add_argument("-f","--filename", help = "Path to the spectrum fits file")
args = parser.parse_args()

#Reading file to get wavelength and flux
wavelegth = rf.wavelength(args.filename)
flux = rf.flux(args.filename)
error = rf.error(args.filename)
print(args)

