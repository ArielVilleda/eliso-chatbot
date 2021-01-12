# coding=utf-8

import time
import os

__author__ = "Ariel Villeda"


class Chat:
    def __init__(self, log_path: str = None):
        if not log_path:
            now = time.strftime("%Y%m%d%H%M%S")
            log_path = "chat_logs/log_{}.chatlog".format(now)
        self.openFile(log_path)
        self.finalized = False  # para saber si el chat ha finalizado
        self.writed = ""
        self.readed = ""
        self.person_name = ""

    @property
    def timestamp(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def person_name(self):
        return self.__person_name

    @person_name.setter
    def person_name(self, name: str):
        self.__person_name = name

    @property
    def finalized(self):
        return self.__finalized

    @finalized.setter
    def finalized(self, status: bool):
        self.__finalized = status

    def openFile(self, file):
        if not os.path.exists(os.path.dirname(file)):
            # Agregamos un bloque de "try" por si el directorio se
            # creace después del if anterior y previo a la ejecución
            # del comando makedirs
            try:
                os.makedirs(os.path.dirname(file))
            except OSError:
                raise SystemExit("Error en creación de directorio de log")
        self.file = open(file, "w")
        return self

    def closeFile(self):
        if self.file is not None:
            self.file.close()
        return self

    def beginChat(self):
        self.finalized = False
        line = "Bienvenido al Chat"
        self.writeLine(line)
        return self

    def endChat(self):
        self.finalized = True
        line = "Chat finalizado"
        self.writeLine(line)
        self.closeFile()  # cerrando el archivo de log
        return self

    def readLine(self):
        self.readed = input("> ")
        self.saveToFile(self.readed, author="Usuario", with_timestamp=True)
        return self.readed

    def writeLine(self, line: str):
        self.writed = line
        self.saveToFile(self.writed, author="Eliso", with_timestamp=True)
        time.sleep(2)  # esperamos antes de escribir en pantalla
        print(self.writed)
        return self

    def saveToFile(self, line: str, **kwargs):
        with_timestamp = kwargs.get("with_timestamp", False)
        author = kwargs.get("author", "")
        log = "{}\t>\t\t{}".format(author, line)
        log = "{} :: {}".format(self.timestamp, log) if with_timestamp else log
        print(log, file=self.file)
        return self
# end class Chat
