import reflex as rx
from web_app_with_reflex.components.navbar import navbar
from web_app_with_reflex.components.posts import post_list


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            post_list(
                
            ),
            class_name="main"
        ),
        class_name="page",
    )
