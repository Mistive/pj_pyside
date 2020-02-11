import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
#from PySide2.QtCore import SIGNAL, SLOT, QObject

import Logon_rc

if __name__ == '__main__':

    app = QApplication(sys.argv)    #QApplication : 프로그램을 대표하는 객체
    logon = QWidget()   #최상위 창을 만든다

    labelId = QLabel('&Id :')   #각 라벨을 설정한다.(Text)
    labelId.setAlignment(Qt.AlignRight | Qt.AlignVCenter)   
    labelPW = QLabel('&Password:')

    lineEditId = QLineEdit()    #무언가를 입력할 수 있는 창을 생성
    lineEditPW = QLineEdit()
    lineEditPW.setEchoMode(QLineEdit.Password)  #치는 값을 안보이게 함

    labelId.setBuddy(lineEditId)    #일종의 매핑느낌?
    labelPW.setBuddy(lineEditPW)

    buttonOk = QPushButton("&Ok")   #푸시버튼 생성
    buttonOk.setIcon(QIcon(":/images/ok.png"))  #푸시 버튼의 아이콘 생성

    #레이아웃 클래스를 이용해 창의 크기가 바뀌어도 글씨가 잘리거나 하지 않음
    layout1 = QGridLayout()
    layout1.addWidget(labelId,0,0)  #(row, col) 위치 값으로 설정
    layout1.addWidget(lineEditId,0,1)
    layout1.addWidget(labelPW,1,0)
    layout1.addWidget(lineEditPW,1,1)

    layout2 = QHBoxLayout()
    layout2.addStretch()    #빈칸 생성
    layout2.addWidget(buttonOk) #버튼 추가

#일종의 레이아웃 합성
    mainLayout = QVBoxLayout()
    mainLayout.addLayout(layout1)
    mainLayout.addLayout(layout2)

    logon.setLayout(mainLayout) # setLayout 호출 시 자동으로 객체 부모 자식관계를 설정
    logon.setWindowTitle('Log on')
    logon.setWindowIcon(QIcon(":/images/ok.png"))

    buttonOk.clicked.connect(app.quit)

    logon.show()
    app.exec_()