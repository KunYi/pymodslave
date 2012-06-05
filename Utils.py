#-------------------------------------------------------------------------------
# Name:        Utils
# Purpose:
#
# Author:      Elbar
#
# Created:     01/03/2012
# Copyright:   (c) USER 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#Qt
from PyQt4 import QtGui
#add logging capability
import logging

def errorMessageBox(msg):

    QtGui.QMessageBox.critical(None,"Error",msg,QtGui.QMessageBox.Ok,QtGui.QMessageBox.NoButton)

def set_up_logger(logger,file_name):

    fh = logging.FileHandler(file_name)
    frm = logging.Formatter("%(asctime)s\t%(levelname)s\t%(module)s.%(funcName)s\t%(threadName)s\t%(message)s")
    fh.setFormatter(frm)
    logger.addHandler(fh)
