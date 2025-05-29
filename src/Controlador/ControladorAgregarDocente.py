from src.Vista.VentanaAgregarDocente import Ui_frmAgregarProfesor as VentanaAgregarDocente
from src.Modelo.ListaDocentes import ListaDocentes
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Validaciones import Validaciones
from PyQt6 import QtWidgets, QtCore


class ControladorAgregarDocentes(QtWidgets.QMainWindow, VentanaAgregarDocente):
    actualizar_datos = QtCore.pyqtSignal()

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes,
                 lista_docentes: ListaDocentes, parent=None):
        super(ControladorAgregarDocentes, self).__init__(parent)
        self.ventana_anterior = parent
        self.estudiante = estudiante
        self.lista_estudiantes = lista_estudiantes
        self.lista_docentes = lista_docentes
        self.validador = Validaciones()

        self.setupUi(self)
        self.btnAgregarDocente.clicked.connect(self.validar_campos)
        self.btnCancelar.clicked.connect(self.cancelar)

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
            self.lista_docentes.registrar_docente(self.txtCedula.text(), self.txtNombre.text(),
                                                  self.txtApellido.text(), self.txtEmail.text(),
                                                  self.txtCelular.text())
            QtWidgets.QMessageBox.about(self, "Registrado", ("Docente Registrado Correctamente." +
                                                             "\nNombre:   \t" + self.txtNombre.text() +
                                                             "\nApellido: \t" + self.txtApellido.text()))

            self.estudiante.agregar_docente(f"D-{self.lista_docentes.contador_docentes:04d}",
                                            self.lista_docentes.obtener_docente(self.txtCedula.text()))

            self.lista_estudiantes.actualizar_estudiante(self.estudiante)
            self.actualizar_datos.emit()
            self.close()
        except Exception as e:
            print(e)

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.ventana_anterior.show()
        super().closeEvent(event)
