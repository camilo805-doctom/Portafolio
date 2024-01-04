import reflex as rx
import portafolio.estilos.estilos as estilos
from portafolio.estilos.estilos import tamaños, texto_colores


def header()-> rx.Component:
    return rx.vstack(
        rx.heading(
            "Juan Camilo Muñoz Bautista",
            size="lg",
            padding_bottom=tamaños.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src="ash.png",
                alt="Imagen de ash en pixel art",
                width="16em",
                height="16em",
                margin_right=tamaños.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("Desarrollador junior del lenguaje Python."),
                    rx.text("Creador de contenido y amante de la tecnología."),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.span(
                    "Programador autodidacta por al rededor de 5 meses con el fin de buscar",
                    rx.span(
                        " soluciones innovadoras.",
                        color=texto_colores.ACENTO.value,
                        font_size=tamaños.DEFAULT.value
                    ),
                ),
                rx.span(
                    "La finalidad de este portafolio es dar a conocer mis habilidades como developer y mostrarme por primera vez a la comunidad."
                ),
                rx.span(
                    "Por ende mostrate mis avance a lo largo de estos meses con una pagina en estilo retro mostrando mi amor por tecnoloías pasadas y un recorrido por mis proyectos."
                ),
                align_items="start"
            ),
            flex_direction=["column","column","column", "row","row"]
        ),
        padding_top=tamaños.VERY_BIG.value,
        style=estilos.max_width_style

    )