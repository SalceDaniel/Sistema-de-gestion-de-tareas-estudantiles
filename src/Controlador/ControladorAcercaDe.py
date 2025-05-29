from src.Vista.VentanaAcercaDe import Ui_frmAcercaDe as VentanaAcercaDe
from PyQt6 import QtWidgets


class ControladorAcercaDe(QtWidgets.QMainWindow, VentanaAcercaDe):

    def __init__(self, parent=None):
        super(ControladorAcercaDe, self).__init__(parent)
        self.ventana_anterior = parent
        self.setupUi(self)
        self.btnRegresar.clicked.connect(self.regresar)

    def regresar(self):
        self.ventana_anterior.show()
        self.close()
