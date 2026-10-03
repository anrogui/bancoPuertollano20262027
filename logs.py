from datetime import datetime
import os


class Log:

    def __init__(self):
        fecha = datetime.now().strftime("%Y%m%d")
        self.ruta = f"log/{fecha}-banco.log"

        if not os.path.exists("log"):
            os.mkdir("log")

    def escribir(self, tipo, mensaje):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.ruta, "a") as fichero:
            fichero.write(f"[{fecha_hora}] [{tipo.upper()}] {mensaje}\n")

    def info(self, resumen_mensaje):
        self.escribir("INFO", resumen_mensaje)

    def error(self, mensaje_error):
        self.escribir("ERROR", mensaje_error)
