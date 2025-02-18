import reflex as rx
from ..ui.base import base_page
from .. import navigation 

class ContactState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data



@rx.page(route = navigation.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    # Welcome Page (Index)
    my_form= rx.form(
        rx.vstack(
            rx.input(
                name="first_name",
                placeholder="First Name", 
                required= True,   
                type ="text",                
            ),
            rx.input(
                name="last_name",
                placeholder="Last Name", 
                required= True,  
                type ="text",                 
            ),
            rx.text_area(
                name= "message",
                placeholder= "your message",
                required= True,
            ),
            rx.hstack(
                rx.checkbox("Checked", name="check"),
                rx.switch("Switched", name="switch"),
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit = ContactState.handle_submit,
        reset_on_submit=True,
    )

    my_child = rx.vstack(
            rx.heading("contact us", size="9"),
            my_form,
            spacing="5",
            justify="center",
            align = "center",
            min_height="85vh",
            id = "my-child",
        )
    return base_page(my_child)

