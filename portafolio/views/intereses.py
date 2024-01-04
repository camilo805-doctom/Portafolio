import reflex as rx
import portafolio.constantes as constantes
import portafolio.estilos.estilos as estilos
from portafolio.estilos.estilos import texto_colores
from portafolio.componentes.button import button

def intereses()-> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Mis intereses",
                class_name="title",
                color=texto_colores.ACENTO.value
                ),
            rx.span("• Como desarrollador quisiera dar soluciones rapidas a problemas que parecen dificiles."),
            rx.span("• El ambito tecnologico siempre me ha llamado la atencion desde pequeño cuando inicie con una pc con Windows XP."),
            rx.span("• A la par tambien soy creador de contenido en la plataforma de Twitch donde de vez en cuando instruyo a la comunidad en cosas de programacion."),
            rx.span("• Tambien soy apasionado a los videojuegos actuales como retros y tambien a la tecnologia antigua."),
            button(
                "Instagram",
                constantes.INSTAGRAM_URL
            ),
            class_name="nes-container is-dark with-title",
            align_items="start",
            width="100%",
        ),
        style=estilos.max_width_style
    )