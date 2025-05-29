class ConfiguracionNotificaciones:

    def __init__(self, correo):
        self.notificaciones_activas = False
        self.correo = correo
        self.notificar_retrasos = False
        self.notificar_proximas_a_vencer = False
        self.notificar_finalizadas = False
        self.dias_antes_vencer = 0
        self.horas_antes_vencer = 0
