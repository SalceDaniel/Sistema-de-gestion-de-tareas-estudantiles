from src.Modelo.Estudiante import Estudiante


class Validaciones:

    def validar_cedula(self, cedula):
        return (
                len(cedula) == 10
                and cedula.isdigit()
                and 1 <= int(cedula[:2]) <= 24
                and 0 <= int(cedula[2]) <= 6
                and (10 - sum([int(cedula[i]) * 2 - 9
                               if i % 2 == 0 and int(cedula[i]) * 2 > 9
                               else int(cedula[i]) * 2 if i % 2 == 0 else int(cedula[i])
                               for i in range(9)]) % 10) % 10 == int(cedula[-1])
        )

    def validar_usuario(self, listado_estudiantes, usuario):
        return str(usuario) not in listado_estudiantes

    def validar_correo(self, correo):
        return (
                correo.count("@") == 1 and
                len(correo.split("@")) == 2 and
                not any(correo.startswith(c) or correo.endswith(c) for c in ["@", ".", " "]) and
                "." in correo.split("@")[1]  # despues de la arroba al menos un punto
        )
    def validar_celular(self, celular):
        return celular.isdigit() and 7 <= len(celular) <= 10
