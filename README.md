# Proyecto de conversación con Bot inteligente ELISO
Bot bastante sencillo elaborado en python, inspirado en el proyecto **sesentero** de J. Weizenbaum, [ELIZA - A Computer Program For the Study of Natural Language Communication Between Man And Machine](https://es.wikipedia.org/wiki/ELIZA) _Communications of the ACM, Vol 9, No 1, January 1966_.

Analiza el input escrito por el usuario y lo compara con una serie de expresiones regulares, anteriormente construidas, para tratar de encontrar o enetender el significado morfológico del enunciado y responder con una respuesta coherente.

Las respuestas que da el bot son algo **trolles** pero sin afán de ofender a alguien (_algunas pueden carecer de sentido, si lo que escribe el usuario no hace **match** con las expresiones regulares especificadas en el código_).
Ejemplo:
``` bash
Bienvenido al Chat
> hola
Hola, ¿te conozco?
> no sé
¡Qué negatividad la tuya!, ¿quién te hizo así?
```

Los logs de los chats, creados durante la ejecución del programa, se guardan automáticamente en la ruta `chat_logs/log_<timestamp>.chatlog`

### Requisitos:
- Python >=3

### Ejecución
``` bash
python project/main.py path/de-archivo-para-guardar-log.chatlog
```
_**El último argumento del comando (`path/...chatlog`) al final es opcional y se usa para especificar dónde guardar el log generado durante el chat**_