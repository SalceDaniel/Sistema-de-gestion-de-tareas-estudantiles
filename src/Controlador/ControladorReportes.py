from PyQt6.QtGui import QStandardItemModel, QStandardItem

from src.Vista.VentanaReportes import Ui_frmReportes as VentanaReportes
from src.Modelo.Estudiante import Estudiante
from PyQt6 import QtWidgets, QtCore
from datetime import timedelta
from src.Controlador.ControladorGraficosReportes import GraficosReportes


class ControladorReportes(QtWidgets.QMainWindow, VentanaReportes):

    def __init__(self, estudiante: Estudiante, parent=None):
        super(ControladorReportes, self).__init__(parent)
        self.modelo_lista = QStandardItemModel()
        self.ventana_modificar_tarea = None
        self.ventana_anterior = parent
        self.ventana_agregar_tarea = None
        self.estudiante_actual = estudiante

        self.setupUi(self)
        self.dtpFechaInicial.setDate(QtCore.QDate.currentDate())
        self.btnRegresar.clicked.connect(self.regresar)
        self.cbxTipoReporte.addItems(["Semanal", "Mensual", "General"])
        self.cbxCriterio.addItems(["Estado", "Prioridad", "Asignatura"])
        self.cbxTipoReporte.currentIndexChanged.connect(self.inicializar_graficos)
        self.cbxCriterio.currentIndexChanged.connect(self.inicializar_graficos)
        self.dtpFechaInicial.dateChanged.connect(self.inicializar_graficos)
        self.inicializar_graficos()
        self.lstDatosReporte.setModel(self.modelo_lista)

    def regresar(self):
        self.ventana_anterior.show()
        self.close()

    def inicializar_graficos(self):
        layout = None
        try:
            # Asegurarse de que el layout del qWidgetGraficos existe
            layout = self.qWidgetGraficos.layout()
            if layout:  # Si existe un layout, eliminamos todos sus widgets
                while layout.count() > 0:
                    item = layout.takeAt(0)  # Tomar el primer elemento del layout
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()  # Eliminar el widget correctamente
            else:
                # Si no existe un layout, lo creamos
                from PyQt6.QtWidgets import QVBoxLayout
                layout = QVBoxLayout()
                self.qWidgetGraficos.setLayout(layout)
        except Exception as e:
            print(f"Error al limpiar widgets: {e}")

        controlador_reportes = GraficosReportes()
        fecha_inicio = self.dtpFechaInicial.date().toPyDate()
        if self.cbxTipoReporte.currentIndex() == 0:
            fecha_fin = fecha_inicio + timedelta(7)
            titulo = ("Reporte Semanal: \nDesde: " + fecha_inicio.strftime("%d-%m-%Y") +
                      "\nHasta: " + fecha_fin.strftime("%d-%m-%Y"))
        elif self.cbxTipoReporte.currentIndex() == 1:
            fecha_fin = fecha_inicio + timedelta(30)
            titulo = ("ReporteMensual: \nDesde: " + self.dtpFechaInicial.date().toPyDate().strftime("%d-%m-%Y") +
                      "\nHasta: " + fecha_fin.strftime("%d-%m-%Y"))
        else:
            fecha_fin = fecha_inicio = None
            titulo = "Reporte de todas las actividades"
        campo = self.cbxCriterio.currentText()
        etiquetas, valores_grafica = self.estudiante_actual.tareas_completadas_tiempo(fecha_inicio, fecha_fin, campo)()
        if valores_grafica.count(0) == len(valores_grafica):
            mensaje = QtWidgets.QLabel("No existe datos para: " + titulo, self)
            mensaje.setStyleSheet("font-size: 20px")
            mensaje.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(mensaje)
            self.modelo_lista.clear()
            self.lstDatosReporte.setVisible(False)
        else:
            chart_view = controlador_reportes.crear_grafico_circular(
                titulo,
                etiquetas,
                valores_grafica
            )
            # Agregar el nuevo chart_view al layout
            layout.addWidget(chart_view)
            # Lenar los datos en el lstView
            self.lstDatosReporte.setVisible(True)
            self.modelo_lista.clear()
            self.modelo_lista.appendRow(QStandardItem(titulo))
            for etiqueta, valor in zip(etiquetas, valores_grafica):
                texto = f"{etiqueta}: {valor}"
                item = QStandardItem(texto)
                self.modelo_lista.appendRow(item)
