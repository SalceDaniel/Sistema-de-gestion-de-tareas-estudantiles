from src.Vista.VentanaAgregarTareas import Ui_frmAgregarTarea as VentanaModificarTarea
from src.Vista.VistaTablas import VistaTablas
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Tarea import Tarea
from src.Modelo.SubTarea import SubTarea
from PyQt6 import QtWidgets, QtCore


class ControladorDetallesTarea(QtWidgets.QMainWindow, VentanaModificarTarea):
    actualizar_datos = QtCore.pyqtSignal()

    def __init__(self, estudiante: Estudiante, tarea: Tarea, parent=None):
        super(ControladorDetallesTarea, self).__init__(parent)
        self.ventana_anterior = parent
        self.tarea = tarea
        self.estudiante = estudiante
        self.vista_tablas = VistaTablas()

        self.setupUi(self)
        self.btnCrearTarea.setVisible(False)
        self.btnCancelar.setVisible(False)
        self.btnAgregarSubTarea.setVisible(False)
        self.btnSubTareaCompletada.setVisible(False)
        self.btnEliminarSubTarea.setVisible(False)
        for widget in [
            self.txtTitulo,
            self.rtxtDescripcion,
            self.cbxEstadoActual,
            self.cbxAsignatura,
            self.cbxEstadoActual,
            self.cbxPrioridad,
            self.dtpFechaLimite
        ]:
            widget: QtWidgets
            widget.setEnabled(False)

        self.lblAgregarTarea.setText("Detalles de la Tarea")
        self.setWindowTitle("::Sistema Gestión de Tareas:: Detalles de la Tarea")
        self.dtpFechaLimite.setDateTime(self.tarea.fecha_limite)
        self.txtTitulo.setText(tarea.titulo)
        self.rtxtDescripcion.setText(tarea.descripcion)
        self.listar_sub_tareas()

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.actualizar_datos.emit()
        self.ventana_anterior.show()
        super().closeEvent(event)

    def showEvent(self, event):
        self.cbxAsignatura.addItem(self.tarea.codigo_asignatura + " - " +
                                   self.estudiante.recuperar_asignatura(self.tarea.codigo_asignatura).nombre)
        self.cbxPrioridad.setCurrentText(self.tarea.prioridad)
        self.cbxEstadoActual.setCurrentText(self.tarea.estado_actual)
        super().showEvent(event)

    def listar_sub_tareas(self):
        self.vista_tablas.inicializar_tabla(self.jgdTablaSubTareas)
        self.jgdTablaSubTareas.setColumnCount(4)  # Establece el número de columnas
        self.jgdTablaSubTareas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.jgdTablaSubTareas.setHorizontalHeaderLabels(["Código sub-tarea", "Fecha_límite", "Titulo", "Estado Actual"])

        for subtarea in self.tarea.lista_subtareas:
            subtarea: SubTarea
            fila_actual = self.jgdTablaSubTareas.rowCount()
            try:
                self.jgdTablaSubTareas.insertRow(fila_actual)
                self.jgdTablaSubTareas.setItem(fila_actual, 0, QtWidgets.QTableWidgetItem(subtarea.codigo_subtarea))
                self.jgdTablaSubTareas.setItem(fila_actual, 1, QtWidgets.QTableWidgetItem(
                    subtarea.fecha_limite.strftime("%d-%m-%Y %H:%M")))
                self.jgdTablaSubTareas.setItem(fila_actual, 2, QtWidgets.QTableWidgetItem(subtarea.titulo))
                self.jgdTablaSubTareas.setItem(fila_actual, 3, QtWidgets.QTableWidgetItem(subtarea.estado_actual))
            except Exception as e:
                print(e)

    def sub_tarea_completada(self):
        if self.vista_tablas.obtener_dato_columa(self.jgdTablaSubTareas, 0) is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar una tarea a marcar Finalizada")
        elif self.tarea.recuperar_sub_tarea(
                self.vista_tablas.obtener_dato_columa(self.jgdTablaSubTareas, 0)).estado_actual == "Finalizada":
            QtWidgets.QMessageBox.warning(self, "Error", "Esta Tarea ya está Finalizada")
        else:
            respuesta = QtWidgets.QMessageBox.question(self, "Confirmación",
                                                       "Seguro que desea marcar la tarea como Finalizada")
            if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
                self.tarea.modificar_estado_sub_tarea(
                    self.vista_tablas.obtener_dato_columa(self.jgdTablaSubTareas, 0), "Finalizada")
                self.listar_sub_tareas()
