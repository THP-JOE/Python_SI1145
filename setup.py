from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'TMP007',
	  version 			= '1.0.0',
	  author			= 'Joe Gutting',
	  author_email		= 'gutting@gmail.com',
	  description		= 'Library for accessing the TMP007 temperature sensor on a Raspberry Pi. Uses Adafruit GPIO I2C. Credit to Tony Dicola as used his BMP library.  Also credit to Adafruit for TMP007 Arduino library',
	  license			= 'MIT',
	  url				= 'https://github.com/THP-JOE/Python_TMP007.git',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.2.0'],
	  install_requires	= ['Adafruit-GPIO>=0.2.0'],
	  packages 			= find_packages())
