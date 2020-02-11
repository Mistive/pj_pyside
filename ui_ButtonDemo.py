# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ButtonDemo.ui'
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


class Ui_buttonDemo(object):
    def setupUi(self, buttonDemo):
        if buttonDemo.objectName():
            buttonDemo.setObjectName(u"buttonDemo")
        buttonDemo.resize(400, 400)
        self.button = QPushButton(buttonDemo)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(50, 52, 301, 28))
        self.button.setLayoutDirection(Qt.LeftToRight)
        self.checkBox = QCheckBox(buttonDemo)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(50, 87, 301, 16))
        self.groupBox = QGroupBox(buttonDemo)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(50, 110, 301, 75))
        self.button1 = QRadioButton(self.groupBox)
        self.button1.setObjectName(u"button1")
        self.button1.setGeometry(QRect(12, 24, 55, 16))
        self.button1.setAutoFillBackground(False)
        self.button1.setCheckable(True)
        self.button1.setChecked(True)
        self.button2 = QRadioButton(self.groupBox)
        self.button2.setObjectName(u"button2")
        self.button2.setGeometry(QRect(12, 47, 69, 16))

        self.retranslateUi(buttonDemo)

        QMetaObject.connectSlotsByName(buttonDemo)
    # setupUi

    def retranslateUi(self, buttonDemo):
        buttonDemo.setWindowTitle(QCoreApplication.translate("buttonDemo", u"Button Demo", None))
        self.button.setText(QCoreApplication.translate("buttonDemo", u"OK", None))
        self.checkBox.setText(QCoreApplication.translate("buttonDemo", u"Case sensitivity", None))
        self.groupBox.setTitle(QCoreApplication.translate("buttonDemo", u"Sex", None))
        self.button1.setText(QCoreApplication.translate("buttonDemo", u"Male", None))
        self.button2.setText(QCoreApplication.translate("buttonDemo", u"Female", None))
    # retranslateUi

