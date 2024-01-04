import reflex as rx
import datetime
import portafolio.estilos.estilos as estilos
from portafolio.estilos.estilos import tamaños, colores
from portafolio.componentes.texto_cabezera import texto_cabezera

def autor()-> rx.Component:
    return rx.vstack(
        texto_cabezera(
            "coin",
            "Hola, este soy yo."
        ),
        rx.flex(
            rx.avatar(
                name="Juan Camilo Muñoz Bautista",
                size="2xl",
                src="AVATAR.jpg",
                bg=colores.PRIMERO.value,
                padding="2px",
                border="4px",
                border_color=colores.SECUNDARIO.value,
                margin_right=tamaños.SMALL.value,
                margin_bottom=tamaños.SMALL.value
            ),
            rx.vstack(
                rx.span(f"Tengo {edad()} años y estoy proximo a entrar a ingenieria de software y por el momento decidi estudiar programación."),
                rx.span("Espero poder iniciar mi vida laboral como programadór junior backend con un dominio intermedio del lenguaje Python."),
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing=tamaños.BIG.value,
            flex_direction=["column","column","column","row",]
        ),
        padding_top=tamaños.VERY_BIG.value,
        style=estilos.max_width_style
    )


def edad()-> int:
    return datetime.date.today().year-2004