import reflex as rx

from .. import contact
from .. import navigation
from ..ui.base import base_page


@rx.page(route = navigation.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    # Welcome Page (Index)
    my_form = rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                    name="first_name",
                    placeholder="First Name", 
                    required= True,   
                    type ="text", 
                    width = "100%",               
                ),
                 rx.input(
                    name="last_name",
                    placeholder="Last Name", 
                    required= True,  
                    type ="text",  
                    width = "100%",               
                ),
                width="100%",
            ),
            rx.input(
                name="email",
                placeholder="email", 
                required= True,  
                type ="email",   
                width = "100%",              
            ),           
            rx.text_area(
                name= "message",
                placeholder= "your message",
                required= True,
                width = "100%",
            ),
            rx.hstack(
                rx.checkbox("Checked", name="check"),
                rx.switch("Switched", name="switch"),
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit = contact.ContactState.handle_submit,
        reset_on_submit=True,
    )

    my_child = rx.vstack(
            rx.heading("contact us", size="9"),
            # rx.text(ContactState.timeleft_label),
            rx.cond(
                contact.ContactState.did_submit , contact.ContactState.thank_you ,""
            ), 
            #rx.cond(
            #    ContactState.did_submit , ContactState.form_data.to_string(),""
            #),
            rx.desktop_only(
                rx.box(
                    my_form,
                    id = "my-form-box",
                    width = "50vw",
                )
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    id = "my-form-box",
                    width = "75vw",
                )
            ),
            rx.mobile_only(my_form),
            spacing="5",
            justify="center",
            align = "center",
            min_height="85vh",
            id = "my-child",
        )
    return base_page(my_child)

  