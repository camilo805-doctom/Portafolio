import reflex as rx
import portafolio.constantes as constantes
import portafolio.estilos.estilos as estilos
from portafolio.componentes.texto_cabezera import texto_cabezera
from portafolio.estilos.estilos import texto_colores
from portafolio.componentes.button import button


def proyectos()-> rx.Component:
    return rx.vstack(
        texto_cabezera(
            "github",
            "Mis proyectos"
        ),
        rx.vstack(
            rx.hstack(
                rx.text("Un repaso rapido por mis proyectos."),
                align_items="start"
            ),
            button(
                "mis proyectos en Git-Hub",
                constantes.GITHUB_URL
            ),
            rx.text(
                "Traductor basico."
            ),
            rx.span(
                "Usando los servicios de google desarrolle un traductor el cual pide al usuario una frase o pablabra en ingles y la traduce al español."
            ),
            button(
                "ingresa al repositorio.",
                constantes.TRADUCTOR_URL
            ),
            rx.text(
                "Diccionario Basico."
            ),
            rx.span(
                "Este diccionario toma un glosario de palabras en las cuales el usuario puede solicitar para saber sus definiciones."
            ),
            button(
                "ingresa al repositorio.",
                constantes.DICCIONARIO_URL
            ),
            rx.text(
                "Calculadora Basica."
            ),
            rx.span(
                "Esta calculadora pregunta por un valor float y despues la operacion a realizar."
            ),
            button(
                "ingresa al repositorio.",
                constantes.CALCULADORA_URL
            ),
            rx.text(
                "Convertidor de Celsius a Fahrenheit."
            ),
            rx.span(
                "Esta convertidor pide dos valores uno en grado celsius y lo convierte a Fahrenheeit."
            ),
            button(
                "ingresa al repositorio.",
                constantes.CONVERTIDOR_URL
            ),
            rx.text(
                "Generador de correos."
            ),
            rx.span(
                "Solicita al usuario unos caracteres especificos con los cuales se le generara un correo con un subdominio aleatorio."
            ),
            button(
                "ingresa al repositorio.",
                constantes.GENERADOR_URL
            ),
            rx.text(
                "Generador de nombres."
            ),
            rx.span(
                "Dada una lista de nombres y apellidos este generador pregunta por el genero y da un nombre aleatorio según el caso."
            ),
            button(
                "Ingresa al repositorio.",
                constantes.GENERADORN_URL
            ),
            rx.text(
                "Pagina wed."
            ),
            rx.span(
                "Pagina wed para mi canal de twitch el cual lleva a enlaces de mis redes sociales entre otros."
            ),
            button(
                "ingresa al repositorio.",
                constantes.PAGINAWED_URL
            ),
            class_name="nes-container is-dark",
            align_items="start",
            width="100%",
        ),
        style=estilos.max_width_style
    )