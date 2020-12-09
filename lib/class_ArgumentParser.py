#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Config argument
from argparse import ArgumentParser

# Class to create argument parser configuration.
class LoadArgumentParser():  
  #Startup parser and define argument to use
  def __init__(self):
    self.parser = ArgumentParser(description='Aplicacion para cifrar y decifrar archivospara Base64 ')
    self.parser.add_argument('-d','--decode',default=False,help='Decore File content form base64',action='store_true')
    self.parser.add_argument('-e','--encode',default=False,help='Code File content to base64',action='store_true')
    self.parser.add_argument('-f','--file',help='File to use',nargs=1)
    self.parser.add_argument('-v','--version',default=False,help='Show Version',action='store_true')
    self.parser.add_argument('-vvv','--verbose',default=False,help='Start logging in verbose mode',action='store_true')
    self.parserARGS = self.parser.parse_args()
  
  # Expose status for 'version' argument 
  def getArgsVersion(self):
    return self.parserARGS.version 

  # Expose status for 'decode' argument 
  def getArgsDecode(self):
    return self.parserARGS.decode
  
  # Expose status for 'code' argument 
  def getArgsEncode(self):
    return self.parserARGS.encode  

  # Expose status for 'verbose' argument 
  def getArgsVerbose(self):
    return self.parserARGS.verbose  

  # Expose status for 'file' argument
  def getArgsFileName(self):
    if not type(self.parserARGS.file) == None.__class__:
      return self.parserARGS.file[0]
    else:
      return False
