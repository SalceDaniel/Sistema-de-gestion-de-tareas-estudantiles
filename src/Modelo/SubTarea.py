class SubTarea:

    def __init__(self, contador_subtarea, titulo, descripcion, fecha_limite, estado_actual="No finalizado"):
        self.codigo_subtarea = f"ST-{contador_subtarea:04d}"  # Código con formato ST-0001
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.estado_actual = estado_actual
