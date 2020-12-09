#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

# Create format to write logs
formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Create custom class for managment logging into this tools
# Require 3 argument:
# * scriptPath <- Path where the script is stored
# * loggingLevel <- File name for the log file
class LogginConfig ():
  def __init__(self,scriptPath,loggingLevel):
    loggingFullFileName = scriptPath + '/code-encode.log'
    try:
      logging.basicConfig(filename=loggingFullFileName,format=formatter,level=loggingLevel)
    except PermissionError:
      print("Unable to write to log file")
      print('Forced stop script')
      exit(1)
    except FileNotFoundError:
      print("Not found directory for logs: " + loggingFullFileName)
      print('Forced stop script')
      exit(1)
  
  # It is used to process INFO type logs.
  # Requires an argument of type string, which must contain the message to save.
  def info(self, message,printOff = False):
        logging.info(message)
        if printOff == False:
          print(message)

  # It is used to process DEBUG type logs.
  # Requires an argument of type string, which must contain the message to save.
  def debug(self, message):
        logging.debug(message)