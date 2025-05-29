from src.Vista.VentanaListarTareas import Ui_frmListarTareas as VentanaListarTareas
from src.Controlador.ControladorAgregarTareas import ControladorAgregarTareas
from src.Controlador.ControladorModificarTarea import ControladorModificarTarea
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Tarea import Tarea
from src.Modelo.Estudiante import Estudiante
from src.Vista.VistaTablas import VistaTablas
from PyQt6 import QtWidgets


class ControladorTareas(QtWidgets.QMainWindow, VentanaListarTareas):

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes, parent=None):
        super(ControladorTareas, self).__init__(parent)
        self.ventana_modificar_tarea = None
        self.ventana_anterior = parent
        self.ventana_agregar_tarea = None

        self.estudiante_actual = estudiante
        self.lista_estudiantes = lista_estudiantes
        self.vista_tablas = VistaTablas()

        self.setupUi(self)
        self.btnAgregarTarea.clicked.connect(self.agregar_tarea)
        self.btnRegresar.clicked.connect(self.regresar)
        self.btnModificarTarea.clicked.connect(self.modificar_tarea)
        self.btnEliminarTarea.clicked.connect(self.eliminar_tarea)
        self.btnTareaCompletada.setText("Tarea Completada")
        self.btnTareaCompletada.clicked.connect(self.tarea_completada)
        self.jgdTablaTareas.cellDoubleClicked.connect(self.modificar_tarea)
        self.listar_tareas()

    def listar_tareas(self):
        self.vista_tablas.inicializar_tabla(self.jgdTablaTareas)
        self.lista_estudiantes.recuperar_datos()
        self.jgdTablaTareas.setColumnCount(7)  # Establece el número de columnas
        self.jgdTablaTareas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.jgdTablaTareas.setHorizontalHeaderLabels(["Código tarea", "Titulo", "Prioridad", "Asignatura",
                                                       "Estado Actual", "# Sub-Tareas", "Sub-Tareas Pendientes"])

        for tarea in self.estudiante_actual.lista_tareas.values():
            tarea: Tarea
            fila_actual = self.jgdTablaTareas.rowCount()
            self.jgdTablaTareas.insertRow(fila_actual)
            self.jgdTablaTareas.setItem(fila_actual, 0, QtWidgets.QTableWidgetItem(tarea.codigo_tarea))
            self.jgdTablaTareas.setItem(fila_actual, 1, QtWidgets.QTableWidgetItem(tarea.titulo))
            self.jgdTablaTareas.setItem(fila_actual, 2, QtWidgets.QTableWidgetItem(tarea.prioridad))
            try:
                self.jgdTablaTareas.setItem(fila_actual, 3, QtWidgets.QTableWidgetItem(
                    self.estudiante_actual.recuperar_asignatura(tarea.codigo_asignatura).nombre))
            except Exception as e:
                print(e)
            self.jgdTablaTareas.setItem(fila_actual, 4, QtWidgets.QTableWidgetItem(tarea.estado_actual))
            self.jgdTablaTareas.setItem(fila_actual, 5, QtWidgets.QTableWidgetItem(str(len(tarea.lista_subtareas))))
            self.jgdTablaTareas.setItem(fila_actual, 6, QtWidgets.QTableWidgetItem(tarea.subtareas_pendientes()))

    def regresar(self):
        self.ventana_anterior.show()
        self.close()

    def agregar_tarea(self):
        self.ventana_agregar_tarea = ControladorAgregarTareas(self.estudiante_actual, self.lista_estudiantes, self)
        self.ventana_agregar_tarea.actualizar_datos.connect(self.listar_tareas)
        self.ventana_agregar_tarea.show()

    def eliminar_tarea(self):

        if self.vista_tablas.obtener_dato_columa(self.jgdTablaTareas, 0) is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar una tarea a eliminar.")
        else:
            respuesta = QtWidgets.QMessageBox.question(self, "Confirmación", "Seguro que desea eliminar la tarea")
            if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
                self.estudiante_actual.eliminar_tarea(self.vista_tablas.obtener_dato_columa(self.jgdTablaTareas, 0))
                self.listar_tareas()
                self.lista_estudiantes.actualizar_estudiante(self.estudiante_actual)

    def modificar_tarea(self):
        if self.vista_tablas.obtener_dato_columa(self.jgdTablaTareas, 0) is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar una fila a modificar.")
        else:
            tarea = self.estudiante_actual.recuperar_tarea(self.vista_tablas.obtener_dato_columa(
                self.jgdTablaTareas, 0))
            self.ventana_modificar_tarea = ControladorModificarTarea(self.estudiante_actual, tarea,
                                                                     self.lista_estudiantes, self)
            self.ventana_modificar_tarea.actualizar_datos.connect(self.listar_tareas)
            self.ventana_modificar_tarea.show()

    def tarea_completada(self):
        if self.vista_tablas.obtener_dato_columa(self.jgdTablaTareas, 0) is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar una tarea a marcar Finalizada")
        elif self.estudiante_actual.recuperar_tarea(
                self.vista_tablas.obtener_dato_columa(self.jgdTablaTareas, 0)).estado_actual == "Finalizada":
            QtWidgets.QMessageBox.warning(self, "Error", "Esta Tarea ya está Finalizada")
        else:
            respuesta = QtWidgets.QMessageBox.question(self, "Confirmación",
                                                       "Seguro que desea marcar la tarea como Finalizada")
            if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
                self.estudiante_actual.modificar_tarea(
                    self.vista_tablas.obtener_dato_columa(self.jgdTablaTareas, 0), "estado")("Finalizada")
                self.listar_tareas()
                self.lista_estudiantes.actualizar_estudiante(self.estudiante_actual)
