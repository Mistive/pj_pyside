# if __name__ == '__main__':
#     from PySide2.QtCore import QCoreApplication
#     QCoreApplication.setLibraryPaths(['C:/Users/user/Anaconda3/Lib/site-packages/PySide2/plugins'])

from PySide2.QtWidgets import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()  #최상위 창 생성
    window.resize(289,170)
    window.setWindowTitle("FIrst Qt Program")

    label = QLabel('Hello Qt',window)   #내부 창 생성성
    label.move(110,80)

    window.show()
    app.exec_()