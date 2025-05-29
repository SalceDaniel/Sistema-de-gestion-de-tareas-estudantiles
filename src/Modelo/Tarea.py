from datetime import datetime
from src.Modelo.SubTarea import SubTarea


class Tarea:

    def __init__(self, contador_tarea, titulo, prioridad, codigo_asignatura, estado_actual, descripcion, fecha_creacion,
                 fecha_limite):
        self.contador_sub_tarea = 0
        self.codigo_tarea = f"T-{contador_tarea:04d}"  # Código con formato T-0001
        self.titulo = titulo
        self.prioridad = prioridad
        self.codigo_asignatura = codigo_asignatura
        self.estado_actual = estado_actual
        self.descripcion = descripcion
        self.fecha_creacion: datetime = fecha_creacion
        self.fecha_limite: datetime = fecha_limite
        self.lista_subtareas: list[SubTarea] = []

    def agregar_subtarea(self, nombre, descripcion, fecha_limite):
        self.contador_sub_tarea += 1
        sub_tarea = SubTarea(self.contador_sub_tarea, nombre, descripcion, fecha_limite)
        self.lista_subtareas.append(sub_tarea)

    def recuperar_sub_tarea(self, codigo):
        for subtarea in self.lista_subtareas:
            if subtarea.codigo_subtarea == codigo:
                return subtarea
        return None

    def modificar_estado_sub_tarea(self, codigo_buscar: str, estado: str):
        for subtarea in self.lista_subtareas:
            if subtarea.codigo_subtarea == codigo_buscar:
                subtarea.estado_actual = estado

    def subtareas_pendientes(self):
        pendientes = 0
        for subtarea in self.lista_subtareas:
            if subtarea.estado_actual != "Finalizada":
                pendientes += 1
        return str(pendientes)
