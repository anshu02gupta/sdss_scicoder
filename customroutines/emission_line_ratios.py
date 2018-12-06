import numpy as np 

#from read_fits import Galaxy_info #Anshu

class Emission_line(object):
	def __init__(self, linename, ew, ew_err):
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
			
	def line_ratios(self):
		self.line_ratios = dict()
		ew_o3 = self.ew[self.linename == '[O_III] 5007']
		ew_n2 = self.ew[self.linename == '[N_II] 6583']
		ew_ha = self.ew[self.linename == 'H_alpha']
		ew_hb = self.ew[self.linename == 'H_beta']
		ew_s2 = self.ew[self.linename == '[S_II] 6716'] + self.ew[self.linename == '[S_II] 6730'] 
		print(ew_ha, ew_hb)
		ew_o3_err = self.ew_err[self.linename == '[O_III] 5007']
		ew_n2_err = self.ew_err[self.linename == '[N_II] 6583']
		ew_ha_err = self.ew_err[self.linename == 'H_alpha']
		ew_hb_err = self.ew_err[self.linename == 'H_beta']
		ew_s2_err = np.sqrt(self.ew_err[self.linename == '[S_II] 6716']**2 + self.ew[self.linename == '[S_II] 6730']**2) 
		
		if ew_hb !=0.0 and ew_o3 != 0.0:
			self.line_ratios["o3hb"]  = np.log10(ew_o3/ew_hb)
			self.line_ratios["o3hb_err"]  = np.sqrt((np.power(ew_o3_err/ew_o3, 2)+ np.power(ew_hb_err/ew_hb,2)))/(ew_o3*np.log(10)/ew_hb)		
		else:
			self.line_ratios["o3hb"] = None
			self.line_ratios["o3hb_err"] = None
			
	
		if ew_ha != 0.0 and ew_n2 != 0.0:
			self.line_ratios["n2ha"]  = np.log10(ew_n2/ew_ha)
			self.line_ratios["n2ha_err"]  = np.sqrt((np.power(ew_n2_err/ew_n2, 2)+ np.power(ew_ha_err/ew_ha,2)))/(ew_n2*np.log(10)/ew_ha)
		else:
			self.line_ratios["n2ha"] = None
			self.line_ratios["n2ha_err"] = None

		if ew_ha != 0.0 and ew_s2 != 0.0:	
			self.line_ratios["s2ha"]  = np.log10(ew_n2/ew_ha)
			self.line_ratios["s2ha_err"]  = np.sqrt((np.power(ew_s2_err/ew_s2, 2)+ np.power(ew_ha_err/ew_ha,2)))/(ew_s2*np.log(10)/ew_ha)
		else: 
			self.line_ratios["s2ha"] = None
			self.line_ratios["s2ha_err"] = None
			
		
		return self.line_ratios
		

		

####################Calling Sequence###########################

#line_ratios = Emission_line(sdss_galaxy.spectral_lines["linename"], sdss_galaxy.spectral_lines["ew"], sdss_galaxy.spectral_lines["ew_err"])

#print(line_ratios.line_ratios())
		
	

