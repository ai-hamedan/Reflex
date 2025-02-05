import reflex as rx

def footer() -> rx.Component:
    return rx.flex(
        rx.text("Copyright 2024, All rights reserved."),
        direction="row",
        spacing="4",
    )