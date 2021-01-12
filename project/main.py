# coding=utf-8

import sys
# Para las expresiones regulares y procesar entradas de cadenas
from eliso import Eliso
# Para leer y escribir dentro del chat
from chat import Chat

__author__ = "Ariel Villeda"


def main(argv=None):
    try:
        log_name = None if len(argv) < 2 else argv[1]
    except IndexError:
        err = "Uso: {} <path/file_to_save_chat.txt>".format(argv[0])
        raise SystemExit(err)

    chat = Chat(log_name)
    eliso = Eliso()  # para procesar cadenas leidas

    chat.beginChat()  # inicializamos lo necesario para comenzar Chat
    while not chat.finalized:
        line = chat.readLine()
        eliso.processExp(string=line)

        # Continuamos segun el resultado del procesamiento del string
        # y las expRegulares
        flag = eliso.exp_matched.flag
        if flag == "despedida":
            response = eliso.exp_matched.random_response
            chat.writeLine(response.format(**eliso.match.groupdict()))
            chat.endChat()
        elif flag == "nombre":
            response = eliso.exp_matched.random_response
            chat.person_name = eliso.match.group("nombre")
            chat.writeLine(response.format(**eliso.match.groupdict()))
        elif flag == "noMatch":
            response = eliso.exp_matched.random_response
            chat.writeLine(response)
        elif flag == "toReflect":
            response = eliso.exp_matched.random_response
            chat.writeLine(
                response.format(
                    *[eliso.reflect(g) for g in eliso.match.groups()]
                )
            )
        else:
            response = eliso.exp_matched.random_response
            chat.writeLine(response.format(**eliso.match.groupdict()))
    # end while not chat.finalized
    return


if __name__ == "__main__":
    main(sys.argv)
