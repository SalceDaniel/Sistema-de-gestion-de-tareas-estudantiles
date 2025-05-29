from src.Modelo.Docente import Docente
import pickle


class ListaDocentes:
    def __init__(self):
        self.listado_docentes: dict[str, Docente] = {}
        self.contador_docentes = 0
        self.DOCENTE_PREDETERMINADO = "D-0000"
        self.recuperar_datos()
        if self.DOCENTE_PREDETERMINADO not in self.listado_docentes:
            self.listado_docentes[self.DOCENTE_PREDETERMINADO] = Docente(
                0, "", "Sin", "Docente", "", ""
            )
            self.guardar_listado()  # Guarda la actualización

    def registrar_docente(self, cedula, nombre, apellido, correo, celular):
        self.contador_docentes += 1
        nuevo_docente = Docente(self.contador_docentes, cedula, nombre, apellido, correo, celular)
        self.listado_docentes[nuevo_docente.codigo_docente] = nuevo_docente
        self.guardar_listado()

    def guardar_listado(self):
        try:
            # Guarda tanto el listado de docentes como el contador
            with open("listaDocentes.dat", "wb") as f:
                pickle.dump({
                    "docentes": self.listado_docentes,
                    "contador": self.contador_docentes
                }, f, pickle.HIGHEST_PROTOCOL)
            print("Datos de docentes guardados correctamente.")
        except Exception as e:
            print("No se pudieron guardar los datos de docentes:", str(e))

    def recuperar_datos(self):
        try:
            with open("listaDocentes.dat", "rb") as f:
                datos_recuperados = pickle.load(f)
                self.listado_docentes = datos_recuperados.get("docentes", {})
                self.contador_docentes = datos_recuperados.get("contador", 0)
            print("Datos de docentes recuperados correctamente.")
        except FileNotFoundError:
            print("Archivo \"listaDocentes.dat\" no encontrado. Se inicializa la lista vacía.")
        except Exception as e:
            print("Error al recuperar datos de docentes:", str(e))

    def obtener_docente(self, codigo_docente):
        if codigo_docente in self.listado_docentes.keys():
            return self.listado_docentes[codigo_docente]
        else:
            print("Docente no registrado")

    def actualizar_docente(self, docente):
        if docente.codigo_docente in self.listado_docentes:
            self.listado_docentes[docente.codigo_docente] = docente
            self.guardar_listado()
        else:
            print("El docente no existe para ser actualizado.")

    def eliminar_docente(self, codigo_docente):
        if codigo_docente in self.listado_docentes:
            del self.listado_docentes[codigo_docente]
            self.guardar_listado()
        else:
            print("El docente no existe para ser eliminado.")
