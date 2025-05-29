from src.Vista.VentanaListarDocentes import Ui_frmListadoDocentes as VentanaListarDocentes
from src.Controlador.ControladorAgregarDocente import ControladorAgregarDocentes
from src.Controlador.ControladorModificarDocente import ControladorModificarDocente
from src.Modelo.ListaDocentes import ListaDocentes
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Docente import Docente
from src.Modelo.Estudiante import Estudiante
from src.Vista.VistaTablas import VistaTablas
from PyQt6 import QtWidgets


class ControladorDocentes(QtWidgets.QMainWindow, VentanaListarDocentes):

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes,
                 lista_docentes: ListaDocentes, parent=None):
        super(ControladorDocentes, self).__init__(parent)
        self.ventana_agregar_docente = None
        self.ventana_modificar_docente = None
        self.ventana_anterior = parent

        self.estudiante_actual = estudiante
        self.lista_docentes = lista_docentes
        self.lista_estudiantes = lista_estudiantes
        self.vista_tablas = VistaTablas()

        self.setupUi(self)
        self.jgdTablaDocentes.setEnabled(False)
        self.btnAgregarDocente.clicked.connect(self.agregar_docente)
        self.btnRegresar.clicked.connect(self.regresar)
        self.btnModificarDocente.clicked.connect(self.modificar_docente)
        self.btnEliminarDocente.clicked.connect(self.eliminar_docente_seleccionado)
        self.listar_docentes()

    def listar_docentes(self):
        self.vista_tablas.inicializar_tabla(self.jgdTablaDocentes)
        self.lista_docentes.recuperar_datos()
        self.jgdTablaDocentes.setColumnCount(6)  # Establece el número de columnas
        self.jgdTablaDocentes.setHorizontalHeaderLabels(["Codigo", "Nombre", "Apellido", "Celular",
                                                         "Email", "# Asignaturas"])
        for docente in self.lista_docentes.listado_docentes.values():
            docente: Docente
            fila_actual = self.jgdTablaDocentes.rowCount()
            self.jgdTablaDocentes.insertRow(fila_actual)
            self.jgdTablaDocentes.setItem(fila_actual, 0, QtWidgets.QTableWidgetItem(docente.codigo_docente))
            self.jgdTablaDocentes.setItem(fila_actual, 1, QtWidgets.QTableWidgetItem(docente.nombre))
            self.jgdTablaDocentes.setItem(fila_actual, 2, QtWidgets.QTableWidgetItem(docente.apellido))
            self.jgdTablaDocentes.setItem(fila_actual, 3, QtWidgets.QTableWidgetItem(docente.celular))
            self.jgdTablaDocentes.setItem(fila_actual, 4, QtWidgets.QTableWidgetItem(docente.correo))
            num_asignaturas = sum(
                1 for asignatura in self.estudiante_actual.lista_asignaturas
                if asignatura.codigo_docente == docente.codigo_docente
            )
            self.jgdTablaDocentes.setItem(fila_actual, 5, QtWidgets.QTableWidgetItem(str(num_asignaturas)))

    def regresar(self):
        self.ventana_anterior.show()
        self.close()

    def agregar_docente(self):
        self.ventana_agregar_docente = ControladorAgregarDocentes(self.estudiante_actual, self.lista_estudiantes,
                                                                  self.lista_docentes, self)
        self.ventana_agregar_docente.actualizar_datos.connect(self.listar_docentes)
        self.ventana_agregar_docente.show()

    def modificar_docente(self):
        try:
            if self.vista_tablas.obtener_dato_columa(self.jgdTablaDocentes, 0) is None:
                QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar una fila a modificar.")
            else:
                docente = self.lista_docentes.obtener_docente(self.vista_tablas.obtener_dato_columa(
                    self.jgdTablaDocentes, 0)
                )
                self.ventana_modificar_docente = ControladorModificarDocente(docente, self.lista_docentes, self)
                self.ventana_modificar_docente.show()
                self.ventana_modificar_docente.actualizar_datos.connect(self.listar_docentes)
        except Exception as e:
            print(e)

    def eliminar_docente_seleccionado(self):
        codigo_docente = self.vista_tablas.obtener_dato_columa(self.jgdTablaDocentes, 0)
        if codigo_docente is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar un docente a eliminar.")
            return
        respuesta = QtWidgets.QMessageBox.question(
            self,
            "Confirmación",
            "¿Seguro que desea eliminar el docente?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if respuesta != QtWidgets.QMessageBox.StandardButton.Yes:
            return

        docente_predeterminado = "D-0000"
        if codigo_docente == docente_predeterminado:
            QtWidgets.QMessageBox.warning(self, "Error", "No es posible eliminar este docente predeterminado.")
            return

        for asignatura in self.estudiante_actual.lista_asignaturas:
            if asignatura.codigo_docente == codigo_docente:
                asignatura.codigo_docente = docente_predeterminado

        self.lista_docentes.eliminar_docente(codigo_docente)
        self.listar_docentes()
        self.estudiante_actual.eliminar_docente(codigo_docente)
        self.lista_estudiantes.actualizar_estudiante(self.estudiante_actual)
