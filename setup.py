from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'SI1145',
	  version 			= '1.0.0',
	  author			= 'Joe Gutting',
	  author_email		= 'gutting@gmail.com',
	  description		= 'Library for accessing the SI1145 UV sensor on a Raspberry Pi. Uses Adafruit GPIO I2C. Credit to Tony Dicola as used his BMP library.  Also credit to Adafruit for SI1145 Arduino library',
	  license			= 'MIT',
	  url				= 'https://github.com/THP-JOE/Python_SI1145.git',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.2.0'],
	  install_requires	= ['Adafruit-GPIO>=0.2.0'],
	  packages 			= find_packages())
