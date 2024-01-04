import reflex as rx
import portafolio.constantes as constantes
from portafolio.estilos.estilos import tamaños,colores
from portafolio.componentes.icono_link import icono_link



def barra_nav()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="ash.png",
                alt="imagen de ash en pixel art",
                width=tamaños.VERY_BIG.value,
                height=tamaños.VERY_BIG.value
            ),
            rx.text("Portafolio de trabajo 2024"),
            rx.spacer(),
            icono_link(
                "github",
                constantes.GITHUB_URL
            ),
            icono_link(
                "linkedin",
                constantes.LINKEDLN_URL
            ),
            icono_link(
                "instagram",
                constantes.INSTAGRAM_URL
            ),
            width="100%"
        ),
        bg=colores.PRIMERO.value,
        position="sticky",
        border_bottom=f"0.25em solid {colores.SECUNDARIO.value} ",
        padding_x=tamaños.BIG.value,
        padding_y=tamaños.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )