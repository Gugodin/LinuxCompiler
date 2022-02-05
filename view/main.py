from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Comandos de Linux")
        Dialog.resize(639, 406)
        self.buttonC = QPushButton(Dialog)
        self.buttonC.setObjectName(u"buttonC")
        self.buttonC.setGeometry(QRect(420, 50, 75, 23))
        self.textEdit = QLineEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 50, 281, 21))
        self.tokens = QLabel(Dialog)
        self.tokens.setObjectName(u"tokens")
        self.tokens.setGeometry(QRect(90, 190, 431, 141))
        self.tokens.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.remover_2 = QLabel(Dialog)
        self.remover_2.setObjectName(u"remover_2")
        self.remover_2.setGeometry(QRect(250, 130, 141, 21))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.remover_2.setFont(font)
        self.remover_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.buttonC.setText(QCoreApplication.translate("Dialog", u"Comprobar", None))
        self.tokens.setText("")
        self.remover_2.setText(QCoreApplication.translate("Dialog", u"Tokens: ", None))
