import sys

from src.Controlador.ControladorLogin import ControladorLogin
from PyQt6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = ControladorLogin()
    myapp.show()
    app.exec()
