from src.Modelo.Validaciones import Validaciones
from src.Vista.VentanaNotificaciones import Ui_frmConfigurarNotificaciones as VentanaConfigurarNotificaciones
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Modelo.Estudiante import Estudiante
from PyQt6 import QtWidgets


class ControladorConfigurarNotificaciones(QtWidgets.QMainWindow, VentanaConfigurarNotificaciones):

    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes, parent=None):
        super(ControladorConfigurarNotificaciones, self).__init__(parent)
        self.ventana_anterior = parent
        self.lista_estudiantes = lista_estudiantes
        self.estudiante = estudiante
        self.validador = Validaciones()

        self.setupUi(self)
        self.cbxRecibirNotificaciones.setChecked(False)
        self.actualizar_configuracion()
        self.btnGuardarConfiguracion.clicked.connect(self.guardar_configuracion)
        self.cbxRecibirNotificaciones.stateChanged.connect(self.actualizar_estado_campos)
        self.btnRegresar.clicked.connect(self.close)

    def guardar_configuracion(self):
        if self.txtCorreo.text().strip() == "":
            QtWidgets.QMessageBox.warning(self, "Error", "Se debe ingresar un correo electrónico.")
            if not self.validador.validar_correo(self.txtCorreo.text()):
                QtWidgets.QMessageBox.warning(self, "Error", "Correo Ingresado es incorrecto")
                return

        self.estudiante: Estudiante
        self.estudiante.configuracion_notificaciones.notificar_retrasos = self.cbxTareasRetrasadas.isChecked()
        self.estudiante.configuracion_notificaciones.notificar_proximas_a_vencer = (
            self.cbxTareasProximas.isChecked())
        self.estudiante.configuracion_notificaciones.dias_antes_vencer = self.sbxDiasAntes.value()
        self.estudiante.configuracion_notificaciones.horas_antes_vencer = self.sbxHorasAntes.value()
        self.lista_estudiantes.actualizar_estudiante(self.estudiante)
        self.close()

    def closeEvent(self, event):
        self.ventana_anterior.show()
        super().closeEvent(event)

    def actualizar_configuracion(self):
        estado_notificaciones = self.estudiante.configuracion_notificaciones.notificaciones_activas
        self.cbxRecibirNotificaciones.setChecked(estado_notificaciones)
        self.habilitar_campos(estado_notificaciones)

        self.estudiante.configuracion_notificaciones.notificaciones_activas = self.cbxRecibirNotificaciones.isChecked()

        self.txtCorreo.setText(self.estudiante.configuracion_notificaciones.correo or self.estudiante.correo)
        self.sbxDiasAntes.setValue(self.estudiante.configuracion_notificaciones.dias_antes_vencer)
        self.sbxHorasAntes.setValue(self.estudiante.configuracion_notificaciones.horas_antes_vencer)
        self.cbxTareasProximas.setChecked(self.estudiante.configuracion_notificaciones.notificar_proximas_a_vencer)
        self.cbxTareasRetrasadas.setChecked(self.estudiante.configuracion_notificaciones.notificar_retrasos)

    def actualizar_estado_campos(self):
        estado = self.cbxRecibirNotificaciones.isChecked()
        self.habilitar_campos(estado)

        # Actualizar el estado de notificaciones en el objeto de configuración
        self.estudiante.configuracion_notificaciones.notificaciones_activas = estado

    def habilitar_campos(self, habilitar: bool):
        self.txtCorreo.setEnabled(habilitar)
        self.cbxTareasRetrasadas.setEnabled(habilitar)
        self.cbxTareasProximas.setEnabled(habilitar)
        self.sbxDiasAntes.setEnabled(habilitar)
        self.sbxHorasAntes.setEnabled(habilitar)
