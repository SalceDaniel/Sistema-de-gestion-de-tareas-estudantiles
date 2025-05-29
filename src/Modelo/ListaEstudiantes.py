from src.Modelo.Estudiante import Estudiante
import pickle


class ListaEstudiantes:
    def __init__(self):
        self.listado_estudiantes: dict[str, Estudiante] = {}

    def registrar_estudiante(self, cedula, nombre, apellido, email, celular, usuario, password):
        if usuario in self.listado_estudiantes:
            print("El usuario ya existe. No se puede agregar.")
        else:
            self.listado_estudiantes[usuario] = Estudiante(
                cedula, nombre, apellido, email, celular, usuario, password
            )
            self.guardar_listado()
            print(f"Estudiante {usuario} registrado correctamente.")

    def guardar_listado(self):
        with open("listaEstudiantes.dat", "wb") as f:
            pickle.dump(self.listado_estudiantes, f, pickle.HIGHEST_PROTOCOL)
        print("Datos de estudiantes guardados correctamente.")

    def recuperar_datos(self):
        try:
            with open("listaEstudiantes.dat", "rb") as f:
                print("Datos de estudiantes recuperados exitosamente.")
                self.listado_estudiantes = pickle.load(f)
        except FileNotFoundError:
            print("Archivo \"listaEstudiantes.dat\" no encontrado. Creando uno nuevo.")
            self.guardar_listado()
        except Exception as e:
            print(f"Error al recuperar los datos: {e}")

    def login_estudiante(self, usuario, password_ingresada):
        if (usuario in self.listado_estudiantes.keys() and self.listado_estudiantes[usuario].contrasena
                == password_ingresada):
            return True

    def actualizar_estudiante(self, estudiante: Estudiante):
        if estudiante.usuario in self.listado_estudiantes:
            self.listado_estudiantes[estudiante.usuario] = estudiante
            print(f"Estudiante {estudiante.usuario} actualizado correctamente.")
            self.guardar_listado()
        else:
            print("El estudiante no existe. No se puede actualizar.")
