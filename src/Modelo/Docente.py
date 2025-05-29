from src.Modelo.Persona import Persona


class Docente(Persona):
    def __init__(self, contador_docente, cedula, nombre, apellido, correo, celular):

        super().__init__(cedula, nombre, apellido, correo, celular)
        self.codigo_docente = f"D-{contador_docente:04d}"  # Código con formato D-0001

