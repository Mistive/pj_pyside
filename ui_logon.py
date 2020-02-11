# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Logon.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import Logon_rc

class Ui_Logon(object):
    def setupUi(self, Logon):
        if Logon.objectName():
            Logon.setObjectName(u"Logon")
        Logon.resize(391, 174)
        icon = QIcon()
        icon.addFile(u":/images/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        Logon.setWindowIcon(icon)
        self.layoutWidget = QWidget(Logon)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 40, 279, 51))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelID = QLabel(self.layoutWidget)
        self.labelID.setObjectName(u"labelID")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelID)

        self.lineEditId = QLineEdit(self.layoutWidget)
        self.lineEditId.setObjectName(u"lineEditId")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditId)

        self.labelPW = QLabel(self.layoutWidget)
        self.labelPW.setObjectName(u"labelPW")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelPW)

        self.lineEditPW = QLineEdit(self.layoutWidget)
        self.lineEditPW.setObjectName(u"lineEditPW")
        self.lineEditPW.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditPW)

        self.layoutWidget1 = QWidget(Logon)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 100, 280, 32))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(178, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonOk = QPushButton(self.layoutWidget1)
        self.buttonOk.setObjectName(u"buttonOk")

        self.horizontalLayout.addWidget(self.buttonOk)

#if QT_CONFIG(shortcut)
        self.labelID.setBuddy(self.lineEditId)
        self.labelPW.setBuddy(self.lineEditPW)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEditId, self.lineEditPW)
        QWidget.setTabOrder(self.lineEditPW, self.buttonOk)

        self.retranslateUi(Logon)

        QMetaObject.connectSlotsByName(Logon)
    # setupUi

    def retranslateUi(self, Logon):
        Logon.setWindowTitle(QCoreApplication.translate("Logon", u"Log on", None))
        self.labelID.setText(QCoreApplication.translate("Logon", u"&id :", None))
        self.labelPW.setText(QCoreApplication.translate("Logon", u"&password :", None))
        self.buttonOk.setText(QCoreApplication.translate("Logon", u"OK", None))
    # retranslateUi

