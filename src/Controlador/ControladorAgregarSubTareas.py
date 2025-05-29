from src.Vista.VentanaAgregarSubTarea import Ui_frmAgregarSubTarea as VentanaAgregarSubTarea
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Tarea import Tarea

from PyQt6 import QtWidgets, QtCore


class ControladorAgregarSubTareas(QtWidgets.QMainWindow, VentanaAgregarSubTarea):
    actualizar_datos = QtCore.pyqtSignal()

    def __init__(self, tarea: Tarea, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes, parent=None):
        super(ControladorAgregarSubTareas, self).__init__(parent)
        self.ventana_anterior = parent
        self.tarea = tarea
        self.estudiante = estudiante
        self.lista_estudiantes = lista_estudiantes

        self.setupUi(self)
        self.btnAgregarSubTarea.clicked.connect(self.validar_campos)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.dtpFechaLimite.setDateTime(self.tarea.fecha_limite)

    def validar_campos(self):
        if len(self.txtTitulo.text()) < 5:
            QtWidgets.QMessageBox.warning(self, "Error", "El campo título debe contener al menos 5 caracteres.")
            return
        print("Registrando tarea")
        self.agregar_sub_tarea()

    def agregar_sub_tarea(self):
        try:
            fecha_vencimiento = self.dtpFechaLimite.dateTime().toPyDateTime()
            self.tarea.agregar_subtarea(self.txtTitulo.text(), self.rtxtDescripcion.toPlainText(),
                                        fecha_vencimiento)
            QtWidgets.QMessageBox.about(self, "Registrado",
                                        ("Sub-Tarea Registrada Correctamente." +
                                         "\nFecha límite:  \t " + fecha_vencimiento.strftime("%d-%m-%Y %H:%M") +
                                         "\nTítulo:        \t " + self.txtTitulo.text())
                                        )
            self.estudiante.actualizar_tarea(self.tarea)
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
