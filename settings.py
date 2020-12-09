#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import librarys
from lib.class_ArgumentParser import *
from lib.class_logging import *
from lib.general_function import *

# Get Script home path
scriptPath = os.path.dirname(os.path.realpath(__file__))

# Load configuration logs
if ArgumentParserInst.getArgsVerbose():
  logLevel = 'DEBUG'
else:
  logLevel = 'INFO'
loggingInst = LogginConfig(scriptPath, logLevel)
loggingInst.info("------------------------",True)
loggingInst.info("Script Start",True)    

# Load Argument Parser
ArgumentParserInst = LoadArgumentParser()

# Validates that the name of the file to use is passed as a parameter
if ArgumentParserInst.getArgsFileName() == False:
  loggingInst.info('Not indicated a file to use. Close')
  loggingInst.debug('Forced stop script')
  exit(5)

### Print Variables for debug:
loggingInst.debug("Logging level from config file: " + logLevel)
loggingInst.debug("Path from script location: " + scriptPath)
loggingInst.debug("Logging file: " + scriptPath + '/code-encode.log')
loggingInst.debug("File Recibed by parameter: " + ArgumentParserInst.getArgsFileName())
loggingInst.debug("Encode file: " + str(ArgumentParserInst.getArgsEncode()))
loggingInst.debug("Decode file: " + str(ArgumentParserInst.getArgsDecode()))