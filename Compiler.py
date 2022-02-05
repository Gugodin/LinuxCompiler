import string
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from view.main import Ui_Dialog

class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.tokens= [
        ['crear','mkdir'],
        ['mover','cd'],
        ['mostrar','ls'],
        ['editar','mv'],
        ['remover','rm'],
        ['crearA','touch'],
        ['diagonal','/'],
        ['guion','-'],
        ['guionB','_'],
        ['PP','..'],
        ['numero',list(string.digits)],
        ['letra',list(string.ascii_letters)]
        ]





# if __name__ == '__main__':
    # command = input('Escribe tu comando de Linux ').split(' ')

    # for i in range(len(command)):
    #     band = False
    #     palabra = command[i]
    #     # print(palabra)

    #     for e in range(len(tokens)):
    #         # print(tokens[e][1])
    #         if palabra == tokens[e][1]:
    #             print(f'Token: {tokens[e][0]}')
    #             band = True
    #             break

    #     if band == False:       
    #         for z in range(len(palabra)):

    #             char = palabra[z]

    #             for e in range(len(tokens)):

    #                 if tokens[e][0] == 'numero' or tokens[e][0] == 'letra':

    #                     if tokens[e][1].count(char) > 0:
    #                         print(f'Token: {tokens[e][0]}')
    #                         band = True
    #                         break
                    
    #                 elif char == tokens[e][1]:
    #                     print(f'Token: {tokens[e][0]}')
    #                     band = True
    #                     break

    #     if band == False:
    #         print(f'El carater siguiente no existe dentro de nuestros tokens {command[i]}')
    #         break
    
        self.ui.buttonC.clicked.connect(self.getTockens) ##ESTO NO SE DONDE VA XD

def getTockens(self):
    command = self.ui.textEdit.text().split(' ')
    listTokens = []

    for i in range(len(command)):
        band = False
        palabra = command[i]

        for e in range(len(self.tokens)):
            if palabra == self.tokens[e][1]:
                print(f'Token: {self.tokens[e][0]}')
                listTokens.append(self.tokens[e][0])
                band = True
                break
        if band == False:       
            for z in range(len(palabra)):

                char = palabra[z]

                for e in range(len(self.tokens)):

                    if self.tokens[e][0] == 'numero' or self.tokens[e][0] == 'letra':

                        if self.tokens[e][1].count(char) > 0:
                            print(f'Token: {self.tokens[e][0]}')
                            listTokens.append(self.tokens[e][0])
                            break
                    
                    elif char == self.tokens[e][1]:
                        print(f'Token: {self.tokens[e][0]}')
                        listTokens.append(self.tokens[e][0])
                        break
    cadenaT = ''
    for i in range(len(listTokens)):
        cadenaT = cadenaT + listTokens[i] + ' '
    
    font = QFont()
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(QFont.Bold)
    self.ui.tokens.setFont(font)
    self.ui.tokens.setText(cadenaT)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec())
   


    # print(command)
