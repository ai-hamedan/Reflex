
import reflex as rx
from web_app_with_reflex.components.navbar import navbar
from web_app_with_reflex.components.posts import post_list
from web_app_with_reflex.state.post_state import PostState
from web_app_with_reflex.components.update_modal import update_post_modal


def post_detail_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.box(
                rx.heading(PostState.post['title']),
                rx.text(f"By: {PostState.post['author']}"),
                rx.text(f"On: {PostState.post['created_at']}", class_name="date"),
                class_name="post_detail_header"
            ),
            rx.box(
                rx.text(PostState.post['body']),
                class_name="post_detail_body"
            ), 
            update_post_modal(),
            class_name="main"   
        ),

        
        class_name="page",
    )