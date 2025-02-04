"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from web_app_with_reflex.pages.home import index
from web_app_with_reflex.pages.create_post import create_post_page
from web_app_with_reflex.pages.post_detail import post_detail_page
from web_app_with_reflex.state.post_state import PostState


import reflex as rx


app = rx.App(
    stylesheets = [
        "/styles/main.css"
    ]
)

# Reflex automatically assigns the first page added as the index if no explicit / route is defined.
app.add_page(index,on_load=[
    PostState.load_posts
])

app.add_page(create_post_page, route="/create_post")

app.add_page(post_detail_page, route="/post/[uid]")