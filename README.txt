AUTHOR: Marc Santiago
EMAIL: marcanthonysanti@gmail.com
This module is intended to provided users with a quick and simple way to
perform a one time pad encryption on text files and strings. 

Getting the Module:
-------------------------------------------------
pip install OneTimePadEncryption
OR
Download the zip file from github

Usage:
Import Module
-------------------------------------------------
from OTP import OneTimePadEncryption
opt = OneTimePadEncryption.OneTimePadEncryption()

Methods:
-------------------------------------------------
opt.decrypt_string_or_file(key, encrypted_string, key_file_mode=False, encrypted_string_file_mode=False)
Usage: Method that takes either the key or the encrypted string as a string or can the key and encrypted string a as file and decrypts the string using the provided string. NOTE** In order to use the the key.dat file you must first also be able to unzip it using a password.

opt.encrypt_string_or_file(plain_text, string_file_mode=False):
Usage: Method that takes either the key or plaintext as a string or file. The key is randomly generated for you and save as a zip.

A COMMAND LINE TOOL HAS BEEN PROVIDED FOR YOU:
FILE NAME: cmd_otp_utility.py
FILE LOCATION: https://github.com/marcsantiago/one_time_pad_encryption/blob/master/cmd_otp_utility.py
