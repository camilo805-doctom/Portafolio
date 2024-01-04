import reflex as rx
from enum import Enum
from .fuentes import Fuentes
from .colores import colores, texto_colores

MAX_WIDTH="1000px"

class tamaños(Enum):
    ZERO="0 !important"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"
    BUTTON="2.75em"
    VERY_BIG="4em"


HOJASESTILO=[
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]


ESTILO_BASE = {
    "font_family": Fuentes.DEFAULT.value,
    "background": colores.PRIMERO.value,
    "color": texto_colores.PRIMERO.value,
    rx.Heading:{
        "font_family": Fuentes.DEFAULT.value,
        "color":texto_colores.ACENTO.value

    },
    rx.Link:{
        "text_decoration":"none",
        "_hover":{
            "color":texto_colores.ACENTO.value,
            "text_decoration":"none"
        }
    },
    rx.Span:{
        "font_size":tamaños.MEDIUM.value
    },
    rx.Button:{
        "margin_bottom":tamaños.DEFAULT.value,
        "height":tamaños.BUTTON.value,
        "color":f"{texto_colores.SECUNDARIO.value} !important",
        "_hover":{
            "color":f"{texto_colores.PRIMERO.value} !important",
        }
    }

}


max_width_style=dict(
    align_items="center",
    padding_x=tamaños.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)
