import reflex as rx
from web_app_with_reflex.state.post_state import PostState

def render_post(post:dict):
    return rx.box(
        rx.box(
            rx.link(
                    rx.heading(post["title"], size="5"),
                    href=f"/post/{post['uid']}",
                    on_click=PostState.select_post(post)
            ),
            rx.text(f"By: {post['author']}",class_name="post_author"),
            class_name="post_header",
        ),
        rx.box(
            rx.text(f"On date: {post['created_at']}", class_name="post_date"),
            rx.text(post["body"]),
            class_name="post_body",
        ),
        class_name="post",
    )

def post_list() -> rx.Component:
    return rx.box(
    rx.heading("Latest Posts",size="8"),
        rx.foreach(
            PostState.posts.reverse(),
            render_fn= render_post
        ),
        class_name="posts"
    )