from src.Vista.VentanaAgregarTareas import Ui_frmAgregarTarea as VentanaAgregarTarea
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Validaciones import Validaciones
from src.Modelo.Asignatura import Asignatura
from PyQt6 import QtWidgets, QtCore
from datetime import datetime


class ControladorAgregarTareas(QtWidgets.QMainWindow, VentanaAgregarTarea):
    actualizar_datos = QtCore.pyqtSignal()

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes, parent=None):
        super(ControladorAgregarTareas, self).__init__(parent)
        self.ventana_anterior = parent
        self.estudiante = estudiante
        self.validador = Validaciones()

        self.setupUi(self)
        self.btnCrearTarea.clicked.connect(self.validar_campos)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.lista_estudiantes = lista_estudiantes
        self.dtpFechaLimite.setDateTime(QtCore.QDateTime.currentDateTime())
        self.actualizar_cbx_asignatura()
        self.jgdTablaSubTareas.setVisible(False)
        self.lblSubTareas.setVisible(False)
        self.btnAgregarSubTarea.setVisible(False)
        self.btnEliminarSubTarea.setVisible(False)
        self.btnSubTareaCompletada.setVisible(False)

    def validar_campos(self):
        if len(self.txtTitulo.text()) < 5:
            QtWidgets.QMessageBox.warning(self, "Error", "El campo título debe contener al menos 5 caracteres.")
            return
        print("Registrando tarea")
        self.registrar_tarea()

    def registrar_tarea(self):
        try:
            fecha_hora_actual = datetime.now()
            fecha_hora_formateada = fecha_hora_actual.strftime("%d-%m-%Y %H:%M")
            fecha_vencimiento = self.dtpFechaLimite.dateTime().toPyDateTime()
            codigo_asignatura = self.cbxAsignatura.currentText().split(" - ")[0]
            self.estudiante.agregar_tarea(self.txtTitulo.text(), self.cbxPrioridad.currentText(),
                                          codigo_asignatura, self.cbxEstadoActual.currentText(),
                                          self.rtxtDescripcion.toPlainText(),
                                          fecha_hora_actual, fecha_vencimiento)
            QtWidgets.QMessageBox.about(self, "Registrado",
                                        ("Tarea Registrada Correctamente." +
                                         "\nFecha creación: " + fecha_hora_formateada +
                                         "\nFecha límite:  \t " + fecha_vencimiento.strftime("%d-%m-%Y %H:%M")))

            self.lista_estudiantes.actualizar_estudiante(self.estudiante)
            self.actualizar_datos.emit()
            self.close()
        except Exception as e:
            print(e)

    def actualizar_cbx_asignatura(self):
        for asignatura in self.estudiante.lista_asignaturas:
            asignatura: Asignatura
            self.cbxAsignatura.addItem(asignatura.codigo_asignatura + " - " + asignatura.nombre)

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.ventana_anterior.show()
        super().closeEvent(event)

    def showEvent(self, event):
        self.cbxAsignatura.clear()
        self.actualizar_cbx_asignatura()
        super().showEvent(event)
