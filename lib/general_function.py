#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os
import base64
from lib.class_ArgumentParser import *
from lib.class_logging import *

# Get Script home path
scriptPath = os.path.dirname(os.path.realpath(__file__))

# Load Argument Parser
ArgumentParserInst = LoadArgumentParser()

# Load configuration logs
if ArgumentParserInst.getArgsVerbose():
  logLevel = 'DEBUG'
else:
  logLevel = 'INFO'
loggingInst = LogginConfig(scriptPath + '/../', logLevel)

# This function validates if a file exists.
# It requires that the path of the file to be validated be passed as a parameter.
def CheckExistFile (fileCheck):
  if os.path.isfile(fileCheck):
    return True
  else:
    return False

# The file passed by parameter is read, the content of each key is encrypted and a 
# file is created with the result.
# It requires that you pass as a parameter the path of the file to encrypt
def encodeBase64(fileToconvert):
  try:
    fopen = open(str(fileToconvert),'r')
  except:
    loggingInst.info('Could not read the file correctly')
    loggingInst.debug('Force stop script')
    exit(2)
  tempStorageEncodedFile = []
  try:
    for line in fopen:
      _tmpSplitLine = line.split()
      loggingInst.debug("Before to convert: " + _tmpSplitLine[0] + " " + _tmpSplitLine[1])
      _message_bytes = _tmpSplitLine[1].encode('ascii')
      base64_bytes = base64.b64encode(_message_bytes)
      base64_message = base64_bytes.decode('ascii')
      loggingInst.debug("After to convert: " + str(base64_message))
      tempStorageEncodedFile.append (_tmpSplitLine[0] + " " + base64_message + "\n")
    fopen.close()
  except Exception as err:
    loggingInst.info("Could not read the file correctly")
    loggingInst.debug(err)
    return False
  try:
    targetFile=str(fileToconvert) + ".base64"
    loggingInst.debug("File name to write: " + str(targetFile))
    with open(targetFile, 'w') as writer:
      for line in tempStorageEncodedFile:
        writer.write(line)
    loggingInst.info('Data saved into: ' + targetFile)
  except Exception as err:
    loggingInst.info("Could not write the file correctly")
    loggingInst.debug(err)
    return False
  return True

# The file passed by parameter is read, the content of each key is decrypted and a 
# file is created with the result.
# It requires that you pass as a parameter the path of the file to decrypted
def decodeBase64(fileToconvert):
  try:
    fopen = open(str(fileToconvert),'r')
  except:
    loggingInst.info('Could not read the file correctly')
    loggingInst.debug('Force stop script')
    exit(3)
  _tempStorageEncodedFile = []
  try:
    for line in fopen:
      _tmpSplitLine = line.split()
      loggingInst.debug("Before to convert: " + _tmpSplitLine[0] + " " + _tmpSplitLine[1])
      _message_bytes = _tmpSplitLine[1].encode('ascii')
      base64_bytes = base64.b64decode(_message_bytes)
      base64_message = base64_bytes.decode('ascii')
      loggingInst.debug("After to convert: " + str(base64_message))
      _tempStorageEncodedFile.append (_tmpSplitLine[0] + " " + base64_message + "\n")
    fopen.close()
  except Exception as err:
    loggingInst.info("Could not read the file correctly")
    loggingInst.debug(err)
    return False
  try:
    targetFile=str(fileToconvert) + ".txt"
    loggingInst.debug("File name to write: " + str(targetFile))
    with open(targetFile, 'w') as writer:
      for line in _tempStorageEncodedFile:
        writer.write(line)
    loggingInst.info('Data saved into: ' + targetFile)
  except Exception as err:
    loggingInst.info("Could not write the file correctly")
    loggingInst.debug(err)
    return False
  return True
