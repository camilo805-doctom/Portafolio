import reflex as rx
import portafolio.estilos.estilos as estilos
from portafolio.estilos.estilos import tamaños
from portafolio.views.barra_nav import barra_nav
from portafolio.views.header import header
from portafolio.views.intereses import intereses
from portafolio.views.proyectos import proyectos
from portafolio.views.conociminetos import conocimientos
from portafolio.views.autor import autor
from portafolio.views.footer import footer
from portafolio.componentes.charmander import charmander

def index()-> rx.Component:
    return rx.box(
        barra_nav(),
        rx.center(
            rx.vstack(
                header(),
                intereses(),
                proyectos(),
                autor(),
                conocimientos(),
                footer(),
                charmander(),
                width="100%",
                spacing=tamaños.VERY_BIG.value
            )
        )
    )

app=rx.App(
    stylesheets=estilos.HOJASESTILO,
    style=estilos.ESTILO_BASE
)

app.add_page(
    index,
    title="Portafolio 2024 | Juan Camilo Muñoz Bautista.",
    description="Desarrollador, creador de contenido y amante de la tecnologia."

)

app.compile()