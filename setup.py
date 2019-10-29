import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spoken_to_written',
      packages = ['spoken_to_written'],
      version='0.1',
      license=open('LICENSE.txt').read(),
      description='Correct Spoken English given as text to Written English ',
      author='Mushtaq Patel',
      author_email='mushtaqpatel0505@gmail.com',
      url='https://github.com/mushtaqpatel0505/Correcting-paragraphs-of-spoken-english-to-written-english',
      classifiers = [
     					 'Intended Audience :: Developers',
      					'Programming Language :: Python'
  				],
	  long_description=open_file('README.rst').read()

     )