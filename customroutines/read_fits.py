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


filename = '/Users/z3525264/Documents/work/SciCoder-2018-Sydney/sdss_scicoder/spectra/spec-10000-57346-0002.fits'

sdss_galaxy = Read_fits(filename)
print(sdss_galaxy.wavelength, sdss_galaxy.flux, sdss_galaxy.error)
