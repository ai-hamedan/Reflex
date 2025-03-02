import reflex as rx
from typing import Optional, List
from sqlmodel import select
from .model import BlogPostModel

class BlogPostState(rx.State):
    posts : List['BlogPostModel'] = []
    Post : Optional ['BlogPostModel'] = None

    def load_posts(self):
        with rx.session() as session:
            result =  session.exec(
                select(BlogPostModel)
            ).all()
            self.posts = result
