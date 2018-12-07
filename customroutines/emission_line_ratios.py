import numpy as np 

####################Calling Sequence###########################
#from read_fits import Galaxy_info #Anshu

#USUAL keywords for emission lines = ['[O_III] 5007', '[N_II] 6583','H_alpha', 'H_beta', '[S_II] 6716','[S_II] 6730']
#filename = '/Users/z3525264/Documents/work/SciCoder-2018-Sydney/sdss_scicoder/spectra/spec-10000-57346-0002.fits'
#sdss_galaxy = Galaxy_info(filename)
#line_ratios = Emission_line(sdss_galaxy.spectral_lines["linename"], sdss_galaxy.spectral_lines["ew"], sdss_galaxy.spectral_lines["ew_err"],'[O_III] 5007', 'H_beta')
#print(line_ratios.line_ratio())
		


class Emission_line(object):
	def __init__(self, linename, ew, ew_err, lineNum=None, lineDe=None):
		if ew_err is None:
			print ("Supply linenames")
		else:
			self.linename = linename
		if ew_err is None:
			print ("Supply EW")
		else:
			self.ew = ew
		if ew_err is None:
			print ("Supply EW errors")
		else:
			self.ew_err = ew_err
		if lineNum is None or lineDe is None:
			print ("Supply lines to measure emission lines")
		else:
			self.lineNum = lineNum
			self.lineDe = lineDe
		
			
	def line_ratio(self):
		self.line_ratio = dict()
		ew_ln1 = self.ew[self.linename == self.lineNum]
		ew_ln2 = self.ew[self.linename == self.lineDe]
		ew_ln1_err = self.ew_err[self.linename == self.lineNum]
		ew_ln2_err = self.ew_err[self.linename == self.lineDe]
		
		
		if ew_ln1 > 0.0 and ew_ln2 > 0.0 and np.isfinite(ew_ln1) and np.isfinite(ew_ln2):
			self.line_ratio["lineratio"]  = np.log10(ew_ln1/ew_ln2)
			self.line_ratio["lineratio_err"]  = np.sqrt((np.power(ew_ln1_err/ew_ln1, 2)+ np.power(ew_ln2_err/ew_ln2,2)))/(ew_ln2*np.log(10)/ew_ln2)
            
		else:
			self.line_ratio["lineratio"] = None
			self.line_ratio["lineratio_err"] = None
		return self.line_ratio
		

		

	

