import reflex as rx

def icono_link(icono:str, url:str)-> rx.Component:
    return rx.link(
        "",
        class_name=f"nes-icon {icono} is-medium",
        href=url,
        is_external=True
    )
