import reflex as rx
from .nav import navbar



def base_page(child: rx.Component, hide_navbar= False, *args, **kwargs )->rx.Component:
    # print([type(x) for x in args])
    if not isinstance(child, rx.Component):
        child = rx.heading("it is not child")
    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-right"), 
        )
    return rx.container(
        navbar(),        
        child,
        rx.logo(),
        rx.color_mode.button(position="bottom-right"), 
             
    )