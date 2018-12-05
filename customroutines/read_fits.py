from astropy.io import fits

filename = 'spectra/spec-10000-57346-0002.fits'

class Read_fits(Object):
	def __init__(self, filename):
	if filename is None:
		print("No filename specified")
	self.filename = filename
	hdu = fits.open(filename)
	data = hdu[1].data
	
	@property
    def wavelength(self):
        """Wavelength binning, linear bins."""
        if getattr(self,'_wavelength',None) is None:
            self._wavelength = 10**self.data[1].data['loglam']
        return self._wavelength

    @property
    def flux(self):
        if getattr(self,'_flux',None) is None:
            self._flux = self.data[1].data['flux']
        return self._flux