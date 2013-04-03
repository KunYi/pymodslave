#-------------------------------------------------------------------------------
# Name:        ModSlaveSettingsTCP
# Purpose:
#
# Author:      ElBar
#
# Created:     17/04/2012
# Copyright:   (c) ElBar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PyQt4 import QtGui,QtCore
from Ui_settingsModbusTCP import Ui_SettingsModbusTCP

import Utils
#add logging capability
import logging
logger = logging.getLogger("modbus_tk")

#-------------------------------------------------------------------------------
class ModSlaveSettingsTCPWindow(QtGui.QDialog):
    """ Class wrapper for TCP settings ui """

    def __init__(self):
        super(ModSlaveSettingsTCPWindow,self).__init__()
        #init value
        self.tcp_port = 502
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_SettingsModbusTCP()
        self.ui.setupUi(self)
        #set init values
        self._set_values()
        #signals-slots
        self.accepted.connect(self._OK_pressed)
        self.rejected.connect(self._cancel_pressed)

    def _set_values(self):
        """set param values to ui"""
        logger.info("Set param values to UI")
        self.ui.leTCPPort.setText(str(self.tcp_port))

    def _get_values(self):
        """get param values from ui"""
        logger.info("Get param values from UI")
        self.tcp_port = int(self.ui.leTCPPort.text())

    def _OK_pressed(self):
        """new values are accepted"""
        port = str(self.ui.leTCPPort.text())
        if (port.isdigit() and int(port) > 0 and int(port) < 65535):#port must be an integer
            self._get_values()
        else:
            self.tcp_port = 502
            self._set_values()
            self._get_values()
            logger.error("Port must be an integer between 1 and 65535")
            Utils.errorMessageBox("Port must be an integer between 1 an 65535")

    def _cancel_pressed(self):
        """new values are rejected"""
        self._set_values()

    def showEvent(self,QShowEvent):
        """set values for controls"""
        self._set_values()

#-------------------------------------------------------------------------------