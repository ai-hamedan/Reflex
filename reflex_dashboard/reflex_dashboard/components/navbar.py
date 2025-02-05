import reflex as rx


def navbar() -> rx.Component:
    return rx.flex(
        rx.link(rx.text("Home"), href="/"),
        rx.link(rx.text("Users"), href="/users"),
        direction="row",
        spacing="4",
    )