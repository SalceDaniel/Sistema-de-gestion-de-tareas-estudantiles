from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.ListaDocentes import ListaDocentes
from src.Vista.VentanaLogin import Ui_FormLogin as VentanaLogin
from src.Controlador.ControladorPrincipal import ControladorPrincipal
from src.Controlador.ControladorRegistro import ControladorRegistro
from PyQt6 import QtWidgets


class ControladorLogin(QtWidgets.QMainWindow, VentanaLogin):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ventana_registro = None
        self.ventana_principal = None
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.iniciar_sesion)
        self.btnRegister.clicked.connect(self.registrar_usuario)

        self.cbxShowPassword.stateChanged.connect(
            lambda estado: self.txtContrasena.setEchoMode(
                QtWidgets.QLineEdit.EchoMode.Normal if estado else QtWidgets.QLineEdit.EchoMode.Password
            )
        )
        self.lista_estudiantes = ListaEstudiantes()
        self.lista_docentes = ListaDocentes()

    def iniciar_sesion(self):
        try:
            usuario = self.txtUsuario.text()
            contrasena = self.txtContrasena.text()

            if self.lista_estudiantes.login_estudiante(usuario, contrasena):
                self.txtUsuario.setText("")
                self.txtContrasena.setText("")
                self.abrir_ventana_principal(self.lista_estudiantes.listado_estudiantes[usuario])
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
        except Exception as e:
            print(e)

    def registrar_usuario(self):
        self.ventana_registro = ControladorRegistro(self.lista_estudiantes, self)
        self.ventana_registro.show()
        self.hide()

    def abrir_ventana_principal(self, estudiante: Estudiante):
        self.ventana_principal = ControladorPrincipal(estudiante, self.lista_estudiantes, self.lista_docentes, self)
        self.ventana_principal.show()
        self.hide()
