import reflex as rx

from ..components.footer import footer
from ..components.navbar import navbar

def template(page: rx.Component) -> rx.Component:
    return rx.flex(
        navbar(),
        page(),
        footer(),
        direction="column",
        spacing="4",
    )
