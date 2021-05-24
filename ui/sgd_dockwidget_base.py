# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sgd_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sgdDockWidgetBase(object):
    def setupUi(self, sgdDockWidgetBase):
        sgdDockWidgetBase.setObjectName("sgdDockWidgetBase")
        sgdDockWidgetBase.resize(467, 782)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.guiGroupSearch = QtWidgets.QGroupBox(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.guiGroupSearch.setFont(font)
        self.guiGroupSearch.setObjectName("guiGroupSearch")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.guiGroupSearch)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.guiDatasetList = QtWidgets.QListWidget(self.guiGroupSearch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guiDatasetList.sizePolicy().hasHeightForWidth())
        self.guiDatasetList.setSizePolicy(sizePolicy)
        self.guiDatasetList.setMinimumSize(QtCore.QSize(0, 80))
        self.guiDatasetList.setMaximumSize(QtCore.QSize(16777215, 1600))
        self.guiDatasetList.setAlternatingRowColors(False)
        self.guiDatasetList.setObjectName("guiDatasetList")
        self.verticalLayout_3.addWidget(self.guiDatasetList)
        self.guiDatasetStatus = QtWidgets.QLabel(self.guiGroupSearch)
        self.guiDatasetStatus.setText("")
        self.guiDatasetStatus.setObjectName("guiDatasetStatus")
        self.verticalLayout_3.addWidget(self.guiDatasetStatus)
        self.verticalLayout.addWidget(self.guiGroupSearch)
        self.guiGroupOptions = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.guiGroupOptions.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.guiGroupOptions.setFont(font)
        self.guiGroupOptions.setFlat(False)
        self.guiGroupOptions.setCheckable(False)
        self.guiGroupOptions.setObjectName("guiGroupOptions")
        self.formLayout = QtWidgets.QFormLayout(self.guiGroupOptions)
        self.formLayout.setObjectName("formLayout")
        self.guiFormatL = QtWidgets.QLabel(self.guiGroupOptions)
        self.guiFormatL.setObjectName("guiFormatL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.guiFormatL)
        self.guiFormat = QtWidgets.QComboBox(self.guiGroupOptions)
        self.guiFormat.setObjectName("guiFormat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.guiFormat)
        self.guiResolutionL = QtWidgets.QLabel(self.guiGroupOptions)
        self.guiResolutionL.setObjectName("guiResolutionL")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.guiResolutionL)
        self.guiResolution = QtWidgets.QComboBox(self.guiGroupOptions)
        self.guiResolution.setObjectName("guiResolution")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.guiResolution)
        self.guiCoordsysL = QtWidgets.QLabel(self.guiGroupOptions)
        self.guiCoordsysL.setObjectName("guiCoordsysL")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.guiCoordsysL)
        self.guiCoordsys = QtWidgets.QComboBox(self.guiGroupOptions)
        self.guiCoordsys.setObjectName("guiCoordsys")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.guiCoordsys)
        self.guiTimestampL = QtWidgets.QLabel(self.guiGroupOptions)
        self.guiTimestampL.setObjectName("guiTimestampL")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.guiTimestampL)
        self.guiTimestamp = QtWidgets.QComboBox(self.guiGroupOptions)
        self.guiTimestamp.setObjectName("guiTimestamp")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.guiTimestamp)
        self.verticalLayout.addWidget(self.guiGroupOptions)
        self.guiGroupExtent = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.guiGroupExtent.setObjectName("guiGroupExtent")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.guiGroupExtent)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.guiFullExtentChbox = QtWidgets.QCheckBox(self.guiGroupExtent)
        self.guiFullExtentChbox.setObjectName("guiFullExtentChbox")
        self.horizontalLayout_2.addWidget(self.guiFullExtentChbox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.guiExtentWidget = gui.QgsExtentGroupBox(self.guiGroupExtent)
        self.guiExtentWidget.setTitleBase("")
        self.guiExtentWidget.setObjectName("guiExtentWidget")
        self.verticalLayout_2.addWidget(self.guiExtentWidget)
        self.verticalLayout.addWidget(self.guiGroupExtent)
        self.guiGroupFiles = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.guiGroupFiles.setObjectName("guiGroupFiles")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.guiGroupFiles)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.guiRequestListBtn = QtWidgets.QPushButton(self.guiGroupFiles)
        self.guiRequestListBtn.setObjectName("guiRequestListBtn")
        self.horizontalLayout_3.addWidget(self.guiRequestListBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.guiLabel23 = QtWidgets.QLabel(self.guiGroupFiles)
        self.guiLabel23.setObjectName("guiLabel23")
        self.horizontalLayout_3.addWidget(self.guiLabel23)
        self.guiFileType = QtWidgets.QComboBox(self.guiGroupFiles)
        self.guiFileType.setObjectName("guiFileType")
        self.horizontalLayout_3.addWidget(self.guiFileType)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.guiFileListLayout = QtWidgets.QVBoxLayout()
        self.guiFileListLayout.setObjectName("guiFileListLayout")
        self.verticalLayout_4.addLayout(self.guiFileListLayout)
        self.guiFileListStatus = QtWidgets.QLabel(self.guiGroupFiles)
        self.guiFileListStatus.setText("")
        self.guiFileListStatus.setObjectName("guiFileListStatus")
        self.verticalLayout_4.addWidget(self.guiFileListStatus)
        self.verticalLayout.addWidget(self.guiGroupFiles)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.guiDownloadBtn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.guiDownloadBtn.setObjectName("guiDownloadBtn")
        self.horizontalLayout.addWidget(self.guiDownloadBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.guiShowMapBtn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.guiShowMapBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/swissgeodownloader/resources/switzerland.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guiShowMapBtn.setIcon(icon)
        self.guiShowMapBtn.setFlat(False)
        self.guiShowMapBtn.setObjectName("guiShowMapBtn")
        self.horizontalLayout_4.addWidget(self.guiShowMapBtn)
        self.guiInfoBtn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.guiInfoBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/swissgeodownloader/resources/die-info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guiInfoBtn.setIcon(icon1)
        self.guiInfoBtn.setFlat(False)
        self.guiInfoBtn.setObjectName("guiInfoBtn")
        self.horizontalLayout_4.addWidget(self.guiInfoBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        sgdDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(sgdDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(sgdDockWidgetBase)

    def retranslateUi(self, sgdDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        sgdDockWidgetBase.setWindowTitle(_translate("sgdDockWidgetBase", "Swiss Geo Downloader"))
        self.guiGroupSearch.setTitle(_translate("sgdDockWidgetBase", "1. Dataset"))
        self.guiGroupOptions.setTitle(_translate("sgdDockWidgetBase", "2. Options"))
        self.guiFormatL.setText(_translate("sgdDockWidgetBase", "Format"))
        self.guiFormat.setToolTip(_translate("sgdDockWidgetBase", "Select format"))
        self.guiResolutionL.setText(_translate("sgdDockWidgetBase", "Resolution [m]"))
        self.guiResolution.setToolTip(_translate("sgdDockWidgetBase", "Select resolution (only raster based datasets)"))
        self.guiCoordsysL.setText(_translate("sgdDockWidgetBase", "Coord.sys"))
        self.guiCoordsys.setToolTip(_translate("sgdDockWidgetBase", "Select coordinate reference system"))
        self.guiTimestampL.setText(_translate("sgdDockWidgetBase", "Timestamp"))
        self.guiTimestamp.setToolTip(_translate("sgdDockWidgetBase", "Select timestamp"))
        self.guiGroupExtent.setTitle(_translate("sgdDockWidgetBase", "3. Extent"))
        self.guiFullExtentChbox.setText(_translate("sgdDockWidgetBase", "Full dataset extent"))
        self.guiGroupFiles.setTitle(_translate("sgdDockWidgetBase", "4. Files"))
        self.guiRequestListBtn.setToolTip(_translate("sgdDockWidgetBase", "Requests are limited to max. 100 files"))
        self.guiRequestListBtn.setText(_translate("sgdDockWidgetBase", "Request file list"))
        self.guiLabel23.setText(_translate("sgdDockWidgetBase", "Filter by type"))
        self.guiFileType.setToolTip(_translate("sgdDockWidgetBase", "Filter file list by type"))
        self.guiDownloadBtn.setToolTip(_translate("sgdDockWidgetBase", "Download list of files"))
        self.guiDownloadBtn.setText(_translate("sgdDockWidgetBase", "Download"))
        self.guiShowMapBtn.setToolTip(_translate("sgdDockWidgetBase", "Show overview map"))
        self.guiInfoBtn.setToolTip(_translate("sgdDockWidgetBase", "Plugin info"))
from qgis import gui
from ..resources import resources
