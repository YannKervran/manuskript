# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/settings.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(485, 379)
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Settings)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lstLabels = QtWidgets.QListView(self.tab)
        self.lstLabels.setObjectName("lstLabels")
        self.horizontalLayout_2.addWidget(self.lstLabels)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnLabelColor = QtWidgets.QPushButton(self.tab)
        self.btnLabelColor.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLabelColor.sizePolicy().hasHeightForWidth())
        self.btnLabelColor.setSizePolicy(sizePolicy)
        self.btnLabelColor.setMinimumSize(QtCore.QSize(64, 64))
        self.btnLabelColor.setMaximumSize(QtCore.QSize(64, 64))
        self.btnLabelColor.setText("")
        self.btnLabelColor.setIconSize(QtCore.QSize(64, 64))
        self.btnLabelColor.setObjectName("btnLabelColor")
        self.verticalLayout_2.addWidget(self.btnLabelColor)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLabelAdd = QtWidgets.QPushButton(self.tab)
        self.btnLabelAdd.setText("")
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnLabelAdd.setIcon(icon)
        self.btnLabelAdd.setObjectName("btnLabelAdd")
        self.horizontalLayout.addWidget(self.btnLabelAdd)
        self.btnLabelRemove = QtWidgets.QPushButton(self.tab)
        self.btnLabelRemove.setText("")
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnLabelRemove.setIcon(icon)
        self.btnLabelRemove.setObjectName("btnLabelRemove")
        self.horizontalLayout.addWidget(self.btnLabelRemove)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lstStatus = QtWidgets.QListView(self.tab_2)
        self.lstStatus.setObjectName("lstStatus")
        self.verticalLayout_4.addWidget(self.lstStatus)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnStatusAdd = QtWidgets.QPushButton(self.tab_2)
        self.btnStatusAdd.setText("")
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnStatusAdd.setIcon(icon)
        self.btnStatusAdd.setObjectName("btnStatusAdd")
        self.horizontalLayout_3.addWidget(self.btnStatusAdd)
        self.btnStatusRemove = QtWidgets.QPushButton(self.tab_2)
        self.btnStatusRemove.setText("")
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnStatusRemove.setIcon(icon)
        self.btnStatusRemove.setObjectName("btnStatusRemove")
        self.horizontalLayout_3.addWidget(self.btnStatusRemove)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.btnLabelColor.setShortcut(_translate("Settings", "Ctrl+S"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Settings", "Labels"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Settings", "Status"))

