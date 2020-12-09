#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Mantainer: Pablo Tessarolo (pablo.te)

import sys, os
from settings import *

if ArgumentParserInst.getArgsVersion():
  print('Author: Morgok857')
  print('Version: 1.0')

# The source file is validated to exist 
if not CheckExistFile(ArgumentParserInst.getArgsFileName()):
  loggingInst.info("Target file not found")

# If the encrypt and decrypt flags are active at the same time, 
# the execution of the program is stopped and the user is notified that it cannot continue
if ArgumentParserInst.getArgsEncode() == True and ArgumentParserInst.getArgsDecode() == True:
  loggingInst.info('The encrypt and decrypt flags are active at the same time. Please remove those that do not apply.')
  loggingInst.debug('Force stop script')
  exit(6)

# This task is executed if the Decode Flag is active.
# The file passed by parameter is read, the content of each key is deciphered and a 
# file is created with the result.
if ArgumentParserInst.getArgsDecode() == True:
  loggingInst.info("Start to read and decode file: " + ArgumentParserInst.getArgsFileName())
  if decodeBase64(ArgumentParserInst.getArgsFileName()):
    loggingInst.info('Task completed successfully')
    exit(0)
  else:
    loggingInst.info('Task could not be completed')
    exit(7)

# This task is executed if the Encode Flag is active. 
# The file passed by parameter is read, the content of each key is encrypted and a 
# file is created with the result.
if ArgumentParserInst.getArgsEncode() == True or ArgumentParserInst.getArgsDecode() == False:
  loggingInst.info("Start to read and encode file: " + ArgumentParserInst.getArgsFileName())
  if encodeBase64(ArgumentParserInst.getArgsFileName()):
    loggingInst.info('Task completed successfully')
    exit(0)
  else:
    loggingInst.info('Task could not be completed')
    exit(8)