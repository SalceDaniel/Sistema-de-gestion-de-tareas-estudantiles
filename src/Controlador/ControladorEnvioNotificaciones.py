import datetime
import math
import ssl
import smtplib

from src.Modelo.Estudiante import Estudiante
from email.message import EmailMessage


class ControladorEnvioNotificaciones:

    def __init__(self, estudiante: Estudiante):
        self.estudiante = estudiante

    def generar_mensaje(self):
        # Encabezado del correo
        mensaje = """
        <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; }
                    p { font-size: 14px; }
                    ul { list-style-type: none; padding: 0; }
                    li { margin: 10px 0; }
                </style>
            </head>
            <body>
                <h2>Notificación de Tareas</h2>
        """
        num_notificaciones = 0
        tareas_agregadas = False
        mensaje += "<h3>Tareas Atrasadas</h3><ul>"
        for tarea in self.estudiante.lista_tareas.values():
            # Tareas Retrasadas
            if self.estudiante.configuracion_notificaciones.notificar_retrasos:
                if tarea.fecha_limite <= datetime.datetime.now():
                    tiempo_retraso = datetime.datetime.now() - tarea.fecha_limite
                    num_notificaciones += 1
                    tareas_agregadas = True
                    mensaje += f"""
                        <li>
                            <strong>{tarea.titulo}</strong>: La fecha límite era el 
                            <strong>{tarea.fecha_limite.strftime('%d-%m-%Y %H:%M')}</strong>.
                            <br>Está retrasada por: <strong>{tiempo_retraso.days} días</strong> 
                            y <strong>{math.floor(tiempo_retraso.seconds / 3600)} horas</strong>.
                            <br> Asignatura: {self.estudiante.recuperar_asignatura(tarea.codigo_asignatura).nombre}.
                        </li>
                    """
        if not tareas_agregadas:
            mensaje += "<li>No hay tareas atrasadas.</li>"
        mensaje += "</ul>"

        mensaje += "<h3>Tareas Próximas a Vencer</h3><ul>"
        tareas_agregadas = False
        for tarea in self.estudiante.lista_tareas.values():
            if self.estudiante.configuracion_notificaciones.notificar_proximas_a_vencer:
                dias_aviso = self.estudiante.configuracion_notificaciones.dias_antes_vencer
                tiempo_restante = tarea.fecha_limite - datetime.datetime.now()
                if 0 <= tiempo_restante.days <= dias_aviso:
                    num_notificaciones += 1
                    tareas_agregadas = True
                    mensaje += f"""
                        <li>
                            <strong>{tarea.titulo}</strong>: La fecha límite es el 
                            <strong>{tarea.fecha_limite.strftime('%d-%m-%Y %H:%M')}</strong>.
                            <br>Le quedan: <strong>{tiempo_restante.days} días</strong> 
                            y <strong>{math.floor(tiempo_restante.seconds / 3600)} horas</strong>.
                            <br> Asignatura: {self.estudiante.recuperar_asignatura(tarea.codigo_asignatura).nombre}.
                        </li>
                    """
        if not tareas_agregadas:
            mensaje += "<li>No hay tareas próximas a vencer.</li>"
        mensaje += "</ul>"
        # Cierre del correo
        mensaje += """
                </ul>
                <p>Por favor, atienda las tareas lo antes posible.</p>
                <br>
                <p>Att. <br><em>::Sistema de Gestión de Tareas::</em></p>
            </body>
        </html>
        """
        return num_notificaciones, mensaje

    def notificar(self, correo_destino, texto_a_enviar):
        correo_envio = "Correo@ejemplo.com"
        clave_acceso = "aaaa aaaa aaaa aaaa"

        asunto = "Notificación de ::Sistema de Gestión de Tareas::"
        cuerpo = texto_a_enviar

        em = EmailMessage()
        em["From"] = correo_envio
        em["To"] = correo_destino
        em["Subject"] = asunto
        em.set_content(cuerpo)
        em.add_alternative(texto_a_enviar, subtype="html")  # Contenido HTML
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(correo_envio, clave_acceso)
                smtp.send_message(em)
                print("Correo enviado correctamente")
        except Exception as e:
            print("Error al enviar el correo:", e)
