import reflex as rx
from ..ui.base import base_page
from .. import navigation 


@rx.page(route = navigation.routes.PRICING_ROUTE)
def pricing_page() -> rx.Component:
    # Welcome Page (Index)
        my_child = rx.vstack(
            rx.heading("Pricing us", size="9"),
            rx.text(
                "Something cool pricing us",                
            ),
            spacing="5",
            justify="center",
            align = "center",
            min_height="85vh",
            id = "my-child",
        )
        return base_page(my_child)
