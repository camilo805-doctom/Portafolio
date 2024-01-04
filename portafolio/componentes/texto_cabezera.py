import reflex as rx
from portafolio.estilos.estilos import tamaños, texto_colores

def texto_cabezera(icono:str, text:str, negro=True)-> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"nes-icon is-large {icono}"
        ),
        rx.heading(
            text,
            size="md",
            color=texto_colores.ACENTO.value if negro else texto_colores.SECUNDARIO.value
        ),
        spacing=tamaños.DEFAULT.value,
        padding_bottom=tamaños.BUTTON.value
    )