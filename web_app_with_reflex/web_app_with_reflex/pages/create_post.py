import reflex as rx 
from web_app_with_reflex.components.navbar import navbar
from web_app_with_reflex.state.post_state import PostState


def create_post_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            
            rx.form(
                rx.heading("Create Post"),
                rx.box(
                    rx.text("Title", class_name="form-label"),
                    rx.input(
                        name="title",
                        placeholder="Enter Title",
                        type="text",
                        class_name="form-input",
                    ),
                    class_name="form-group",
                ),
                rx.box(
                    rx.text("Body", class_name="form-label"),
                    rx.text_area(
                        name="body",   
                        placeholder="Enter The Post Body",
                        class_name="form-input",
                    ),
                    class_name="form-group",
                ),
                rx.box(
                    rx.button("Save Post", type="submit"),
                    class_name="form-group",
                ),

                on_submit= PostState.create_post

            ),
            class_name="main",
        ),
        class_name="page",
    )