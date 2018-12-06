from astropy.io import fits


class Read_fits(object):
	def __init__(self, filename):
		if filename is None:
			print("No filename specified")
		else:
			self.filename = filename
			self.hdu = fits.open(self.filename)
			#self.data = self.hdu[1].data
#			print(self.hdu.info())
			#print(self.data[1])
	@property
	def wavelength(self):
		"""Wavelength binning, linear bins."""
		if getattr(self,'_wavelength',None) is None:
			self._wavelength = 10**self.hdu[1].data['loglam']
		return self._wavelength

	@property
	def flux(self):
		if getattr(self,'_flux',None) is None:
			self._flux = self.hdu[1].data['flux']
		return self._flux

	@property
	def error(self):
		if getattr(self,'_ivar',None) is None:
			self._error = self.hdu[1].data['ivar']
		return self._error
		

class Galaxy_info(object):
	def __init__(self, filename):
		if filename is None:
			print("No filename specified")
		else:
			self.filename = filename
			self.hdu = fits.open(self.filename)
		
	@property
	def redshift(self):
		if getattr(self,'_LINEZ',None) is None:
			self._redshift = dict()
			self._redshift["z"] = self.hdu[3].data['LINEZ']
			self._redshift["z_err"] = self.hdu[3].data['LINEZ_ERR']
			#print(self.hdu[3].data['LINEZ'])
			return self._redshift
		
	@property
	def spectral_lines(self):
		if getattr(self,'_LINENAME',None) is None:
			self._spectral_lines = dict()
			self._spectral_lines["linename"] = self.hdu[3].data['LINENAME']
			self._spectral_lines["linewave"] = self.hdu[3].data['LINEWAVE']
			self._spectral_lines["ew"] = self.hdu[3].data['LINEEW']
			self._spectral_lines["ew_err"] = self.hdu[3].data['LINEEW_ERR']
			#print(self.hdu[3].data['LINEZ'])
			return self._spectral_lines
		



#filename = '/Users/z3525264/Documents/work/SciCoder-2018-Sydney/sdss_scicoder/spectra/spec-10000-57346-0002.fits'

#sdss_galaxy = Galaxy_info(filename)
#print(sdss_galaxy.spectral_lines["linename"])
