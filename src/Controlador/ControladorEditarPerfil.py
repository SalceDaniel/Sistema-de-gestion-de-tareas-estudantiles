from src.Vista.VentanaRegistro import Ui_FormRegistro as VentanaEditarPerfil
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Validaciones import Validaciones
from PyQt6 import QtWidgets, QtCore


class ControladorEditarPerfil(QtWidgets.QMainWindow, VentanaEditarPerfil):
    actualizar_datos = QtCore.pyqtSignal()

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes, parent=None):
        super().__init__(parent)
        self.lista_estudiantes = lista_estudiantes
        self.estudiante_actual = estudiante
        self.validador = Validaciones()

        self.ventana_anterior = parent
        self.setupUi(self)

        self.btnRegistrarUsuario.clicked.connect(self.validar_campos)
        self.llenar_datos_usuario(self.estudiante_actual)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.cbxMostrarPassword.stateChanged.connect(
            lambda estado: self.txtPassword.setEchoMode(
                QtWidgets.QLineEdit.EchoMode.Normal if estado else QtWidgets.QLineEdit.EchoMode.Password
            )
        )
        self.show()

    def llenar_datos_usuario(self, estudiante: Estudiante):
        self.btnRegistrarUsuario.setText("Guardar Cambios")
        self.lblRegistroNuevoUsuario.setText("Editar Perfil")
        self.setWindowTitle("::Sistema Gestión de Tareas:: Editar Perfil")
        self.txtCedula.setText(estudiante.cedula)
        self.txtCedula.setReadOnly(True)
        self.txtCedula.setEnabled(False)
        self.txtUsuario.setText(estudiante.usuario)
        self.txtUsuario.setEnabled(False)
        self.txtUsuario.setReadOnly(True)
        self.txtUsuario.setText(estudiante.usuario)
        self.txtNombre.setText(estudiante.nombre)
        self.txtApellido.setText(estudiante.apellido)
        self.txtEmail.setText(estudiante.correo)
        self.txtCelular.setText(estudiante.celular)
        self.txtPassword.setText(estudiante.contrasena)
        self.txtConfirmaPassword.setText(estudiante.contrasena)

    def validar_campos(self):
        if self.txtCedula.text().strip() != "":
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

        if self.txtPassword.text() != self.txtConfirmaPassword.text():
            QtWidgets.QMessageBox.warning(self, "Error", "Las contraseñas no coinciden.")
            return
        print("Registrando Cambios")
        self.guardar_cambios()

    def guardar_cambios(self):
        try:
            self.estudiante_actual: Estudiante
            self.estudiante_actual.nombre = self.txtNombre.text()
            self.estudiante_actual.apellido = self.txtApellido.text()
            self.estudiante_actual.correo = self.txtEmail.text()
            self.estudiante_actual.celular = self.txtCelular.text()
            self.estudiante_actual.contrasena = self.txtPassword.text()
            QtWidgets.QMessageBox.about(self, "Registrado", ("Cambios Guardados Correctamente." +
                                                             "\nUsuario:   \t" + self.txtUsuario.text() +
                                                             "\nContraseña:\t" + self.txtPassword.text()))
            self.lista_estudiantes.actualizar_estudiante(self.estudiante_actual)
            self.actualizar_datos.emit()
            self.close()
        except Exception as e:
            print(e)

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.ventana_anterior.show()
        super().closeEvent(event)
