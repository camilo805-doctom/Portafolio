import reflex as rx
import portafolio.constantes as constantes
from portafolio.estilos.estilos import tamaños

def charmander() -> rx.Component:
    return rx.link(

        rx.vstack(
            rx.vstack(
                rx.span(
                    "Repo"
                ),
                rx.span(
                    "del portafolio."
                ),
                align_items="start",
                class_name="nes-balloon from-right is-dark",
                margin_bottom=tamaños.BIG.value
            ),
            rx.box(
                rx.span(
                    constantes.VERSION,
                    class_name="is-error"
                ),
                class_name="nes-badge"
            )
        ),
        rx.box(
            class_name="nes-charmander"
        ),
        href=constantes.PORTAFOLIO_URL,
        is_external=True,
        align_items="end",
        display="flex",
        margin_top=tamaños.ZERO.value
    )