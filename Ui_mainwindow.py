# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\python\pyModSlave\ui\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 498))
        MainWindow.setMaximumSize(QtCore.QSize(500, 640))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/Bus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.vericallayout = QtGui.QVBoxLayout(self.centralWidget)
        self.vericallayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.vericallayout.setContentsMargins(9, 9, 11, 11)
        self.vericallayout.setSpacing(9)
        self.vericallayout.setObjectName(_fromUtf8("vericallayout"))
        self.frame_commands = QtGui.QFrame(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_commands.sizePolicy().hasHeightForWidth())
        self.frame_commands.setSizePolicy(sizePolicy)
        self.frame_commands.setMinimumSize(QtCore.QSize(482, 40))
        self.frame_commands.setMaximumSize(QtCore.QSize(482, 40))
        self.frame_commands.setFrameShape(QtGui.QFrame.Box)
        self.frame_commands.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_commands.setObjectName(_fromUtf8("frame_commands"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_commands)
        self.horizontalLayout_5.setContentsMargins(11, 6, 11, 6)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lblModbusMode = QtGui.QLabel(self.frame_commands)
        self.lblModbusMode.setObjectName(_fromUtf8("lblModbusMode"))
        self.horizontalLayout_5.addWidget(self.lblModbusMode)
        self.cmbModbusMode = QtGui.QComboBox(self.frame_commands)
        self.cmbModbusMode.setMinimumSize(QtCore.QSize(0, 24))
        self.cmbModbusMode.setObjectName(_fromUtf8("cmbModbusMode"))
        self.cmbModbusMode.addItem(_fromUtf8(""))
        self.cmbModbusMode.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.cmbModbusMode)
        self.lblSlave = QtGui.QLabel(self.frame_commands)
        self.lblSlave.setObjectName(_fromUtf8("lblSlave"))
        self.horizontalLayout_5.addWidget(self.lblSlave)
        self.sbSlaveID = QtGui.QSpinBox(self.frame_commands)
        self.sbSlaveID.setMinimumSize(QtCore.QSize(0, 24))
        self.sbSlaveID.setMinimum(1)
        self.sbSlaveID.setMaximum(247)
        self.sbSlaveID.setObjectName(_fromUtf8("sbSlaveID"))
        self.horizontalLayout_5.addWidget(self.sbSlaveID)
        self.lblSimCycle = QtGui.QLabel(self.frame_commands)
        self.lblSimCycle.setObjectName(_fromUtf8("lblSimCycle"))
        self.horizontalLayout_5.addWidget(self.lblSimCycle)
        self.spInterval = QtGui.QSpinBox(self.frame_commands)
        self.spInterval.setMinimumSize(QtCore.QSize(0, 24))
        self.spInterval.setMinimum(1000)
        self.spInterval.setMaximum(10000)
        self.spInterval.setSingleStep(500)
        self.spInterval.setProperty("value", 5000)
        self.spInterval.setObjectName(_fromUtf8("spInterval"))
        self.horizontalLayout_5.addWidget(self.spInterval)
        self.vericallayout.addWidget(self.frame_commands)
        self.tabIOs = QtGui.QTabWidget(self.centralWidget)
        self.tabIOs.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabIOs.sizePolicy().hasHeightForWidth())
        self.tabIOs.setSizePolicy(sizePolicy)
        self.tabIOs.setMinimumSize(QtCore.QSize(0, 0))
        self.tabIOs.setObjectName(_fromUtf8("tabIOs"))
        self.tabCoils = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabCoils.sizePolicy().hasHeightForWidth())
        self.tabCoils.setSizePolicy(sizePolicy)
        self.tabCoils.setObjectName(_fromUtf8("tabCoils"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabCoils)
        self.verticalLayout.setContentsMargins(11, 9, 11, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.tabCoils)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setContentsMargins(11, 6, 11, 6)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pbResetDO = QtGui.QPushButton(self.frame)
        self.pbResetDO.setMinimumSize(QtCore.QSize(48, 0))
        self.pbResetDO.setMaximumSize(QtCore.QSize(48, 16777215))
        self.pbResetDO.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/edit-clear-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbResetDO.setIcon(icon1)
        self.pbResetDO.setObjectName(_fromUtf8("pbResetDO"))
        self.horizontalLayout_6.addWidget(self.pbResetDO)
        self.lblCoilsStartAddr = QtGui.QLabel(self.frame)
        self.lblCoilsStartAddr.setObjectName(_fromUtf8("lblCoilsStartAddr"))
        self.horizontalLayout_6.addWidget(self.lblCoilsStartAddr)
        self.sbCoilsStartAddr = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbCoilsStartAddr.sizePolicy().hasHeightForWidth())
        self.sbCoilsStartAddr.setSizePolicy(sizePolicy)
        self.sbCoilsStartAddr.setMinimumSize(QtCore.QSize(50, 0))
        self.sbCoilsStartAddr.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sbCoilsStartAddr.setMinimum(0)
        self.sbCoilsStartAddr.setMaximum(65535)
        self.sbCoilsStartAddr.setSingleStep(10)
        self.sbCoilsStartAddr.setProperty("value", 0)
        self.sbCoilsStartAddr.setObjectName(_fromUtf8("sbCoilsStartAddr"))
        self.horizontalLayout_6.addWidget(self.sbCoilsStartAddr)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.sbNoOfCoils = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbNoOfCoils.sizePolicy().hasHeightForWidth())
        self.sbNoOfCoils.setSizePolicy(sizePolicy)
        self.sbNoOfCoils.setMinimumSize(QtCore.QSize(50, 0))
        self.sbNoOfCoils.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sbNoOfCoils.setMinimum(1)
        self.sbNoOfCoils.setMaximum(500)
        self.sbNoOfCoils.setSingleStep(10)
        self.sbNoOfCoils.setProperty("value", 50)
        self.sbNoOfCoils.setObjectName(_fromUtf8("sbNoOfCoils"))
        self.horizontalLayout_6.addWidget(self.sbNoOfCoils)
        self.chkSimCoils = QtGui.QCheckBox(self.frame)
        self.chkSimCoils.setObjectName(_fromUtf8("chkSimCoils"))
        self.horizontalLayout_6.addWidget(self.chkSimCoils)
        self.verticalLayout.addWidget(self.frame)
        self.tvCoilsData = QtGui.QTableView(self.tabCoils)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tvCoilsData.sizePolicy().hasHeightForWidth())
        self.tvCoilsData.setSizePolicy(sizePolicy)
        self.tvCoilsData.setMinimumSize(QtCore.QSize(450, 0))
        self.tvCoilsData.setCornerButtonEnabled(False)
        self.tvCoilsData.setObjectName(_fromUtf8("tvCoilsData"))
        self.tvCoilsData.horizontalHeader().setVisible(False)
        self.tvCoilsData.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tvCoilsData)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/DO.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabIOs.addTab(self.tabCoils, icon2, _fromUtf8(""))
        self.tabDiscreteInputs = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabDiscreteInputs.sizePolicy().hasHeightForWidth())
        self.tabDiscreteInputs.setSizePolicy(sizePolicy)
        self.tabDiscreteInputs.setObjectName(_fromUtf8("tabDiscreteInputs"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabDiscreteInputs)
        self.verticalLayout_2.setContentsMargins(11, 9, 11, 9)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_2 = QtGui.QFrame(self.tabDiscreteInputs)
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(11, 6, 11, 6)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbResetDI = QtGui.QPushButton(self.frame_2)
        self.pbResetDI.setMinimumSize(QtCore.QSize(48, 0))
        self.pbResetDI.setMaximumSize(QtCore.QSize(48, 16777215))
        self.pbResetDI.setText(_fromUtf8(""))
        self.pbResetDI.setIcon(icon1)
        self.pbResetDI.setObjectName(_fromUtf8("pbResetDI"))
        self.horizontalLayout.addWidget(self.pbResetDI)
        self.lblDigInputsStartAddr = QtGui.QLabel(self.frame_2)
        self.lblDigInputsStartAddr.setObjectName(_fromUtf8("lblDigInputsStartAddr"))
        self.horizontalLayout.addWidget(self.lblDigInputsStartAddr)
        self.sbDigInputsstartAddr = QtGui.QSpinBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbDigInputsstartAddr.sizePolicy().hasHeightForWidth())
        self.sbDigInputsstartAddr.setSizePolicy(sizePolicy)
        self.sbDigInputsstartAddr.setMinimumSize(QtCore.QSize(50, 0))
        self.sbDigInputsstartAddr.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sbDigInputsstartAddr.setMinimum(0)
        self.sbDigInputsstartAddr.setMaximum(65535)
        self.sbDigInputsstartAddr.setSingleStep(10)
        self.sbDigInputsstartAddr.setProperty("value", 0)
        self.sbDigInputsstartAddr.setObjectName(_fromUtf8("sbDigInputsstartAddr"))
        self.horizontalLayout.addWidget(self.sbDigInputsstartAddr)
        self.lblNoOfDigInputs = QtGui.QLabel(self.frame_2)
        self.lblNoOfDigInputs.setObjectName(_fromUtf8("lblNoOfDigInputs"))
        self.horizontalLayout.addWidget(self.lblNoOfDigInputs)
        self.sbNoOfDigInputs = QtGui.QSpinBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbNoOfDigInputs.sizePolicy().hasHeightForWidth())
        self.sbNoOfDigInputs.setSizePolicy(sizePolicy)
        self.sbNoOfDigInputs.setMinimumSize(QtCore.QSize(50, 0))
        self.sbNoOfDigInputs.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sbNoOfDigInputs.setMinimum(1)
        self.sbNoOfDigInputs.setMaximum(500)
        self.sbNoOfDigInputs.setSingleStep(10)
        self.sbNoOfDigInputs.setProperty("value", 50)
        self.sbNoOfDigInputs.setObjectName(_fromUtf8("sbNoOfDigInputs"))
        self.horizontalLayout.addWidget(self.sbNoOfDigInputs)
        self.chkSimDisInputs = QtGui.QCheckBox(self.frame_2)
        self.chkSimDisInputs.setObjectName(_fromUtf8("chkSimDisInputs"))
        self.horizontalLayout.addWidget(self.chkSimDisInputs)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.tvDiscreteInputsData = QtGui.QTableView(self.tabDiscreteInputs)
        self.tvDiscreteInputsData.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tvDiscreteInputsData.sizePolicy().hasHeightForWidth())
        self.tvDiscreteInputsData.setSizePolicy(sizePolicy)
        self.tvDiscreteInputsData.setMinimumSize(QtCore.QSize(450, 0))
        self.tvDiscreteInputsData.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tvDiscreteInputsData.setCornerButtonEnabled(False)
        self.tvDiscreteInputsData.setObjectName(_fromUtf8("tvDiscreteInputsData"))
        self.tvDiscreteInputsData.horizontalHeader().setVisible(False)
        self.tvDiscreteInputsData.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tvDiscreteInputsData)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/DI.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabIOs.addTab(self.tabDiscreteInputs, icon3, _fromUtf8(""))
        self.tabInputRegisters = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabInputRegisters.sizePolicy().hasHeightForWidth())
        self.tabInputRegisters.setSizePolicy(sizePolicy)
        self.tabInputRegisters.setObjectName(_fromUtf8("tabInputRegisters"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabInputRegisters)
        self.verticalLayout_6.setContentsMargins(11, 9, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.frame_3 = QtGui.QFrame(self.tabInputRegisters)
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(11, 6, 11, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pbResetAI = QtGui.QPushButton(self.frame_3)
        self.pbResetAI.setMinimumSize(QtCore.QSize(48, 0))
        self.pbResetAI.setMaximumSize(QtCore.QSize(48, 16777215))
        self.pbResetAI.setText(_fromUtf8(""))
        self.pbResetAI.setIcon(icon1)
        self.pbResetAI.setObjectName(_fromUtf8("pbResetAI"))
        self.horizontalLayout_2.addWidget(self.pbResetAI)
        self.lblInputRegsStartAddr = QtGui.QLabel(self.frame_3)
        self.lblInputRegsStartAddr.setObjectName(_fromUtf8("lblInputRegsStartAddr"))
        self.horizontalLayout_2.addWidget(self.lblInputRegsStartAddr)
        self.sbInputRegsStartAddr = QtGui.QSpinBox(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbInputRegsStartAddr.sizePolicy().hasHeightForWidth())
        self.sbInputRegsStartAddr.setSizePolicy(sizePolicy)
        self.sbInputRegsStartAddr.setMinimumSize(QtCore.QSize(50, 0))
        self.sbInputRegsStartAddr.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sbInputRegsStartAddr.setMinimum(0)
        self.sbInputRegsStartAddr.setMaximum(65535)
        self.sbInputRegsStartAddr.setSingleStep(10)
        self.sbInputRegsStartAddr.setProperty("value", 0)
        self.sbInputRegsStartAddr.setObjectName(_fromUtf8("sbInputRegsStartAddr"))
        self.horizontalLayout_2.addWidget(self.sbInputRegsStartAddr)
        self.lblNoOfInputRegs = QtGui.QLabel(self.frame_3)
        self.lblNoOfInputRegs.setObjectName(_fromUtf8("lblNoOfInputRegs"))
        self.horizontalLayout_2.addWidget(self.lblNoOfInputRegs)
        self.sbNoOfInputRegs = QtGui.QSpinBox(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbNoOfInputRegs.sizePolicy().hasHeightForWidth())
        self.sbNoOfInputRegs.setSizePolicy(sizePolicy)
        self.sbNoOfInputRegs.setMinimumSize(QtCore.QSize(50, 0))
        self.sbNoOfInputRegs.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sbNoOfInputRegs.setMinimum(1)
        self.sbNoOfInputRegs.setMaximum(500)
        self.sbNoOfInputRegs.setSingleStep(10)
        self.sbNoOfInputRegs.setProperty("value", 50)
        self.sbNoOfInputRegs.setObjectName(_fromUtf8("sbNoOfInputRegs"))
        self.horizontalLayout_2.addWidget(self.sbNoOfInputRegs)
        self.chkSimInputRegs = QtGui.QCheckBox(self.frame_3)
        self.chkSimInputRegs.setObjectName(_fromUtf8("chkSimInputRegs"))
        self.horizontalLayout_2.addWidget(self.chkSimInputRegs)
        self.cmbInputRegsType = QtGui.QComboBox(self.frame_3)
        self.cmbInputRegsType.setMaxVisibleItems(2)
        self.cmbInputRegsType.setObjectName(_fromUtf8("cmbInputRegsType"))
        self.cmbInputRegsType.addItem(_fromUtf8(""))
        self.cmbInputRegsType.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbInputRegsType)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.tvInputRegistersData = QtGui.QTableView(self.tabInputRegisters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tvInputRegistersData.sizePolicy().hasHeightForWidth())
        self.tvInputRegistersData.setSizePolicy(sizePolicy)
        self.tvInputRegistersData.setMinimumSize(QtCore.QSize(450, 0))
        self.tvInputRegistersData.setCornerButtonEnabled(False)
        self.tvInputRegistersData.setObjectName(_fromUtf8("tvInputRegistersData"))
        self.tvInputRegistersData.horizontalHeader().setVisible(False)
        self.tvInputRegistersData.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.tvInputRegistersData)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/AI.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabIOs.addTab(self.tabInputRegisters, icon4, _fromUtf8(""))
        self.tabHoldingRegisters = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabHoldingRegisters.sizePolicy().hasHeightForWidth())
        self.tabHoldingRegisters.setSizePolicy(sizePolicy)
        self.tabHoldingRegisters.setObjectName(_fromUtf8("tabHoldingRegisters"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabHoldingRegisters)
        self.verticalLayout_7.setContentsMargins(11, 9, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.frame_4 = QtGui.QFrame(self.tabHoldingRegisters)
        self.frame_4.setFrameShape(QtGui.QFrame.Box)
        self.frame_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(11, 6, 11, 6)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pbResetAO = QtGui.QPushButton(self.frame_4)
        self.pbResetAO.setMinimumSize(QtCore.QSize(48, 0))
        self.pbResetAO.setMaximumSize(QtCore.QSize(48, 16777215))
        self.pbResetAO.setText(_fromUtf8(""))
        self.pbResetAO.setIcon(icon1)
        self.pbResetAO.setObjectName(_fromUtf8("pbResetAO"))
        self.horizontalLayout_4.addWidget(self.pbResetAO)
        self.lblHoldRegsStarAddr = QtGui.QLabel(self.frame_4)
        self.lblHoldRegsStarAddr.setObjectName(_fromUtf8("lblHoldRegsStarAddr"))
        self.horizontalLayout_4.addWidget(self.lblHoldRegsStarAddr)
        self.sbHoldingRegsStartAddr = QtGui.QSpinBox(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbHoldingRegsStartAddr.sizePolicy().hasHeightForWidth())
        self.sbHoldingRegsStartAddr.setSizePolicy(sizePolicy)
        self.sbHoldingRegsStartAddr.setMinimumSize(QtCore.QSize(50, 0))
        self.sbHoldingRegsStartAddr.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sbHoldingRegsStartAddr.setMinimum(0)
        self.sbHoldingRegsStartAddr.setMaximum(65535)
        self.sbHoldingRegsStartAddr.setSingleStep(10)
        self.sbHoldingRegsStartAddr.setProperty("value", 0)
        self.sbHoldingRegsStartAddr.setObjectName(_fromUtf8("sbHoldingRegsStartAddr"))
        self.horizontalLayout_4.addWidget(self.sbHoldingRegsStartAddr)
        self.lblHoldRegs = QtGui.QLabel(self.frame_4)
        self.lblHoldRegs.setObjectName(_fromUtf8("lblHoldRegs"))
        self.horizontalLayout_4.addWidget(self.lblHoldRegs)
        self.sbNoOfHoldingRegs = QtGui.QSpinBox(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbNoOfHoldingRegs.sizePolicy().hasHeightForWidth())
        self.sbNoOfHoldingRegs.setSizePolicy(sizePolicy)
        self.sbNoOfHoldingRegs.setMinimumSize(QtCore.QSize(50, 0))
        self.sbNoOfHoldingRegs.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sbNoOfHoldingRegs.setMinimum(1)
        self.sbNoOfHoldingRegs.setMaximum(500)
        self.sbNoOfHoldingRegs.setSingleStep(10)
        self.sbNoOfHoldingRegs.setProperty("value", 50)
        self.sbNoOfHoldingRegs.setObjectName(_fromUtf8("sbNoOfHoldingRegs"))
        self.horizontalLayout_4.addWidget(self.sbNoOfHoldingRegs)
        self.chkSimHoldRegs = QtGui.QCheckBox(self.frame_4)
        self.chkSimHoldRegs.setObjectName(_fromUtf8("chkSimHoldRegs"))
        self.horizontalLayout_4.addWidget(self.chkSimHoldRegs)
        self.cmbHoldRegsType = QtGui.QComboBox(self.frame_4)
        self.cmbHoldRegsType.setMaxVisibleItems(2)
        self.cmbHoldRegsType.setObjectName(_fromUtf8("cmbHoldRegsType"))
        self.cmbHoldRegsType.addItem(_fromUtf8(""))
        self.cmbHoldRegsType.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.cmbHoldRegsType)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.tvHoldingRegistersData = QtGui.QTableView(self.tabHoldingRegisters)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tvHoldingRegistersData.sizePolicy().hasHeightForWidth())
        self.tvHoldingRegistersData.setSizePolicy(sizePolicy)
        self.tvHoldingRegistersData.setMinimumSize(QtCore.QSize(450, 0))
        self.tvHoldingRegistersData.setCornerButtonEnabled(False)
        self.tvHoldingRegistersData.setObjectName(_fromUtf8("tvHoldingRegistersData"))
        self.tvHoldingRegistersData.horizontalHeader().setVisible(False)
        self.tvHoldingRegistersData.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.tvHoldingRegistersData)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/AO.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabIOs.addTab(self.tabHoldingRegisters, icon5, _fromUtf8(""))
        self.vericallayout.addWidget(self.tabIOs)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menuBar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuCommands = QtGui.QMenu(self.menuBar)
        self.menuCommands.setObjectName(_fromUtf8("menuCommands"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/exit-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSerial_RTU = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/serial-pot-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSerial_RTU.setIcon(icon7)
        self.actionSerial_RTU.setIconVisibleInMenu(True)
        self.actionSerial_RTU.setObjectName(_fromUtf8("actionSerial_RTU"))
        self.actionTCP = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/ethernet-port-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTCP.setIcon(icon8)
        self.actionTCP.setIconVisibleInMenu(True)
        self.actionTCP.setObjectName(_fromUtf8("actionTCP"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/info-sign-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSettings = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/options-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon10)
        self.actionSettings.setIconVisibleInMenu(True)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionBus_Monitor = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/TV-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBus_Monitor.setIcon(icon11)
        self.actionBus_Monitor.setObjectName(_fromUtf8("actionBus_Monitor"))
        self.actionReset_Counters = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/reset-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_Counters.setIcon(icon12)
        self.actionReset_Counters.setObjectName(_fromUtf8("actionReset_Counters"))
        self.actionLog = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/text-x-log-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLog.setIcon(icon13)
        self.actionLog.setObjectName(_fromUtf8("actionLog"))
        self.actionModbus_Manual = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/help-desk-icon-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionModbus_Manual.setIcon(icon14)
        self.actionModbus_Manual.setObjectName(_fromUtf8("actionModbus_Manual"))
        self.actionLoad_Session = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/document-import-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_Session.setIcon(icon15)
        self.actionLoad_Session.setObjectName(_fromUtf8("actionLoad_Session"))
        self.actionSave_Session = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/document-export-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Session.setIcon(icon16)
        self.actionSave_Session.setObjectName(_fromUtf8("actionSave_Session"))
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/plug-disconnect-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/plug-connect-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionConnect.setIcon(icon17)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionHeaders = QtGui.QAction(MainWindow)
        self.actionHeaders.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/Header16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHeaders.setIcon(icon18)
        self.actionHeaders.setObjectName(_fromUtf8("actionHeaders"))
        self.menuFile.addAction(self.actionLoad_Session)
        self.menuFile.addAction(self.actionSave_Session)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionSerial_RTU)
        self.menuOptions.addAction(self.actionTCP)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionModbus_Manual)
        self.menuHelp.addAction(self.actionAbout)
        self.menuView.addAction(self.actionLog)
        self.menuView.addAction(self.actionBus_Monitor)
        self.menuView.addAction(self.actionHeaders)
        self.menuCommands.addAction(self.actionConnect)
        self.menuCommands.addAction(self.actionReset_Counters)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuCommands.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.lblModbusMode.setBuddy(self.cmbModbusMode)
        self.lblSlave.setBuddy(self.sbSlaveID)

        self.retranslateUi(MainWindow)
        self.tabIOs.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pyModSlave", None))
        self.lblModbusMode.setText(_translate("MainWindow", "Modbus Mode", None))
        self.cmbModbusMode.setItemText(0, _translate("MainWindow", "RTU", None))
        self.cmbModbusMode.setItemText(1, _translate("MainWindow", "TCP", None))
        self.lblSlave.setText(_translate("MainWindow", "Slave Addr", None))
        self.lblSimCycle.setText(_translate("MainWindow", "SimCycle (msec)", None))
        self.pbResetDO.setToolTip(_translate("MainWindow", "Reset", None))
        self.lblCoilsStartAddr.setText(_translate("MainWindow", "Start Addr", None))
        self.label.setText(_translate("MainWindow", "No of Coils", None))
        self.chkSimCoils.setText(_translate("MainWindow", "Sim", None))
        self.tabIOs.setTabText(self.tabIOs.indexOf(self.tabCoils), _translate("MainWindow", "Coils", None))
        self.pbResetDI.setToolTip(_translate("MainWindow", "Reset", None))
        self.lblDigInputsStartAddr.setText(_translate("MainWindow", "Start Addr", None))
        self.lblNoOfDigInputs.setText(_translate("MainWindow", "No of Inputs", None))
        self.chkSimDisInputs.setText(_translate("MainWindow", "Sim", None))
        self.tabIOs.setTabText(self.tabIOs.indexOf(self.tabDiscreteInputs), _translate("MainWindow", "Discrete Inputs", None))
        self.pbResetAI.setToolTip(_translate("MainWindow", "Reset", None))
        self.lblInputRegsStartAddr.setText(_translate("MainWindow", "Start Addr", None))
        self.lblNoOfInputRegs.setText(_translate("MainWindow", "No of Regs", None))
        self.chkSimInputRegs.setText(_translate("MainWindow", "Sim", None))
        self.cmbInputRegsType.setItemText(0, _translate("MainWindow", "Dec", None))
        self.cmbInputRegsType.setItemText(1, _translate("MainWindow", "Hex", None))
        self.tabIOs.setTabText(self.tabIOs.indexOf(self.tabInputRegisters), _translate("MainWindow", "Input Registers", None))
        self.pbResetAO.setToolTip(_translate("MainWindow", "Reset", None))
        self.lblHoldRegsStarAddr.setText(_translate("MainWindow", "Start Addr", None))
        self.lblHoldRegs.setText(_translate("MainWindow", "No of Regs", None))
        self.chkSimHoldRegs.setText(_translate("MainWindow", "Sim", None))
        self.cmbHoldRegsType.setItemText(0, _translate("MainWindow", "Dec", None))
        self.cmbHoldRegsType.setItemText(1, _translate("MainWindow", "Hex", None))
        self.tabIOs.setTabText(self.tabIOs.indexOf(self.tabHoldingRegisters), _translate("MainWindow", "Holding Registers", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuCommands.setTitle(_translate("MainWindow", "Commands", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSerial_RTU.setText(_translate("MainWindow", "Modbus RTU...", None))
        self.actionTCP.setText(_translate("MainWindow", "Modbus TCP...", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings...", None))
        self.actionBus_Monitor.setText(_translate("MainWindow", "Bus Monitor", None))
        self.actionReset_Counters.setText(_translate("MainWindow", "Reset Counters", None))
        self.actionLog.setText(_translate("MainWindow", "Log", None))
        self.actionModbus_Manual.setText(_translate("MainWindow", "Modbus Manual", None))
        self.actionLoad_Session.setText(_translate("MainWindow", "Load Session...", None))
        self.actionSave_Session.setText(_translate("MainWindow", "Save Session...", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionHeaders.setText(_translate("MainWindow", "Headers", None))

import pyModSlaveQt_rc
