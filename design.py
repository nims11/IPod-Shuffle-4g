# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blah.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(485, 295)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 221))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.chkTrackVoiceOver = QtGui.QCheckBox(self.formLayoutWidget)
        self.chkTrackVoiceOver.setObjectName(_fromUtf8("chkTrackVoiceOver"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.chkTrackVoiceOver)
        self.chkPlaylistVoiceOver = QtGui.QCheckBox(self.formLayoutWidget)
        self.chkPlaylistVoiceOver.setObjectName(_fromUtf8("chkPlaylistVoiceOver"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.chkPlaylistVoiceOver)
        self.chkRenameUnicode = QtGui.QCheckBox(self.formLayoutWidget)
        self.chkRenameUnicode.setObjectName(_fromUtf8("chkRenameUnicode"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.chkRenameUnicode)
        self.chkTrackGain = QtGui.QCheckBox(self.formLayoutWidget)
        self.chkTrackGain.setObjectName(_fromUtf8("chkTrackGain"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.chkTrackGain)
        self.trackGain = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.trackGain.setMinimum(0.0)
        self.trackGain.setObjectName(_fromUtf8("trackGain"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.trackGain)
        self.chkAutoDirectoryPlaylist = QtGui.QCheckBox(self.formLayoutWidget)
        self.chkAutoDirectoryPlaylist.setObjectName(_fromUtf8("chkAutoDirectoryPlaylist"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.chkAutoDirectoryPlaylist)
        self.chkID3Template = QtGui.QCheckBox(self.formLayoutWidget)
        self.chkID3Template.setObjectName(_fromUtf8("chkID3Template"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.chkID3Template)
        self.templateTxt = QtGui.QLineEdit(self.formLayoutWidget)
        self.templateTxt.setObjectName(_fromUtf8("templateTxt"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.templateTxt)
        self.btnBrowse = QtGui.QPushButton(self.formLayoutWidget)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.btnBrowse)
        self.btnShuffle = QtGui.QPushButton(self.centralwidget)
        self.btnShuffle.setEnabled(False)
        self.btnShuffle.setGeometry(QtCore.QRect(390, 220, 85, 27))
        self.btnShuffle.setObjectName(_fromUtf8("btnShuffle"))
        self.btnCancel = QtGui.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(300, 220, 85, 27))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.chkTrackVoiceOver.setText(_translate("MainWindow", "Track Voice Over", None))
        self.chkPlaylistVoiceOver.setText(_translate("MainWindow", "Playlist Voice Over", None))
        self.chkRenameUnicode.setText(_translate("MainWindow", "Rename Unicode", None))
        self.chkTrackGain.setText(_translate("MainWindow", "Track Gain", None))
        self.chkAutoDirectoryPlaylist.setText(_translate("MainWindow", "Auto Directory Playlists", None))
        self.chkID3Template.setText(_translate("MainWindow", "ID3 Template", None))
        self.templateTxt.setPlaceholderText(_translate("MainWindow", "{genre} ,{album}-{artist},leave empty for auto", None))
        self.btnBrowse.setText(_translate("MainWindow", "Select the IPOD Folder", None))
        self.btnShuffle.setText(_translate("MainWindow", "Shuffle !", None))
        self.btnCancel.setText(_translate("MainWindow", "Cancel", None))

