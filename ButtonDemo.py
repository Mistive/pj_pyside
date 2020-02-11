from PySide2.QtWidgets import *

import sys

from ui_ButtonDemo import Ui_buttonDemo


class MyForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = Ui_buttonDemo()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.okButtonClicked)
        self.ui.checkBox.toggled.connect(self.onCaseSensitivity)
        self.ui.button1.toggled.connect(self.onMale)

    def okButtonClicked(self):
        print('okButtonClicked')

    def onCaseSensitivity(self, toggle):
        print('okCaseSensitity', toggle)
        print(self.ui.checkBox.isChecked())

    def onMale(self, toggle):
        print('onMale', toggle)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = MyForm()
    form.show()
    app.exec_()