from PySide6 import QtCore, QtWidgets, QtGui
import sys
import random

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Uma lista de olá mundo
        self.hello = ["Hallo Welt", "Hei maailma", "Olá Mundo"]
        
        # Cria um botão 
        self.button = QtWidgets.QPushButton("Click me")

        # Cria um texto e coloca ele alinhado no centro
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.interface = QtWidgets.QVBoxLayout(self)
        self.interface.addWidget(self.text)

        self.interface.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

# Executar a aplicação
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())