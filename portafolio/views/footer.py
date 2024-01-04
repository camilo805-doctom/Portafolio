import reflex as rx
import portafolio.constantes as constantes
import portafolio.estilos.estilos as estilos
from portafolio.estilos.estilos import tamaños, texto_colores

def footer()-> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Portafolio 2024.",
                font_size=tamaños.MEDIUM.value,
                margin_bottom=tamaños.ZERO.value
            ),
            rx.link(
                "Creado con esfuerzo y ",
                 rx.box(class_name="nes-icon is-small heart"),
                " a la programacion por Juan Camilo Muñoz Bautista.",
                href=constantes.CAMILO_URL,
                is_external= True,
                font_size=tamaños.MEDIUM.value,
                color=texto_colores.TERCIARIO.value
            ),
            align_items="start",
            spacing=tamaños.MEDIUM.value
        ),
        rx.spacer(),
        rx.box(class_name="nes-logo"),
        padding_bottom=tamaños.BIG.value,
        style=estilos.max_width_style,
        align_items="center"
    )