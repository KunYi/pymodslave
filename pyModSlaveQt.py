#-------------------------------------------------------------------------------
# Name:        pyModSlaveQt
# Purpose:
#
# Author:      ElBar
#
# Created:     29/02/2012
# Copyright:   (c) ElBar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
from PyQt4 import QtGui,QtCore
#add logging capability
import logging

from Ui_mainwindow import Ui_MainWindow
from ModSlaveAbout import ModSlaveAboutWindow
from ModSlaveSettingsRTU import ModSlaveSettingsRTUWindow
from ModSlaveSettingsTCP import ModSlaveSettingsTCPWindow
from ModSlaveSettings import ModSlaveSettingsWindow
#modbus toolkit
import modbus_tk
import ModSlaveSim as simSlave
import Utils
#logger
logger = modbus_tk.utils.create_logger("dummy")

#-------------------------------------------------------------------------------
class ModSlaveMainWindow(QtGui.QMainWindow):
    """ Class wrapper for main window ui """

    def __init__(self):
        super(ModSlaveMainWindow,self).__init__()
        #init
        self.svr = None#Server
        self._svr_args = []
        self.slv = None#Slave
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #setup toolbar
        self.ui.mainToolBar.addAction(self.ui.actionSerial_RTU)
        self.ui.mainToolBar.addAction(self.ui.actionTCP)
        self.ui.mainToolBar.addAction(self.ui.actionSettings)
        self.ui.mainToolBar.addAction(self.ui.actionAbout)
        self.ui.mainToolBar.addAction(self.ui.actionExit)
        #setup status bar
        self.status_ind = QtGui.QWidget(self.ui.centralWidget)
        self.status_ind.setFixedSize(16, 16)
        self.status_text = QtGui.QLabel(self.ui.centralWidget)
        self.ui.statusBar.addWidget(self.status_ind)
        self.ui.statusBar.addWidget(self.status_text, 14)
        #setup dialogs
        self._about_dlg = ModSlaveAboutWindow()
        self._settingsRTU_dlg = ModSlaveSettingsRTUWindow()
        self._settingsTCP_dlg = ModSlaveSettingsTCPWindow()
        self._settings_dlg = ModSlaveSettingsWindow()
        #signals-slots
        self.ui.actionAbout.triggered.connect(self._about_dlg.show)
        self.ui.actionSerial_RTU.triggered.connect(self._settings_RTU_show)
        self.ui.actionTCP.triggered.connect(self._settings_TCP_show)
        self.ui.actionSettings.triggered.connect(self._settings_show)
        self.ui.btStartStop.clicked.connect(self._start_stop)
        self.ui.cmbModbusMode.currentIndexChanged.connect(self._update_status_bar)
        #show window
        self._update_status_bar()
        self.show()

    def _settings_RTU_show(self):
        """open RTU settings dialog"""
        self._settingsRTU_dlg.exec_()
        self._update_status_bar()

    def _settings_TCP_show(self):
        """open TCP settings dialog"""
        self._settingsTCP_dlg.exec_()
        self._update_status_bar()

    def _settings_show(self):
        """open general settings dialog"""
        self._settings_dlg.exec_()
        self._update_status_bar()

    def _update_status_bar(self):
        """update status bar"""
        if (self.ui.cmbModbusMode.currentText() == "TCP"):#TCP server
            msg = "TCP : {0}".format(self._settingsTCP_dlg.tcp_port)
        elif (self.ui.cmbModbusMode.currentText() == "RTU"):#RTU server
            msg = "RTU : {0}, {1}, {2}, {3}, {4}".format(self._settingsRTU_dlg.rtu_port,
                                                    self._settingsRTU_dlg.baud_rate,
                                                    self._settingsRTU_dlg.byte_size,
                                                    self._settingsRTU_dlg.stop_bits,
                                                    self._settingsRTU_dlg.parity)
        self.status_text.setText(msg)
        if (self.svr != None):#server is running
            self.status_ind.setStyleSheet("background-color: green")
        else:#server is stopped
            self.status_ind.setStyleSheet("background-color: red")

    def _update_ui(self):
        """update enable-disable status of ui components"""
        if (self.ui.btStartStop.isChecked()):#start
            self.ui.btStartStop.setText("Stop")
            self.ui.cmbModbusMode.setEnabled(False)
            self.ui.sbSlaveID.setEnabled(False)
            self.ui.spInterval.setEnabled(False)
            self.ui.actionSerial_RTU.setEnabled(False)
            self.ui.actionTCP.setEnabled(False)
            self.ui.actionSettings.setEnabled(False)
        else:#stop
            self.ui.btStartStop.setText("Start")
            self.ui.cmbModbusMode.setEnabled(True)
            self.ui.sbSlaveID.setEnabled(True)
            self.ui.spInterval.setEnabled(True)
            self.ui.actionSerial_RTU.setEnabled(True)
            self.ui.actionTCP.setEnabled(True)
            self.ui.actionSettings.setEnabled(True)

    def _start_stop(self):
        """start - stop server and slave"""
        del self._svr_args[:]#clear params
        if (self.ui.btStartStop.isChecked()):#start
            if (self.ui.cmbModbusMode.currentText() == "TCP"):#TCP server params
                logger.info("Starting TCP server")
                self._svr_args.append("-tcp")
                self._svr_args.append(self._settingsTCP_dlg.tcp_port)
            elif (self.ui.cmbModbusMode.currentText() == "RTU"):#RTU server params
                logger.info("Starting RTU server")
                self._svr_args.append("-rtu")
                self._svr_args.append(self._settingsRTU_dlg.rtu_port)
                self._svr_args.append(self._settingsRTU_dlg.baud_rate)
                self._svr_args.append(self._settingsRTU_dlg.byte_size)
                self._svr_args.append(self._settingsRTU_dlg.parity[0])
                self._svr_args.append(self._settingsRTU_dlg.stop_bits)
            if (len(self._svr_args) > 0):#check for valid no of parameters
                self.svr = simSlave.ModServerFactory(self._svr_args)
                if (self.svr == None):#fail to build server
                    logger.error("Fail to start server")
                    Utils.errorMessageBox("Fail to start server")
                    self.ui.btStartStop.setChecked(False)
                else:
                    self.svr.start()
                    self.slv = simSlave.ModSlaveSim(self.svr,self.ui.sbSlaveID.value(),
                                                self.ui.spInterval.value()/1000.0,
                                                self._settings_dlg.coils,
                                                self._settings_dlg.inputs,
                                                self._settings_dlg.input_regs,
                                                self._settings_dlg.hold_regs)
                    if (self.slv == None):#fail to build slave
                        logger.error("Fail to start slave")
                        Utils.errorMessageBox("Fail to start slave")
                        self.svr.stop()
                        self.svr = None
                        self.ui.btStartStop.setChecked(False)
                    else:
                        self.slv.start()
        else:#stop
            logger.info("Stop server")
            self.slv.stop()
            self.svr.stop()
            self.slv = None
            self.svr = None
        #update user interface
        self._update_ui()
        self._update_status_bar()
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def main():

    #set-up logger
    Utils.set_up_logger(logger,'pyModSlaveQt.log')
    #create qt application
    app=QtGui.QApplication(sys.argv)
    #load main window
    window=ModSlaveMainWindow()
    #application loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------