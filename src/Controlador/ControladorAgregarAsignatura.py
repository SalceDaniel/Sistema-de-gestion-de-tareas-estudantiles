from src.Vista.VentanaAgregarAsignatura import Ui_frmAgregarAsignatura as VentanaAgregarAsignatura
from src.Modelo.ListaDocentes import ListaDocentes
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Docente import Docente
from PyQt6 import QtWidgets, QtCore


class ControladorAgregarAsignatura(QtWidgets.QMainWindow, VentanaAgregarAsignatura):
    actualizar_datos = QtCore.pyqtSignal()

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes,
                 lista_docentes: ListaDocentes, parent=None):
        super(ControladorAgregarAsignatura, self).__init__(parent)
        self.ventana_anterior = parent
        self.estudiante = estudiante
        self.lista_docentes = lista_docentes
        self.lista_estudiantes = lista_estudiantes

        self.setupUi(self)
        self.btnAgregar.clicked.connect(self.validar_campos)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.actualizar_cbx_docentes()

    def validar_campos(self):
        if '-' in self.txtCodigoAsignatura.text():
            QtWidgets.QMessageBox.warning(self, "Error", "El código de la asignatura no puede contener el simbolo\"-\".")
            return
        if len(self.txtCodigoAsignatura.text()) < 3:
            QtWidgets.QMessageBox.warning(self, "Error", "El código de la asignatura debe tener al menos 3 caracteres.")
            return
        if self.txtCodigoAsignatura.text().lower() in [tarea.codigo_asignatura.lower() for tarea in self.estudiante.lista_asignaturas]:
            QtWidgets.QMessageBox.warning(self, "Error", "El código se encuentra ocupado, ingrese otro. ")
            return
        self.registrar_asignatura()

    def registrar_asignatura(self):
        try:
            self.estudiante: Estudiante
            self.estudiante.agregar_asignatura(self.txtNombre.text(), self.txtCodigoAsignatura.text(),
                                               self.cbxDocente.currentText().split(" - ")[0])
            QtWidgets.QMessageBox.about(self, "Registrado", ("Asignatura registrada correctamente." +
                                                             "\nNombre: \t" + self.txtNombre.text() +
                                                             "\nCódigo: \t" + self.txtCodigoAsignatura.text()))
            self.lista_estudiantes.actualizar_estudiante(self.estudiante)
            self.actualizar_datos.emit()
            self.close()
        except Exception as e:
            print(e)

    def actualizar_cbx_docentes(self):
        self.cbxDocente.clear()
        for docente in self.lista_docentes.listado_docentes.values():
            docente: Docente
            self.cbxDocente.addItem(docente.codigo_docente + " - " + docente.nombre + " " + docente.apellido)

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.ventana_anterior.show()
        super().closeEvent(event)
