from src.Vista.VentanaAgregarTareas import Ui_frmAgregarTarea as VentanaModificarTarea
from src.Vista.VistaTablas import VistaTablas
from src.Controlador.ControladorAgregarSubTareas import ControladorAgregarSubTareas
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Validaciones import Validaciones
from src.Modelo.Asignatura import Asignatura
from src.Modelo.Tarea import Tarea
from src.Modelo.SubTarea import SubTarea
from PyQt6 import QtWidgets, QtCore


class ControladorModificarTarea(QtWidgets.QMainWindow, VentanaModificarTarea):
    actualizar_datos = QtCore.pyqtSignal()

    def __init__(self, estudiante: Estudiante, tarea: Tarea, lista_estudiantes: ListaEstudiantes, parent=None):
        super(ControladorModificarTarea, self).__init__(parent)
        self.ventana_agregar_sub_tarea = None
        self.ventana_anterior = parent
        self.tarea = tarea
        self.estudiante = estudiante
        self.lista_estudiantes = lista_estudiantes
        self.validador = Validaciones()
        self.vista_tablas = VistaTablas()

        self.setupUi(self)
        self.btnCrearTarea.clicked.connect(self.validar_campos)
        self.btnCancelar.clicked.connect(self.cancelar)

        self.btnCrearTarea.setText("Guardar Cambios")
        self.btnAgregarSubTarea.clicked.connect(self.agregar_sub_tarea)
        self.btnSubTareaCompletada.clicked.connect(self.sub_tarea_completada)
        self.lblAgregarTarea.setText("Modificar Tarea")
        self.setWindowTitle("::Sistema Gestión de Tareas:: Modificar Tarea")
        self.dtpFechaLimite.setDateTime(self.tarea.fecha_limite)
        self.txtTitulo.setText(tarea.titulo)
        self.rtxtDescripcion.setText(tarea.descripcion)
        self.listar_sub_tareas()

    def validar_campos(self):
        if len(self.txtTitulo.text()) < 5:
            QtWidgets.QMessageBox.warning(self, "Error", "El campo título debe contener al menos 5 caracteres.")
            return
        print("Registrando tarea")
        self.registrar_tarea()

    def registrar_tarea(self):
        try:
            fecha_vencimiento = self.dtpFechaLimite.dateTime().toPyDateTime()
            codigo_asignatura = self.cbxAsignatura.currentText().split(" - ")[0]
            if codigo_asignatura != self.tarea.codigo_asignatura:
                self.estudiante.modificar_tarea(self.tarea.codigo_tarea, "asignatura")(codigo_asignatura)
            if fecha_vencimiento != self.tarea.fecha_limite:
                self.estudiante.modificar_tarea(self.tarea.codigo_tarea, "fecha_limite")(fecha_vencimiento)
            if self.rtxtDescripcion.toPlainText() != self.tarea.descripcion:
                self.estudiante.modificar_tarea(self.tarea.codigo_tarea, "descripcion")(
                    self.rtxtDescripcion.toPlainText())
            if self.cbxPrioridad.currentText() != self.tarea.prioridad:
                self.estudiante.modificar_tarea(self.tarea.codigo_tarea, "prioridad")(self.cbxPrioridad.currentText())
            if self.txtTitulo.text() != self.tarea.titulo:
                self.estudiante.modificar_tarea(self.tarea.codigo_tarea, "titulo")(self.txtTitulo.text())
            if self.cbxEstadoActual.currentText() != self.tarea.estado_actual:
                self.estudiante.modificar_tarea(self.tarea.codigo_tarea, "estado")(self.cbxEstadoActual.currentText())

            QtWidgets.QMessageBox.about(self, "Modificado", "Cambios guardados correctamente")

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
        self.actualizar_datos.emit()
        self.ventana_anterior.show()
        super().closeEvent(event)

    def showEvent(self, event):
        self.actualizar_cbx_asignatura()
        try:
            self.cbxAsignatura.setCurrentIndex(self.estudiante.lista_asignaturas.index(
                self.estudiante.recuperar_asignatura(self.tarea.codigo_asignatura)))
            self.cbxPrioridad.setCurrentText(self.tarea.prioridad)
            self.cbxEstadoActual.setCurrentText(self.tarea.estado_actual)
        except Exception as e:
            print(e)
        super().showEvent(event)

    def agregar_sub_tarea(self):
        self.ventana_agregar_sub_tarea = ControladorAgregarSubTareas(self.tarea, self.estudiante,
                                                                     self.lista_estudiantes, self)
        self.ventana_agregar_sub_tarea.actualizar_datos.connect(self.listar_sub_tareas)
        self.ventana_agregar_sub_tarea.show()

    def listar_sub_tareas(self):
        self.vista_tablas.inicializar_tabla(self.jgdTablaSubTareas)
        self.lista_estudiantes.recuperar_datos()
        self.jgdTablaSubTareas.setColumnCount(4)  # Establece el número de columnas
        self.jgdTablaSubTareas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.jgdTablaSubTareas.setHorizontalHeaderLabels(["Código sub-tarea", "Fecha_límite",
                                                          "Titulo", "Estado Actual"])

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
                self.lista_estudiantes.actualizar_estudiante(self.estudiante)
