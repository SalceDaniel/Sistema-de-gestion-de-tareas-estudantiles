from src.Vista.VentanaCalendario import Ui_frmCalendario as VentanaCalendario
from src.Controlador.ControladorTareasCalendario import ControladorTareasCalendario
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Tarea import Tarea
from PyQt6 import QtWidgets
from PyQt6.QtGui import QColor, QTextCharFormat, QBrush


class ControladorCalendario(QtWidgets.QMainWindow, VentanaCalendario):

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes, parent=None):
        super(ControladorCalendario, self).__init__(parent)
        self.ventana_tareas_calendario = None
        self.fecha_seleccionada = None
        self.ventana_anterior = parent

        self.estudiante_actual = estudiante
        self.lista_estudiantes = lista_estudiantes

        self.setupUi(self)
        self.btnRegresar.clicked.connect(self.regresar)
        self.llenar_calendario()
        self.dtpCalendario.selectionChanged.connect(self.on_selection_changed)
        self.btnVerEventos.clicked.connect(self.ver_tareas_calendario)
        self.on_selection_changed()

    def regresar(self):
        self.ventana_anterior.show()
        self.close()

    def llenar_calendario(self):
        formato = QTextCharFormat()
        formato.setBackground(QBrush(QColor(0, 255, 0)))
        formato.setForeground(QBrush(QColor(0, 0, 0)))
        lista_tareas: list[Tarea] = list(self.estudiante_actual.lista_tareas.values())
        for tarea in lista_tareas:
            self.dtpCalendario.setDateTextFormat(tarea.fecha_limite, formato)

    def on_selection_changed(self):
        try:
            self.fecha_seleccionada = self.dtpCalendario.selectedDate().toPyDate()
            lista_tareas: list[Tarea] = list(self.estudiante_actual.lista_tareas.values())
            for tarea in lista_tareas:
                if tarea.fecha_limite.date() == self.fecha_seleccionada:
                    self.btnVerEventos.setEnabled(True)
                    break
                else:
                    self.btnVerEventos.setEnabled(False)
        except Exception as e:
            print(e)

    def ver_tareas_calendario(self):
        self.ventana_tareas_calendario = ControladorTareasCalendario(
            self.estudiante_actual, self.fecha_seleccionada, self)
        self.ventana_tareas_calendario.show()
