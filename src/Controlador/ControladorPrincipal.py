from src.Controlador.ControladorEditarPerfil import ControladorEditarPerfil
from src.Vista.VentanaPrincipal import Ui_MainWindow as VentanaPrincipal
from src.Controlador.ControladorDocentes import ControladorDocentes
from src.Controlador.ControladorAsignaturas import ControladorAsignaturas
from src.Controlador.ControladorTareas import ControladorTareas
from src.Controlador.ControladorAcercaDe import ControladorAcercaDe
from src.Controlador.ControladorCalendario import ControladorCalendario
from src.Controlador.ControladorReportes import ControladorReportes
from src.Controlador.ControladorConfigurarNotificaciones import ControladorConfigurarNotificaciones
from src.Modelo.Estudiante import Estudiante
from src.Modelo.ListaDocentes import ListaDocentes
from src.Modelo.ListaEstudiantes import ListaEstudiantes
from src.Vista.VistaTablas import VistaTablas
from src.Controlador.ControladorEnvioNotificaciones import ControladorEnvioNotificaciones
from PyQt6 import QtWidgets


class ControladorPrincipal(QtWidgets.QMainWindow, VentanaPrincipal):
    def __init__(self, estudiante: Estudiante, lista_estudiantes: ListaEstudiantes, lista_docentes: ListaDocentes,
                 parent=None):
        super().__init__(parent)
        self.ventana_configura_notificaciones = None
        self.ventana_reportes = None
        self.ventana_calendario = None
        self.ventana_editar_perfil = None
        self.ventana_acerca_de = None
        self.ventana_tareas = None
        self.ventana_asignaturas = None
        self.ventana_docente = None
        self.lista_docentes = lista_docentes
        self.estudiante_actual = estudiante
        self.lista_estudiantes = lista_estudiantes
        self.ventana_anterior = parent
        self.vista_tablas = VistaTablas()
        self.controlador_envio_notificaciones = ControladorEnvioNotificaciones(self.estudiante_actual)

        self.setupUi(self)

        self.lblBienvenidaUsuario.setText("Bienvenido " +
                                          self.estudiante_actual.nombre + " " +
                                          self.estudiante_actual.apellido)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

        self.actionDocentes.triggered.connect(self.mostrar_ventana_docente)
        self.actionAsignaturas.triggered.connect(self.mostrar_ventana_asignaturas)
        self.actionTareas.triggered.connect(self.mostrar_ventana_tareas)
        self.actionAcercaDe.triggered.connect(self.mostrar_acerca_de)
        self.actionEditarPerfil.triggered.connect(self.mostrar_editar_perfil)
        self.actionCalendario.triggered.connect(self.mostrar_vista_calendario)
        self.actionReportes.triggered.connect(self.mostrar_ventana_reportes)
        self.actionNotificaciones.triggered.connect(self.mostrar_ventana_configuracion_notificaciones)

        self.actionDocentesMB.triggered.connect(self.mostrar_ventana_docente)
        self.actionAsignaturasMB.triggered.connect(self.mostrar_ventana_asignaturas)
        self.actionTareasMB.triggered.connect(self.mostrar_ventana_tareas)
        self.actionAcercaDeMB.triggered.connect(self.mostrar_acerca_de)
        self.actionEditarPerfilMB.triggered.connect(self.mostrar_editar_perfil)
        self.actionCalendarioMB.triggered.connect(self.mostrar_vista_calendario)
        self.actionReportesMB.triggered.connect(self.mostrar_ventana_reportes)
        self.actionNotificacionesMB.triggered.connect(self.mostrar_ventana_configuracion_notificaciones)
        self.actionCerrarSesionMB.triggered.connect(self.cerrar_sesion)

        try:
            mensaje = ""
            if estudiante.configuracion_notificaciones.notificaciones_activas:
                num_notificaciones, mensaje = self.controlador_envio_notificaciones.generar_mensaje()
            else:
                num_notificaciones = 0
            if num_notificaciones > 0:
                respuesta = QtWidgets.QMessageBox.question(
                    self, "Notificaciones Pendientes",
                    "Usted tiene: " + str(num_notificaciones) + " notificaciones pendientes" +
                    "\n¿Desea que se envie un correo con las notificaciones pendientes?"
                )
                if QtWidgets.QMessageBox.StandardButton.Yes == respuesta:
                    self.controlador_envio_notificaciones.notificar(
                        self.estudiante_actual.configuracion_notificaciones.correo, mensaje)
                    print(mensaje)
        except Exception as e:
            print(e)

    def cerrar_sesion(self):
        self.ventana_anterior.show()
        self.close()

    def closeEvent(self, event):
        self.ventana_anterior.show()
        super().closeEvent(event)

    def actualizar_nombre(self):
        self.lblBienvenidaUsuario.setText("Bienvenido " +
                                          self.estudiante_actual.nombre + " " +
                                          self.estudiante_actual.apellido)

    def mostrar_ventana_docente(self):
        self.ventana_docente = ControladorDocentes(self.estudiante_actual, self.lista_estudiantes,
                                                   self.lista_docentes, self)
        self.ventana_docente.show()

    def mostrar_ventana_asignaturas(self):
        self.ventana_asignaturas = ControladorAsignaturas(self.estudiante_actual, self.lista_estudiantes,
                                                          self.lista_docentes, self)
        self.ventana_asignaturas.show()

    def mostrar_ventana_tareas(self):
        clave = self.estudiante_actual.usuario
        self.lista_estudiantes.recuperar_datos()
        self.estudiante_actual = self.lista_estudiantes.listado_estudiantes[clave]
        self.ventana_tareas = ControladorTareas(self.estudiante_actual, self.lista_estudiantes, self)
        self.ventana_tareas.show()

    def mostrar_acerca_de(self):
        self.ventana_acerca_de = ControladorAcercaDe(self)
        self.ventana_acerca_de.show()

    def mostrar_editar_perfil(self):
        self.ventana_editar_perfil = ControladorEditarPerfil(self.estudiante_actual, self.lista_estudiantes, self)
        self.ventana_editar_perfil.actualizar_datos.connect(self.actualizar_nombre)
        self.ventana_editar_perfil.show()

    def mostrar_vista_calendario(self):
        self.ventana_calendario = ControladorCalendario(self.estudiante_actual, self.lista_estudiantes, self)
        self.ventana_calendario.show()

    def mostrar_ventana_reportes(self):
        self.ventana_reportes = ControladorReportes(self.estudiante_actual, self)
        self.ventana_reportes.show()

    def mostrar_ventana_configuracion_notificaciones(self):
        self.ventana_configura_notificaciones = ControladorConfigurarNotificaciones(
            self.estudiante_actual, self.lista_estudiantes, self)
        self.ventana_configura_notificaciones.show()
