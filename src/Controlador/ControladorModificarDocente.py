from src.Vista.VentanaAgregarDocente import Ui_frmAgregarProfesor as VentanaModificarDocente
from src.Modelo.ListaDocentes import ListaDocentes
from src.Modelo.Docente import Docente
from src.Modelo.Validaciones import Validaciones
from PyQt6 import QtWidgets, QtCore


class ControladorModificarDocente(QtWidgets.QMainWindow, VentanaModificarDocente):
    actualizar_datos = QtCore.pyqtSignal()

    def __init__(self, docente: Docente, lista_docentes: ListaDocentes,  parent=None):
        super(ControladorModificarDocente, self).__init__(parent)
        self.ventana_anterior = parent
        self.docente = docente
        self.lista_docentes = lista_docentes
        self.validador = Validaciones()

        self.setupUi(self)
        self.btnAgregarDocente.clicked.connect(self.validar_campos)
        self.btnCancelar.clicked.connect(self.cancelar)

        self.btnAgregarDocente.setText("Guardar Cambios")
        self.lblAgregarDocente.setText("Modificar Docente")
        self.setWindowTitle("::Sistema Gestión de Tareas:: Modificar Docente")
        self.txtCedula.setText(docente.cedula)
        self.txtNombre.setText(docente.nombre)
        self.txtApellido.setText(docente.apellido)
        self.txtEmail.setText(docente.correo)
        self.txtCelular.setText(docente.celular)

    def validar_campos(self):
        if self.txtCedula.text().strip() != "":
            if not self.validador.validar_cedula(self.txtCedula.text()):
                QtWidgets.QMessageBox.warning(self, "Error", "La cédula ingresada no es válida.")
                return
        if self.txtEmail.text().strip() != "":
            if not self.validador.validar_correo(self.txtEmail.text()):
                QtWidgets.QMessageBox.warning(self, "Error", "Correo Ingresado es incorrecto")
                return
        print("Registrando Docente")
        self.registrar_docente()

    def registrar_docente(self):
        try:
            self.docente.cedula = self.txtCedula.text()
            self.docente.nombre = self.txtNombre.text()
            self.docente.apellido = self.txtApellido.text()
            self.docente.correo = self.txtEmail.text()
            self.docente.celular = self.txtCelular.text()

            QtWidgets.QMessageBox.about(self, "Registrado", ("Docente Modificado Correctamente." +
                                                             "\nNombre:   \t" + self.txtNombre.text() +
                                                             "\nApellido: \t" + self.txtApellido.text()))

            self.lista_docentes.actualizar_docente(self.docente)
            self.actualizar_datos.emit()
            self.close()
        except Exception as e:
            print(e)

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.ventana_anterior.show()
        super().closeEvent(event)
