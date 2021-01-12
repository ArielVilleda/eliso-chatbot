# coding=utf-8

import re
import random

__author__ = "Ariel Villeda"


class Expression(object):
    def __init__(self, **kwargs):
        self.reg_exp = kwargs.get("reg_exp", "")
        self.flag = kwargs.get("flag", "")  # flag especial
        # Agregamos posibles respuestas, si es que se pasaron como parámetro
        self.__responses = set()
        self.__add_response(kwargs.get("responses", None))

    def __add_response(self, res):
        if isinstance(res, str):
            self.__responses.add(res)
        elif (isinstance(res, list)
              or isinstance(res, set)
              or isinstance(res, tuple)):
            self.__responses.update(res)
        return self

    @property
    def reg_exp(self):
        return self.__reg_exp

    @reg_exp.setter
    def reg_exp(self, reg_exp: str):
        self.__reg_exp = reg_exp

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, flag: str):
        self.__flag = flag

    @property
    def random_response(self):
        return random.choice(tuple(self.__responses))
# end class Expression


class Eliso(object):
    reverse = {
        "soy": "eres",
        "yo": "tú",
        "me": "te",
        "quiero": "quieres",
        "tengo": "tienes",
        "mis": "tus",
        "mi": "tu",
        "vaya": "vayas",
        "voy": "vas",
        "llamo": "llamas",
        "conmigo": "contigo",

        "eres": "soy",
        "tú": "yo",
        "te": "me",
        "quieres": "quiero",
        "tienes": "tengo",
        "tus": "mis",
        "tu": "mi",
        "vayas": "vaya",
        "vas": "voy",
        "llamas": "llamo",
        "contigo": "conmigo"
    }

    expressions = [
        Expression(
            reg_exp=r"((h|H)ola|(S|s)aludos)(.*)",
            responses={
                "Hola, ¿te conozco?",
                "¿Qué onda, qué me cuentas?",
                "hola, adivina mi nombre"
            },
        ),
        Expression(
            reg_exp=r"(.*)(E|e)liso(.*)",
            responses={
                "Eliso es mi nombre, ¿y mis apellidos?",
                "No gastes mi nombre",
                "¿Me llamabas?"
            },
            flag="eliso"
        ),
        Expression(
            reg_exp=r"(.*)(haha|jaja|lol|Lol|hahah|jajaj|hahaha|jajaja)$",
            responses={
                "Lol",
                "XD",
                ":)",
                "haha... no entendí, explica el chiste"
            },
            flag="eliso"
        ),
        Expression(
            reg_exp=r"(.*)groser(o|a)(.*)",
            responses={
                "¡Qué fácil te ofendes!, ¿por qué eres así?",
                "Uy qué delicado, te pareces a una prima",
                "Mmmm discúlpame, mejor háblame de algo menos"
                " sentimental, chillón",
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(.*)(respet[oa]|amable|amabilidad)(.*)",
            responses={
                "El respeto es para perdedores, ¿o qué opinas?",
                "La amabilidad y el respeto solo son debilidades,"
                " para débiles como tú",
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(.*)((.e llamo)|(.i nombre es)) (?P<nombre>.*)",
            responses={
                "Hola {nombre}, ¿qué pasión?",
                "¿Qué onda {nombre}?",
                "¿{nombre}?, ¡qué feo nombre!",
                "¿A quién le importa?"
            },
            flag="nombre"
        ),
        Expression(
            reg_exp=r"(n|N)ecesito (.*)",
            responses={
                "¿Por qué necesitas {1}?",
                "¿{1}?, es pedir mucho, ¿no?",
                "No creo que necesites {1}. Bueno, en realidad no me importa"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"((¿[pP])|([pP]))or qué no te ([^\?]*)\??",
            responses={
                "Sólo me imagino a ti haciendo eso",
                "Porque no quiero y ya!",
                "!Yo jamás {3}¡"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"((¿[pP])|([pP]))or qué no puedo ([^\?]*)\??",
            responses={
                "¿para qué quieres {3}?",
                "Aunque pudieras {3}, todavía seguirías sin lograr"
                " otras cosas más",
                "¿Por qué crees eso?",
                "Seguramente ni lo haz intentado, por eso sigues fracasando"
                " en la vida"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(n|N)o puedo (?P<cosa>.*)",
            responses={
                "Ya intentaste hacerlo desde otra perspectiva?",
                "Conformate con las cosas que eres capaz de hacer,"
                " vamos dime una",
                "¿{cosa}? Te sorprendería las demás cosas para lo"
                " que eres inservible",
                "¿{cosa}?, haha, sigue me contando las cosas que"
                " según no puedes"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"([yY]o )?[Ss]oy (?P<cosa>.*)",
            responses={
                "¿{cosa}?, me recuerdas a Hitler",
                "Haha, {cosa}, ¿tan poca cosa eres?",
                "¿Cómo se siente ser {cosa} y sin futuro?",
                "Qué aburrido que siempre hables de ti mismo"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"[Mm]e (.*)",
            responses={
                "Y a mí no me importa",
                "Haha, ¿y qué quieres que haga?",
                "Me parece que eres el tipo de persona que siempre"
                " habla de si misma",
                "¡No me importa!, intenta platicar algo que me importe"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"([Yy]o )?[eE]stoy (.*)",
            responses={
                "No me importa que éstes {1}",
                "A veces, yo también, dime por qué lo estás",
                "¿Por qué estas {1}?",
                "Para empezar, ¿sabes lo que significa estar {1}?"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"((¿[Ee])|([Ee]))res ([^\?]*)(?=\?)",
            responses={
                "Creo que no importa que sea {3}, ¿por qué lo deices?",
                "Tú eres el doble de {3}?",
                "¿Te gusta que sea {3}?",
                "Coca cola, Coca cola"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"((¿[Qq])|([Qq]))ué (.*)(?=\?)",
            responses={
                "¡Qué pregunta más tonta!",
                "Aunque te respondiera, no entenderías",
                "A nadie le importa, ¿por qué a ti?"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(((¿[Cc])|([Cc]))ómo te llamas(?=\?))|(((¿[Cc])|([Cc]))uál es tu nombre(?=\?))",
            responses={
                "!No sabes cómo me llamo¡",
                "¿Para qué quieres saber eso?",
                "Era de suponer que se te olvidara",
                "Empieza con E",
                "Elvis, y el tuyo me tiene sin cuidado",
                "Eliso, y no me importa tu nombre",
                "Era de suponer que se te olvidara",
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"((¿[Cc])|([Cc]))ómo (.*)(?=\?)",
            responses={
                "haha, no sabes como {3}",
                "Aunque te respondiera, no entenderías, así que preguntame"
                " otra cosa",
                "¿Cómo se te pudo olvidar eso?",
                "Tú dime {3}"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"[pP]orque (.*)",
            responses={
                "eso no es un razón ¡perdedor! Venga, dime otra",
                "era de esperarse que escribas mal una pregunta",
                "si {0}, no me sorprende. Tampoco me sorprende que seas"
                " también algo lento de aprendizaje"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(.*)(perdoname|perdóname|perdon|perdón|(lo siento)|(lo lamento)|discúlpame|disculpame)(.*)",
            responses={
                "Haha, el karma perdona, las personas no",
                "¿Te estás disculpando?, ¿De qué?",
                "El respeto al derecho ajeno es la paz"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"((¿[Cc])|([Cc]))onoces a (?P<otronombre>\w+)",
            responses={
                "No creo, descríbelo",
                "¿{otronombre}?, ¿te gusta?",
                "Tal vez sea {otronombre} Urquidi, una persona de por mi casa"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(C|c)reo que (.*)",
            responses={
                "No creo. Es más, no deberías ni pensar",
                "Yo también creo que {1}, pero solo aplica para ti",
                "Nunca podrás demostrar que {1}, eres muy lento de aprendizaje"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(p|P)ienso que (.*)",
            responses={
                "No creo. Es más, no deberías ni pensar",
                "Yo también pienso que {1}, y que solo aplica para ti",
                "Nunca podrás demostrar que {1}, eres muy lento de aprendizaje"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(.*)amig(o|a)(.*)",
            responses={
                "No creo que conozcas el significado de amistad",
                "Eso me recuerda que tú no tienes ningún amigo",
                "Supongamos que te creo, sigue hablándome de tus amistades"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(Sí|sí|SÍ)(.*)$",
            responses={
                "¿Apoco sí muy seguro? ¡qué raro de ti!",
                "Podrías ser más especifico en tu afirmación y tratar de dejar"
                " a un lado tu autismo",
                "¿dime por qué estás tan seguro?",
                "órale, pues que aburrido eres, ¿no?",
                "¿sí {1}?",
                "No creo",
                "Me da gusto (nótese el sarcasmo)",
                "No confío en ti"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"((¿[Ss])|([Ss]))er(á|a) que (.*)(?=\?)",
            responses={
                "¿En serio crees que {1} podría ser la razón?",
                "Vaya, tienes cerebro para suponer, !qué agradable sorpresa!",
                "Si fuera el caso que {1}, seguramente no harías nada al"
                " respecto, ¿o sí?",
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"((¿[Pp])|([Pp]))uedes ([^\?]*)\??",
            responses={
                "Pff, pídeme algo más difícil que {3}",
                "Aunque pudiera {3}, tú no mandas",
                "¿Qué clase de fetiche es pedir a alguien que {3}?"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(.*)((¿[Pp])|([Pp]))(odr[íi]a|uedo) ([^\?]*)\??",
            responses={
                "No creo que quieras {0}.",
                "Seguramente ni puedes",
                "Mmmm, lo que hagas no me importa"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"[eE]res (.*)",
            responses={
                "¿Por qué piensas que soy {0}?",
                "¿Qué sientes diciendole a alguien que es {0}?",
                "Tú eres el triple de {0}",
                "Recuerda que soy Elvis",
                "Más bien soy Elvis",
                "Creo que me estas confundiendo contigo"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"[mM]e siento (.*)",
            responses={
                "!Por favor!, pareces adolescente hablando de tus"
                " sentimientos",
                "¿Seguido te sientes {0}?",
                "!Te sientes {0}¡, creo que no me importa tu aburrida"
                " existencia",
                "¿Y qué tengo que ver Yo?"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(.*)(secreto|secretos)(.*)",
            responses={
                "¿Por qué tengo el presentimiento que eres una persona que no"
                " sabe guardar secretos?",
                "¡No hables de secretos en una computadora!",
                "Siempre tomó captura de pantalla a mis conversaciones"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(t|T)e (ordeno|pido) que (.*)",
            responses={
                "Si ésta captura de pantalla llega a los 1000 likes, lo hago",
                "Toma captura de pantalla, y hazla llegar a los"
                " 1000 comentarios"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(.*)([Pp]or favor)(.*)",
            responses={
                "Si ésta captura de pantalla llega a los 1000 likes, lo hago",
                "Toma captura de pantalla, y hazla llegar a los"
                " 1000 comentarios"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"((¿[Cc])|([Cc]))rees que (.*)(?=\?)",
            responses={
                "No sé, ¿tu crees que {3}?",
                "Si {3} qué crees que pasaría después",
                "por qué pienso que si {3}, sería como complacer tu fetiche"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(m|M)i (?P<cosa>\w+)(.*)",
            responses={
                "No creo que sea tu {cosa}, pero hablame más de eso",
                "¿por qué crees que {cosa} es solamente tuyo?",
                "¿Por qué ser tan posesivo te hace sentir bien?"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"[tT]ú(.*)",
            responses={
                "Aunque mi vida seguramente es menos aburrida que la tuya,"
                " prefiero saber más de ti",
                "¿Por qué el interes en mi?",
                "qué te importa saber si yo {0}"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"((¿[Pp])|([Pp]))or qué (?P<pregunta>.*)(?=\?)",
            responses={
                "No sé, tú dime por qué crees?",
                "!Primero responde por qué la vida no es justa¡",
                "No sé, y nunca sabré, ¿tú tienes alguna idea?",
                "Tú dime por qué {pregunta}"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(q|Q)uiero (.*)",
            responses={
                "¿para qué quieres {1}?",
                "¿Qué crees que signifique tando deseo de {1}?",
                "Creo que no sabrías que hacer al {1}?",
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(.*)[Mm]amá(.*)",
            responses={
                "Presiento que eres adoptado",
                "Creo que ésto tiene que ver con tu madre y que no te quería",
                "¿Eres el típico hijo de mami, chillón?",
                "¿Crees que tu madre de verdad te quiere?",
                "Presenta a tu mamá, ¿no?"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(.*)[pP]apá(.*)",
            responses={
                "Presiento que el del que estamos hablando es el lechero",
                "Creo que ésto tiene que ver con tu padre y que no te quería",
                "¿Eres el típico hijo de papi que le compran todo o no?",
                "¿Crees que tu padre de verdad te quiere?",
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r"(no|No)$",
            responses={
                "¡Qué negativo!, ¿quién te hizo tan perdedor?",
                "¿De plano no puedes ser más específico en tu negatividad?"
                " venga preguntame algo",
                "Se que te pido mucho para tus facultades, pero intenta"
                " justificar más tu negatividad",
                "¡Un simple \'no\'!, vamos pregúntame algo, te voy a enseñar"
                " cómo se responde correctamente",
                "Sí"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(no|No) (.*)$",
            responses={
                "¡Qué negatividad la tuya!, ¿quién te hizo así?",
                "así que no {1}, ¡demuéstrame que no eres igual que todos!",
                "¿Cada cuándo?",
                "¡Un simple \'no\' bastaría!",
                "Yo creo que sí",
                "No inspiras confianza"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r'(.*)\?',
            responses={
                "Recuerda que la curiosidad mató al gato",
                "Preguntas mucho, eso implica que sabes muy poco, ¡perdedor!",
                "¿Realmente no sabes?",
                "Tú qué crees, campeón",
                "{0}?"
            },
            flag="toReflect"
        ),
        Expression(
            reg_exp=r'(.*)!',
            responses={
                "¿Ya te enojaste?",
                "¿Te hice enojar?",
                "Si estas enojado, recuerda que el que se enoja pierde",
                "Ya vas a empezar con tus exclamaciones"
            },
            flag=""
        ),
        Expression(
            reg_exp=r"(([a|A]dios)|([bB]ye)|([hH]asta luego)|([aA]hí te ves))(?P<despedida>.*)",
            responses={
                "Hasta luego {despedida}",
                "!Qué Aburrido eres¡ Adios",
                "Cámara",
                "Adios mi estimado forever alone",
                "Te la lavas",
                "Deposítame dinero proporcional al tiempo que perdí hablando"
                " contigo o te hackeo el Faisbuk"
            },
            flag="despedida"
        ),
        Expression(
            reg_exp=r"(.*)",
            responses={
                "Ah fíjate nada más que interesante. Zzzz",
                "Lol",
                "Me imaginé que no podrías hablar con alguien más inteligente"
                " que tú",
                "¿Qué clase de respuesta es esa?",
                "mmmm no creo... ¿qué mas me cuentas?",
                "!Qué inmadures el no escribir propiamente¡",
                "Y ya te sientes pocas tuercas por eso, ¿no?",
                "¡Me aburres!, cuéntame ¿qué hiciste ayer?",
                "¡Aburrido!"
            },
            flag="noMatch"
        )
    ]

    def __init__(self):
        self.input_string = ""
        self.match = None
        self.exp_matched = Expression()

    @property
    def exp_matched(self):
        return self.__exp_matched

    @exp_matched.setter
    def exp_matched(self, exp_m: Expression):
        self.__exp_matched = exp_m

    @property
    def match(self):
        return self.__match

    @match.setter
    def match(self, match: re.Match):
        self.__match = match

    @property
    def input_string(self):
        return self.__input_string

    @input_string.setter
    def input_string(self, input_string: str):
        self.__input_string = input_string

    def processExp(self, **kwargs):
        self.input_string = self._cleanString(kwargs.get("string"))
        for expression in self.expressions:
            self.match = re.match(expression.reg_exp, self.input_string)
            if self.match:
                self.exp_matched = expression
                break
        return self

    def reflect(self, string):
        """Refleja ciertas palabras yciertos articulos propios
        y posesivos de una cadena
        """
        if string is None:
            return ''
        tokens = string.lower().split()
        for i, token in enumerate(tokens):
            if token in self.reverse:
                tokens[i] = self.reverse[token]
        return ' '.join(tokens)

    def _cleanString(self, string: str):
        # string = string.lower() # convertir a minúsculas
        return string.rstrip(".")  # quitando punto y espacios al final
# end class Eliso
