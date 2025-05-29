import datetime

from src.Modelo.Tarea import Tarea
from src.Modelo.Estudiante import Estudiante
from src.Vista.VentanaListarTareas import Ui_frmListarTareas as VentanaTareasCalendario
from src.Controlador.ControladorDetallesTarea import ControladorDetallesTarea
from src.Vista.VistaTablas import VistaTablas
from PyQt6 import QtWidgets, QtGui


class ControladorTareasCalendario(QtWidgets.QMainWindow, VentanaTareasCalendario):

    def __init__(self, estudiante: Estudiante, fecha_seleccionada: datetime.date, parent=None):
        super(ControladorTareasCalendario, self).__init__(parent)
        self.fecha_seleccionada = fecha_seleccionada
        self.ventana_anterior = parent
        self.ventana_mostrar_detalles = None
        self.estudiante_actual = estudiante
        self.vista_tablas = VistaTablas()

        self.setupUi(self)
        self.btnAgregarTarea.setVisible(False)
        self.btnEliminarTarea.setVisible(False)
        self.btnModificarTarea.setVisible(False)
        self.btnTareaCompletada.setVisible(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\../src/recursos/iconos/ver_actividades.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.btnTareaCompletada.setIcon(icon4)
        self.btnTareaCompletada.setText("Ver detalles")
        self.btnTareaCompletada.clicked.connect(self.mostrar_detalles)
        self.jgdTablaTareas.doubleClicked.connect(self.mostrar_detalles)
        self.btnRegresar.clicked.connect(self.regresar)
        self.lblListadoTareas.setText(self.fecha_seleccionada.strftime("Listado Tareas del: %d-%m-%Y"))

        try:
            self.listar_tareas()
        except Exception as e:
            print(e)

    def listar_tareas(self):
        tareas: list[Tarea] = self.estudiante_actual.listar_tareas_fecha(self.fecha_seleccionada)
        self.vista_tablas.inicializar_tabla(self.jgdTablaTareas)
        self.jgdTablaTareas.setColumnCount(7)  # Establece el número de columnas
        self.jgdTablaTareas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.jgdTablaTareas.setHorizontalHeaderLabels(["Código tarea", "Titulo", "Prioridad", "Asignatura",
                                                       "Estado Actual", "# Sub-Tareas", "Sub-Tareas Pendientes"])
        for tarea in tareas:
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

    def mostrar_detalles(self):

        if self.vista_tablas.obtener_dato_columa(self.jgdTablaTareas, 0) is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar una fila a modificar.")
        else:
            tarea = self.estudiante_actual.recuperar_tarea(self.vista_tablas.obtener_dato_columa(
                self.jgdTablaTareas, 0))
            self.ventana_mostrar_detalles = ControladorDetallesTarea(self.estudiante_actual, tarea, self)
            self.ventana_mostrar_detalles.show()
