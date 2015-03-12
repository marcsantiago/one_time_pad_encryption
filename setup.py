import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'OneTimePadEncryption',
  packages = ['OTP'],
  version = '2.0.1',
  author = 'Marc Santiago',
  author_email = 'marcanthonysanti@gmail.com',
  url = 'https://github.com/marcsantiago/one_time_pad_encryption', 
  download_url = 'https://github.com/marcsantiago/one_time_pad_encryption/tarball/0.1', 
  keywords = ['encryption', 'one time pad'],
  description = 'This module is intended to provided users with a quick and simple way to perform\
  a one time pad encryption on text files and string.  It will work with python 2 or 3.', 
  long_description=read('README.txt'),
  classifiers = [],
)
