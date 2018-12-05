import argparse
import plot.py as pl
import read_fits.py as rf
parser = argparse.ArgumentParser(description = "This program reads sdss spectrum and plots them", usage = "final_module_name --filename <filename.fits> ")
parser.add_argument("-f","--filename", help = "Path to the spectrum fits file")
args = parser.parse_args()
print(args)

