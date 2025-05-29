from src.Vista.VentanaListarAsignaturas import Ui_frmListarAsignaturas as VentanaListarAsignaturas
from src.Controlador.ControladorAgregarAsignatura import ControladorAgregarAsignatura
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.ListaDocentes import ListaDocentes
from src.Modelo.Estudiante import Estudiante
from src.Modelo.Asignatura import Asignatura
from src.Vista.VistaTablas import VistaTablas
from PyQt6 import QtWidgets


class ControladorAsignaturas(QtWidgets.QMainWindow, VentanaListarAsignaturas):

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes,
                 lista_docentes: ListaDocentes, parent=None):
        super(ControladorAsignaturas, self).__init__(parent)
        self.ventana_anterior = parent
        self.ventana_agregar_asignatura = None
        self.estudiante = estudiante
        self.lista_estudiantes = lista_estudiantes
        self.lista_docentes = lista_docentes
        self.vista_tablas = VistaTablas()
        try:
            self.setupUi(self)
            self.btnAgregarAsignatura.clicked.connect(self.agregar_asignatura)
            self.btnRegresar.clicked.connect(self.regresar)
            self.btnModificarAsignatura.clicked.connect(self.modificar_asignatura)
            self.btnEliminarAsignatura.clicked.connect(self.eliminar_asignatura)
            self.listar_asignaturas()
        except Exception as e:
            print(e)

    def listar_asignaturas(self):
        self.lista_estudiantes.recuperar_datos()
        self.estudiante = self.lista_estudiantes.listado_estudiantes[self.estudiante.usuario]
        self.vista_tablas.inicializar_tabla(self.jgdTablaAsignaturas)

        self.jgdTablaAsignaturas.setColumnCount(3)
        self.jgdTablaAsignaturas.setHorizontalHeaderLabels(["Codigo", "Nombre", "Docente"])
        for asignatura in self.estudiante.lista_asignaturas:
            asignatura: Asignatura
            fila_actual = self.jgdTablaAsignaturas.rowCount()
            self.jgdTablaAsignaturas.insertRow(fila_actual)
            self.jgdTablaAsignaturas.setItem(fila_actual, 0, QtWidgets.QTableWidgetItem(asignatura.codigo_asignatura))
            self.jgdTablaAsignaturas.setItem(fila_actual, 1, QtWidgets.QTableWidgetItem(asignatura.nombre))

            self.jgdTablaAsignaturas.setItem(fila_actual, 2, QtWidgets.QTableWidgetItem(
                self.lista_docentes.obtener_docente(asignatura.codigo_docente).nombre + " " +
                self.lista_docentes.obtener_docente(asignatura.codigo_docente).apellido))

    def regresar(self):
        self.ventana_anterior.show()
        self.close()

    def agregar_asignatura(self):
        try:
            self.ventana_agregar_asignatura = ControladorAgregarAsignatura(self.estudiante, self.lista_estudiantes,
                                                                           self.lista_docentes, self)
            self.ventana_agregar_asignatura.show()
            self.ventana_agregar_asignatura.actualizar_datos.connect(self.listar_asignaturas)
        except Exception as e:
            print(e)

    def modificar_asignatura(self):
        if self.vista_tablas.obtener_dato_columa(self.jgdTablaAsignaturas, 0) is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar una fila a modificar.")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Aun no existe esta opcion.")

    def eliminar_asignatura(self):
        codigo_asignatura = self.vista_tablas.obtener_dato_columa(self.jgdTablaAsignaturas, 0)
        codigo_asignatura_predeterminado = "Ninguna"
        if codigo_asignatura is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar una asignatura a eliminar.")
        elif codigo_asignatura == codigo_asignatura_predeterminado:
            QtWidgets.QMessageBox.warning(self, "Error", "No es posible eliminar esta asignatura predeterminada.")
        else:
            respuesta = QtWidgets.QMessageBox.question(self, "Confirmación", "Seguro que desea eliminar la asignatura")
            if respuesta == QtWidgets.QMessageBox.StandardButton.Yes:
                self.estudiante.lista_asignaturas.remove(self.estudiante.recuperar_asignatura(codigo_asignatura))
                self.listar_asignaturas()
                self.lista_estudiantes.actualizar_estudiante(self.estudiante)
