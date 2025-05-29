from src.Vista.VentanaRegistro import Ui_FormRegistro as VentanaRegistro
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Validaciones import Validaciones
from PyQt6 import QtWidgets


class ControladorRegistro(QtWidgets.QMainWindow, VentanaRegistro):
    def __init__(self, lista_estudiantes: ListaEstudiantes, parent=None):
        super().__init__(parent)
        self.ventana_anterior = parent
        self.setupUi(self)
        self.btnRegistrarUsuario.clicked.connect(self.validar_campos)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.cbxMostrarPassword.stateChanged.connect(
            lambda estado: self.txtPassword.setEchoMode(
                QtWidgets.QLineEdit.EchoMode.Normal if estado else QtWidgets.QLineEdit.EchoMode.Password
            )
        )
        self.lista_estudiantes = lista_estudiantes
        self.validador = Validaciones()
        self.show()

    def validar_campos(self):
        if not self.validador.validar_cedula(self.txtCedula.text()):
            QtWidgets.QMessageBox.warning(self, "Error", "La cédula ingresada no es válida.")
            return
        if self.txtNombre.text().strip() == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Debe ingresar por lo menos un Nombre")
            return
        if self.txtEmail.text().strip() != "":
            if not self.validador.validar_correo(self.txtEmail.text()):
                QtWidgets.QMessageBox.warning(self, "Error", "Correo Ingresado es incorrecto")
                return
        if self.txtCelular.text().strip() != "":
            if not self.validador.validar_celular(self.txtCelular.text()):
                QtWidgets.QMessageBox.warning(self, "Error", "Celular ingresado debe tener entre 7 y 10 números")
                return
        if len(self.txtUsuario.text()) < 5:
            QtWidgets.QMessageBox.warning(self, "Error", "El usuario debe tener al menos 5 caracteres.")
            return

        if not self.validador.validar_usuario(self.lista_estudiantes.listado_estudiantes, self.txtUsuario.text()):
            QtWidgets.QMessageBox.warning(self, "Error", "El usuario seleccionado está ocupado."
                                                         "\nIngrese otro.")
            return

        if self.txtPassword.text() != self.txtConfirmaPassword.text():
            QtWidgets.QMessageBox.warning(self, "Error", "Las contraseñas no coinciden.")
            return
        print("Registrando Usuario")
        self.registrar_usuario()

    def registrar_usuario(self):
        try:
            self.lista_estudiantes.registrar_estudiante(self.txtCedula.text(), self.txtNombre.text(),
                                                       self.txtApellido.text(), self.txtEmail.text(),
                                                       self.txtCelular.text(), self.txtUsuario.text(),
                                                       self.txtPassword.text())
            QtWidgets.QMessageBox.about(self, "Registrado", ("Usuario Registrado Correctamente." +
                                                             "\nUsuario:   \t" + self.txtUsuario.text() +
                                                             "\nContraseña:\t" + self.txtPassword.text()))
            self.close()
        except Exception as e:
            print(e)

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.ventana_anterior.show()
        super().closeEvent(event)
