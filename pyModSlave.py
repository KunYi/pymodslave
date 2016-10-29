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
import os
import subprocess
import webbrowser
from PyQt4 import QtGui,QtCore
import logging # add logging capability
import ConfigParser # config file parser

from Ui_mainwindow import Ui_MainWindow
from ModSlaveAbout import ModSlaveAboutWindow
from ModSlaveSettingsRTU import ModSlaveSettingsRTUWindow
from ModSlaveSettingsTCP import ModSlaveSettingsTCPWindow
from ModSlaveSettings import ModSlaveSettingsWindow
from ModSlaveMBData import ModSlaveMBData
from ModSlaveMBDataModel import ModSlaveMBDataModel
from ModSlaveBusMonitor import ModSlaveBusMonitorWindow
from ModSlaveMBDataItemDelegate import ModSlaveMBDataItemDelegate

#modbus toolkit
import modbus_tk
import ModSlaveSim as simSlave
from modbus_tk.hooks import install_hook
import Utils

#Hooks
SLAVE_HOOKS = ("modbus.Slave.on_exception")

#-------------------------------------------------------------------------------
class ModSlaveMainWindow(QtGui.QMainWindow):
    """ Class wrapper for main window ui """

    def __init__(self):
        super(ModSlaveMainWindow,self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #init
        self.svr = None # Server
        self._svr_args = []
        self.slv = None # Slave
        #data models
        self.coils = None
        self.dis_inputs = None
        self.input_regs = None
        self.hold_regs = None
        #no of signals
        self._no_coils = 10
        self._no_inputs = 10
        self._no_input_regs = 10
        self._no_hold_regs = 10
        self._time_interval = 2000 # interval for simulation in msec
        self._params_file_name = 'pyModSlave.ini'
        self._logger = logging.getLogger("modbus_tk")
        self._setupUI()

    def _setupUI(self):
        #create window from ui
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #disable Sim for Coils, Holding Regs
        self.ui.chkSimCoils.setVisible(False)
        self.ui.chkSimHoldRegs.setVisible(False)
        #setup toolbar
        self.ui.mainToolBar.addAction(self.ui.actionSerial_RTU)
        self.ui.mainToolBar.addAction(self.ui.actionTCP)
        self.ui.mainToolBar.addAction(self.ui.actionSettings)
        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.actionLog)
        self.ui.mainToolBar.addAction(self.ui.actionBus_Monitor)
        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.actionReset_Counters)
        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.actionModbus_Manual)
        self.ui.mainToolBar.addAction(self.ui.actionAbout)
        self.ui.mainToolBar.addAction(self.ui.actionExit)
        #setup status bar
        pm = QtGui.QPixmap()
        self.status_ind = QtGui.QLabel(self.ui.centralWidget)
        self.status_ind.setFixedSize(16,16)
        self.status_ind.setPixmap(QtGui.QPixmap(':/img/bullet-red-16.png'))
        self.status_text = QtGui.QLabel(self.ui.centralWidget)
        self.status_packet_text = QtGui.QLabel(self.ui.centralWidget)
        self.status_packet_text.setStyleSheet("QLabel {color:blue;}")
        self.status_error_text = QtGui.QLabel(self.ui.centralWidget)
        self.status_error_text.setStyleSheet("QLabel {color:red;}")
        self.ui.statusBar.addWidget(self.status_ind)
        self.ui.statusBar.addWidget(self.status_text, 14)
        self.ui.statusBar.addWidget(self.status_packet_text, 14)
        self.ui.statusBar.addWidget(self.status_error_text, 14)
        #setup ui dialogs
        self._about_dlg = ModSlaveAboutWindow()
        self._settingsRTU_dlg = ModSlaveSettingsRTUWindow()
        self._settingsTCP_dlg = ModSlaveSettingsTCPWindow()
        self._settings_dlg = ModSlaveSettingsWindow()
        self._bus_monitor_dlg = ModSlaveBusMonitorWindow(self)
        #signals-slots
        self.ui.actionAbout.triggered.connect(self._about_dlg.show)
        self.ui.actionSerial_RTU.triggered.connect(self._settings_RTU_show)
        self.ui.actionTCP.triggered.connect(self._settings_TCP_show)
        self.ui.actionSettings.triggered.connect(self._settings_show)
        self.ui.actionBus_Monitor.triggered.connect(self._bus_monitor_show)
        self.ui.actionReset_Counters.triggered.connect(self._reset_counters)
        self.ui.actionLog.triggered.connect(self._open_log_file)
        self.ui.actionModbus_Manual.triggered.connect(self._open_modbus_manual)
        self.ui.btStartStop.clicked.connect(self._start_stop)
        self.ui.cmbModbusMode.currentIndexChanged.connect(self._update_status_bar)
        self.ui.spInterval.valueChanged.connect(self._spInterval_value_changed)
        self.connect(self._bus_monitor_dlg, QtCore.SIGNAL("update_counters"), self._update_counters)
        self.ui.cmbModbusMode.currentIndexChanged.connect(self._update_modbus_mode)
        self.ui.chkSimCoils.stateChanged.connect(self._sim_coils_changed)
        self.ui.chkSimDisInputs.stateChanged.connect(self._sim_dis_inputs_changed)
        self.ui.chkSimInputRegs.stateChanged.connect(self._sim_input_regs_changed)
        self.ui.chkSimHoldRegs.stateChanged.connect(self._sim_hold_regs_changed)
        self.ui.cmbInputRegsType.currentIndexChanged.connect(self._input_regs_data_type_changed)
        self.ui.cmbHoldRegsType.currentIndexChanged.connect(self._hold_regs_data_type_changed)
        self.ui.pbResetDO.clicked.connect(self._reset_DO)
        self.ui.pbResetDI.clicked.connect(self._reset_DI)
        self.ui.pbResetAO.clicked.connect(self._reset_AO)
        self.ui.pbResetAI.clicked.connect(self._reset_AI)
        #read only table views
        self.ui.tvCoilsData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.tvDiscreteInputsData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.tvHoldingRegistersData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.tvInputRegistersData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #item delegates
        self.ui.tvCoilsData.setItemDelegate(ModSlaveMBDataItemDelegate(True))
        self.ui.tvDiscreteInputsData.setItemDelegate(ModSlaveMBDataItemDelegate(True))
        self.ui.tvHoldingRegistersData.setItemDelegate(ModSlaveMBDataItemDelegate(False))
        self.ui.tvInputRegistersData.setItemDelegate(ModSlaveMBDataItemDelegate(False))
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
        self._bus_monitor_dlg.set_max_no_of_bus_monitor_lines(self._settings_dlg.max_no_of_bus_monitor_lines)
        self._update_status_bar()

    def _mbdata_show(self):
        """coils data dialog"""
        self._mbdata_dlg.show()

    def _bus_monitor_show(self):
        """coils data dialog"""
        self._bus_monitor_dlg.svr = self.svr
        self._bus_monitor_dlg.move(self.x() + self.width() + 20, self.y())
        self._bus_monitor_dlg.show()

    def _spInterval_value_changed(self,value):
        """sim interval value changed"""
        self._time_interval = value

    def _update_status_bar(self):
        """update status bar"""
        if (self.ui.cmbModbusMode.currentText() == "TCP"):#TCP server
            msg = "TCP : {0}:{1}".format(self._settingsTCP_dlg.tcp_ip,
                                        self._settingsTCP_dlg.tcp_port)
        elif (self.ui.cmbModbusMode.currentText() == "RTU"):#RTU server
            msg = "RTU : {0}, {1}, {2}, {3}, {4}".format(self._settingsRTU_dlg.rtu_port,
                                                    self._settingsRTU_dlg.baud_rate,
                                                    self._settingsRTU_dlg.byte_size,
                                                    self._settingsRTU_dlg.stop_bits,
                                                    self._settingsRTU_dlg.parity)
        self.status_text.setText(msg)
        if (self.svr is not None):#server is running
            self.status_ind.setPixmap(QtGui.QPixmap(':/img/bullet-green-16.png'))
        else:#server is stopped
            self.status_ind.setPixmap(QtGui.QPixmap(':/img/bullet-red-16.png'))
        self._update_counters()

    def _update_counters(self):
        """update packets - errors counters"""
        self.status_packet_text.setText('Packets : %d' % self._bus_monitor_dlg.packets)
        self.status_error_text.setText('Erros : %d' % self._bus_monitor_dlg.errors)

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
            self.ui.sbNoOfCoils.setEnabled(False)
            self.ui.sbCoilsStartAddr.setEnabled(False)
            self.ui.sbNoOfDigInputs.setEnabled(False)
            self.ui.sbDigInputsstartAddr.setEnabled(False)
            self.ui.sbNoOfHoldingRegs.setEnabled(False)
            self.ui.sbHoldingRegsStartAddr.setEnabled(False)
            self.ui.sbNoOfInputRegs.setEnabled(False)
            self.ui.sbInputRegsStartAddr.setEnabled(False)
        else:#stop
            self.ui.btStartStop.setText("Start")
            self.ui.cmbModbusMode.setEnabled(True)
            self.ui.sbSlaveID.setEnabled(True)
            self.ui.spInterval.setEnabled(True)
            self.ui.actionSerial_RTU.setEnabled(True)
            self.ui.actionTCP.setEnabled(True)
            self.ui.actionSettings.setEnabled(True)
            self.ui.sbNoOfCoils.setEnabled(True)
            self.ui.sbCoilsStartAddr.setEnabled(True)
            self.ui.sbNoOfDigInputs.setEnabled(True)
            self.ui.sbDigInputsstartAddr.setEnabled(True)
            self.ui.sbNoOfHoldingRegs.setEnabled(True)
            self.ui.sbHoldingRegsStartAddr.setEnabled(True)
            self.ui.sbNoOfInputRegs.setEnabled(True)
            self.ui.sbInputRegsStartAddr.setEnabled(True)
            _empty_model = self.coils_data_model = ModSlaveMBDataModel(0, 0, 0)
            self.set_data_models(_empty_model,_empty_model,_empty_model,_empty_model)

    def _start_stop(self):
        """start - stop server and slave"""
        self._reset_counters()
        del self._svr_args[:]#clear params
        svr_hooks = []
        if (self.ui.btStartStop.isChecked()):#start
            if (self.ui.cmbModbusMode.currentText() == "TCP"): # TCP server params
                self._logger.info("Starting TCP server")
                self._svr_args.append("-tcp")
                self._svr_args.append(self._settingsTCP_dlg.tcp_port)
                self._svr_args.append(self._settingsTCP_dlg.tcp_ip)
            elif (self.ui.cmbModbusMode.currentText() == "RTU"): # RTU server params
                self._logger.info("Starting RTU server")
                self._svr_args.append("-rtu")
                self._svr_args.append(self._settingsRTU_dlg.rtu_port - 1) # zero based index
                self._svr_args.append(self._settingsRTU_dlg.baud_rate)
                self._svr_args.append(self._settingsRTU_dlg.byte_size)
                self._svr_args.append(self._settingsRTU_dlg.parity[0])
                self._svr_args.append(self._settingsRTU_dlg.stop_bits)
            if (len(self._svr_args) > 0): # check for valid no of parameters
                self.svr = simSlave.ModServerFactory(self._svr_args)
                if (self.svr is None):#fail to build server
                    self._logger.error("Fail to start server")
                    Utils.errorMessageBox("Fail to start server")
                    self.ui.btStartStop.setChecked(False)
                else:
                    self.svr.start()
                    self.slv = simSlave.ModSlaveSim(self.svr,self.ui.sbSlaveID.value(),
                                                self.ui.spInterval.value()/1000.0,
                                                self.ui.sbCoilsStartAddr.value(), self.ui.sbNoOfCoils.value(),
                                                self.ui.sbDigInputsstartAddr.value(), self.ui.sbNoOfDigInputs.value(),
                                                self.ui.sbInputRegsStartAddr.value(), self.ui.sbNoOfInputRegs.value(),
                                                self.ui.sbHoldingRegsStartAddr.value(), self.ui.sbNoOfHoldingRegs.value())
                    if (self.slv is None):#fail to build slave
                        self._logger.error("Fail to start slave")
                        Utils.errorMessageBox("Fail to start slave")
                        self.svr.stop()
                        self.svr = None
                        self.ui.btStartStop.setChecked(False)
                    else:
                        self.set_data_models(self.slv.coils_data_model,
                                                         self.slv.dis_inputs_data_model,
                                                         self.slv.input_regs_data_model,
                                                         self.slv.hold_regs_data_model)
                        self.slv.start()
        else:#stop
            self._logger.info("Stop server")
            self.slv.stop()
            self.svr.stop()
            self.slv = None
            self.svr = None
        #update user interface
        self._update_ui()
        self._update_status_bar()

    def _load_params(self):
        self._logger.info("Load params")
        config_tcp_defaut = {'TCP_Port':'502', 'TCP_IP':'127.000.000.001'}
        config_rtu_defaut = {'RTU_Port':'0', 'Baud':'9600', 'DataBits':'8', 'StopBits':'1', 'Parity':'None'}
        config_var_defaut = {'Coils':'10', 'DisInputs':'10', 'InputRegs':'10', 'HoldRegs':'10', 'TimeInterval':'1000', 'MaxNoOfBusMonitorLines':'50'}
        config_default = {}
        config_default.update(config_tcp_defaut)
        config_default.update(config_rtu_defaut)
        config_default.update(config_var_defaut)
        config = ConfigParser.RawConfigParser(config_default)
        if not(config.read(self._params_file_name)):#if file does not exist exit
            self._logger.error("Parameters file does not exist")
            return
        #TCP Settings
        self._settingsTCP_dlg.tcp_port = config.getint('TCP', 'TCP_Port')
        self._settingsTCP_dlg.tcp_ip = config.get('TCP', 'TCP_IP')
        #RTU Settings
        self._settingsRTU_dlg.rtu_port = config.getint('RTU', 'RTU_Port')
        self._settingsRTU_dlg.baud_rate = config.getint('RTU', 'Baud')
        self._settingsRTU_dlg.byte_size = config.getint('RTU', 'DataBits')
        self._settingsRTU_dlg.stop_bits = config.get('RTU', 'StopBits')
        self._settingsRTU_dlg.parity = config.get('RTU', 'Parity')
        #Var Settings
        self._no_coils = config.getint('Var', 'Coils')
        self._no_inputs = config.getint('Var', 'DisInputs')
        self._no_input_regs = config.getint('Var', 'InputRegs')
        self._no_hold_regs = config.getint('Var', 'HoldRegs')
        self._time_interval = config.getint('Var', 'TimeInterval')
        self._settings_dlg.max_no_of_bus_monitor_lines = config.getint('Var', 'MaxNoOfBusMonitorLines')
        self._bus_monitor_dlg.set_max_no_of_bus_monitor_lines(self._settings_dlg.max_no_of_bus_monitor_lines)

    def _save_params(self):
        self._logger.info("Save params")
        config = ConfigParser.RawConfigParser()
        #TCP Settings
        config.add_section('TCP')
        config.set('TCP','TCP_Port',self._settingsTCP_dlg.tcp_port)
        config.set('TCP','TCP_IP',self._settingsTCP_dlg.tcp_ip)
        #RTU Settings
        config.add_section('RTU')
        config.set('RTU','RTU_Port',self._settingsRTU_dlg.rtu_port)
        config.set('RTU','Baud',self._settingsRTU_dlg.baud_rate)
        config.set('RTU','DataBits',self._settingsRTU_dlg.byte_size)
        config.set('RTU','StopBits',self._settingsRTU_dlg.stop_bits)
        config.set('RTU','Parity',self._settingsRTU_dlg.parity)
        #Var Settings
        config.add_section('Var')
        config.set('Var','Coils',self._no_coils)
        config.set('Var','DisInputs',self._no_inputs)
        config.set('Var','InputRegs',self._no_input_regs)
        config.set('Var','HoldRegs',self._no_hold_regs)
        config.set('Var','TimeInterval',self._time_interval)
        config.set('Var','MaxNoOfBusMonitorLines',self._settings_dlg.max_no_of_bus_monitor_lines)
        #Save Settings
        config_file = open(self._params_file_name, 'wb')
        config.write(config_file)

    def _reset_counters(self):
        self._bus_monitor_dlg.reset_counters()

    def _update_modbus_mode(self, index):
        if (index == 0):# RTU
            self.ui.lblSlave.setText('Slave Addr')
            #self.ui.sbSlaveID.setVisible(True)
        elif (index == 1):# TCP
            self.ui.lblSlave.setText('Unit ID')
            #self.ui.sbSlaveID.setVisible(False)

    def _open_log_file(self):
        """open application log"""
        if (not os.path.exists('pyModSlave.log')):
            msg = "File 'pyModSlave.log' does not exist"
            self._logger.error(msg)
            Utils.errorMessageBox(msg)
            return
        try:
            subprocess.Popen(['notepad.exe', 'pyModSlave.log'])
        except WindowsError as we:
            msg = "Windows Error No %i - %s" % we.args
            self._logger.error(msg)
            Utils.errorMessageBox(msg)

    def _open_modbus_manual(self):
        """open modbus manual"""
        if (not os.path.exists('ManModbus\index.html')):
            msg = "Modbus Manual is missing"
            self._logger.error(msg)
            Utils.errorMessageBox(msg)
            return
        try:
            webbrowser.open_new_tab('ManModbus\index.html')
        except WindowsError as we:
            msg = "Cannot open Modbus Manual %i - %s" % we.args
            self._logger.error(msg)
            Utils.errorMessageBox(msg)

    def showEvent(self,QShowEvent):
        """set values for controls"""
        self._load_params()
        self.ui.sbNoOfCoils.setValue(self._no_coils)
        self.ui.sbNoOfDigInputs.setValue(self._no_inputs)
        self.ui.sbNoOfHoldingRegs.setValue(self._no_hold_regs)
        self.ui.sbNoOfInputRegs.setValue(self._no_input_regs)
        self.ui.spInterval.setValue(self._time_interval)
        self._update_status_bar()

    def closeEvent(self,QCloseEvent):
        """window is closing"""
        self._no_coils = self.ui.sbNoOfCoils.value()
        self._no_inputs = self.ui.sbNoOfDigInputs.value()
        self._no_hold_regs = self.ui.sbNoOfHoldingRegs.value()
        self._no_input_regs = self.ui.sbNoOfInputRegs.value()
        self._save_params()

    def set_data_models(self, coils, dis_inputs, input_regs, hold_regs):
        self.coils = coils
        self.dis_inputs = dis_inputs
        self.input_regs = input_regs
        self.hold_regs = hold_regs
        #table views models
        #coils
        self.ui.tvCoilsData.setModel(self.coils.model)
        self.connect(self.coils, QtCore.SIGNAL("update_view"), self._models_data_changed)
        self.connect(self.ui.tvCoilsData.itemDelegate(), QtCore.SIGNAL("update_data"), self.coils.update_item)
        self._sim_coils_changed()
        #discrete inputs
        self.ui.tvDiscreteInputsData.setModel(self.dis_inputs.model)
        self.connect(self.dis_inputs, QtCore.SIGNAL("update_view"), self._models_data_changed)
        self.connect(self.ui.tvDiscreteInputsData.itemDelegate(), QtCore.SIGNAL("update_data"), self.dis_inputs.update_item)
        self._sim_dis_inputs_changed()
        #input regs
        self.ui.tvInputRegistersData.setModel(self.input_regs.model)
        self.connect(self.input_regs, QtCore.SIGNAL("update_view"), self._models_data_changed)
        self.input_regs.set_data_type(self.ui.cmbInputRegsType.currentIndex())
        self.connect(self.ui.tvInputRegistersData.itemDelegate(), QtCore.SIGNAL("update_data"), self.input_regs.update_item)
        self._sim_input_regs_changed()
        #holding regs
        self.ui.tvHoldingRegistersData.setModel(self.hold_regs.model)
        self.connect(self.hold_regs, QtCore.SIGNAL("update_view"), self._models_data_changed)
        self.hold_regs.set_data_type(self.ui.cmbHoldRegsType.currentIndex())
        self.connect(self.ui.tvHoldingRegistersData.itemDelegate(), QtCore.SIGNAL("update_data"), self.hold_regs.update_item)
        self._sim_hold_regs_changed()
        #update table views
        self._models_data_changed()

    def _sim_coils_changed(self):
        self.coils.sim = self.ui.chkSimCoils.isChecked()
        self.ui.pbResetDO.setDisabled(self.coils.sim)
        if (self.coils.sim):
            self.ui.tvCoilsData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        else:
            self.ui.tvCoilsData.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed)

    def _sim_dis_inputs_changed(self):
        self.dis_inputs.sim = self.ui.chkSimDisInputs.isChecked()
        self.ui.pbResetDI.setDisabled(self.dis_inputs.sim)
        if (self.dis_inputs.sim):
            self.ui.tvDiscreteInputsData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        else:
            self.ui.tvDiscreteInputsData.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed)

    def _sim_input_regs_changed(self):
        self.input_regs.sim = self.ui.chkSimInputRegs.isChecked()
        self.ui.pbResetAI.setDisabled(self.input_regs.sim)
        if (self.input_regs.sim):
            self.ui.tvInputRegistersData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        else:
            self.ui.tvInputRegistersData.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed)

    def _sim_hold_regs_changed(self):
        self.hold_regs.sim = self.ui.chkSimHoldRegs.isChecked()
        self.ui.pbResetAO.setDisabled(self.hold_regs.sim)
        if (self.hold_regs.sim):
            self.ui.tvHoldingRegistersData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        else:
            self.ui.tvHoldingRegistersData.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed)

    def _models_data_changed(self):
        self.ui.tvCoilsData.resizeColumnsToContents()
        self.ui.tvDiscreteInputsData.resizeColumnsToContents()
        self.ui.tvInputRegistersData.resizeColumnsToContents()
        self.ui.tvHoldingRegistersData.resizeColumnsToContents()

    def _input_regs_data_type_changed(self):
        if (self.input_regs):
            self.input_regs.set_data_type(self.ui.cmbInputRegsType.currentIndex())
            (self.ui.tvInputRegistersData.itemDelegate()).set_data_type(self.ui.cmbInputRegsType.currentIndex())

    def _hold_regs_data_type_changed(self):
        if (self.hold_regs):
            self.hold_regs.set_data_type(self.ui.cmbHoldRegsType.currentIndex())
            (self.ui.tvHoldingRegistersData.itemDelegate()).set_data_type(self.ui.cmbHoldRegsType.currentIndex())

    def _reset_DO(self):
        self._logger.info("Reset DO")
        self.coils.reset_data()

    def _reset_DI(self):
        self._logger.info("Reset DI")
        self.dis_inputs.reset_data()

    def _reset_AO(self):
        self._logger.info("Reset AO")
        self.hold_regs.reset_data()

    def _reset_AI(self):
        self._logger.info("Reset AI")
        self.input_regs.reset_data()
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def main():

    #logger
    logger = modbus_tk.utils.create_logger("console")
    Utils.set_up_logger_file(logger,'pyModSlave.log')
    #create qt application
    app = QtGui.QApplication(sys.argv)
    #load main window
    window=ModSlaveMainWindow()
    #application loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------