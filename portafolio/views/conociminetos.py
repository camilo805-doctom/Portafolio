import reflex as rx
import portafolio.estilos.estilos as estilos
from portafolio.estilos.estilos import tamaños, colores
from portafolio.componentes.texto_cabezera import texto_cabezera

def conocimientos()-> rx.Component:
    return rx.vstack(
        rx.vstack(
            texto_cabezera(
                "trophy",
                "Mis conocimientos",
                False
            ),
            rx.text(
                "Al no estar en un universidad en un periodo corto de tiempo decidi estudiar programación de forma autodidacta aprendiendo desde cursos gratuitos, documentacion y hasta la ayuda de la propia comunidad."
            ),
            rx.text(
                "Por lo cual mis conocimientos estan en Pyhton un lenguaje del que propiamente sigo aprendiendo cada vez mas."
            ),
            spacing=tamaños.BIG.value,
            padding_y=tamaños.VERY_BIG.value,
            style=estilos.max_width_style
        ),
        bg=colores.ACENTO.value,
        width="100%"
    )