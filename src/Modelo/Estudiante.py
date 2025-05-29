import datetime

from src.Modelo.Persona import Persona
from src.Modelo.Tarea import Tarea
from src.Modelo.Asignatura import Asignatura
from src.Modelo.Docente import Docente
from src.Modelo.ConfiguracionNotificaciones import ConfiguracionNotificaciones


class Estudiante(Persona):

    def __init__(self, cedula, nombre, apellido, correo, celular,
                 usuario, contrasena):
        super().__init__(cedula, nombre, apellido, correo, celular)
        self.contador_tarea = 0
        self.contrasena = contrasena
        self.usuario = usuario
        self.lista_tareas: dict[str, Tarea] = {}
        self.lista_asignaturas: list[Asignatura] = []
        self.lista_docentes_estudiante: dict[str, Docente] = {}
        self.configuracion_notificaciones = ConfiguracionNotificaciones(correo)
        self.lista_asignaturas.append(Asignatura("Ninguna", "Ninguna", "D-0000"))
        self.lista_docentes_estudiante["D-0000"] = Docente(0, "", "Sin", "Docente", "", "")

    def agregar_tarea(self, titulo, prioridad, codigo_asignatura, estado_actual, descripcion,
                      fecha_creacion, fecha_limite):
        self.contador_tarea += 1
        tarea_nueva = Tarea(self.contador_tarea, titulo, prioridad, codigo_asignatura, estado_actual, descripcion,
                            fecha_creacion, fecha_limite)
        self.lista_tareas[tarea_nueva.codigo_tarea] = tarea_nueva

    def eliminar_tarea(self, codigo_tarea):
        del self.lista_tareas[codigo_tarea]

    def modificar_tarea(self, codigo_tarea, campo):
        def modificar_titulo(titulo_nuevo):
            self.lista_tareas[codigo_tarea].titulo = titulo_nuevo

        def modificar_fecha_limite(fecha_limite_nueva):
            self.lista_tareas[codigo_tarea].fecha_limite = fecha_limite_nueva

        def modificar_descripcion(descripcion_nueva):
            self.lista_tareas[codigo_tarea].descripcion = descripcion_nueva

        def modificar_prioridad(prioridad_nueva):
            self.lista_tareas[codigo_tarea].prioridad = prioridad_nueva

        def modificar_asignatura(asignatura_nueva):
            self.lista_tareas[codigo_tarea].codigo_asignatura = asignatura_nueva

        def modificar_estado(estado_nuevo):
            self.lista_tareas[codigo_tarea].estado_actual = estado_nuevo

        modificaciones = {
            "titulo": modificar_titulo,
            "fecha_limite": modificar_fecha_limite,
            "descripcion": modificar_descripcion,
            "prioridad": modificar_prioridad,
            "asignatura": modificar_asignatura,
            "estado": modificar_estado
        }
        if codigo_tarea in self.lista_tareas.keys():
            return modificaciones[campo]
        else:
            return None

    def listar_tareas_fecha(self, fecha_limite: datetime.date):
        if self.lista_tareas:
            return [
                tarea_actual for tarea_actual in self.lista_tareas.values()
                if tarea_actual.fecha_limite.date() == fecha_limite
            ]
        else:
            return []  # Retorna una lista vacía si no hay tareas

    def agregar_asignatura(self, nombre_asignatura, codigo_asignatura, codigo_docente):
        self.lista_asignaturas.append(Asignatura(nombre_asignatura, codigo_asignatura, codigo_docente))

    def agregar_docente(self, codigo_docente, nuevo_docente):
        self.lista_docentes_estudiante[codigo_docente] = nuevo_docente

    def recuperar_asignatura(self, codigo):
        for asignatura in self.lista_asignaturas:
            if asignatura.codigo_asignatura == codigo:
                return asignatura
        return Asignatura("Ninguna", "Ninguna", "D-0000")

    def recuperar_tarea(self, codigo):
        for tarea in self.lista_tareas.values():
            if tarea.codigo_tarea == codigo:
                return tarea
        return None

    def actualizar_tarea(self, tarea: Tarea):
        self.lista_tareas[tarea.codigo_tarea] = tarea

    def tareas_completadas_tiempo(self, fecha_inicio, fecha_fin, tipo_reporte):
        def filtrar_lista(campo, valor_comparar):
            tareas_filtradas = filter(
                lambda tarea: (
                        getattr(tarea, campo) == valor_comparar and
                        (
                                (fecha_inicio is None or fecha_fin is None)  # Sin restricción de fechas
                                or fecha_inicio <= tarea.fecha_limite.date() <= fecha_fin  # Con restricción de fechas
                        )
                ),
                self.lista_tareas.values()
            )
            return len(list(tareas_filtradas))

        def datos_asignaturas():
            return datos_general("codigo_asignatura",
                                 [asignatura.codigo_asignatura for asignatura in self.lista_asignaturas])

        def datos_prioridad():
            return datos_general("prioridad", ["Alta", "Media", "Baja"])

        def datos_estado():
            return datos_general("estado_actual", ["Finalizada", "No Finalizada"])

        def datos_general(campo, valores):
            etiquetas = []
            datos = []
            for valor in valores:
                if campo == "codigo_asignatura":
                    etiquetas.append(self.recuperar_asignatura(valor).nombre)
                else:
                    etiquetas.append(valor)
                datos.append(filtrar_lista(campo, valor))
            return etiquetas, datos

        lista_funciones = {
            "Asignatura": datos_asignaturas,
            "Prioridad": datos_prioridad,
            "Estado": datos_estado,
        }
        return lista_funciones[tipo_reporte]

    def eliminar_asignatura(self, codigo_asignatura):
        for asignatura in self.lista_asignaturas:
            if asignatura.codigo_asignatura == codigo_asignatura:
                self.lista_asignaturas.remove(asignatura)
            print(asignatura.codigo_asignatura + ":" + asignatura.codigo_docente)
        print(str(self.lista_asignaturas))

    def eliminar_docente(self, codigo_docente):
        del self.lista_docentes_estudiante[codigo_docente]
