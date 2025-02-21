from datetime import datetime,timezone
import asyncio
import reflex as rx
from ..ui.base import base_page
from .. import navigation 
from sqlmodel import Field
import sqlalchemy



def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ContactEntryModel(rx.Model , table= True):
    first_name: str
    last_name: str | None = None
    email: str | None = None # = Field(Nullable= True)
    message: str
    created_at: datetime = Field(
        default_factory = get_utc_now, 
        sa_type = sqlalchemy.DateTime(timezone = True), 
        sa_column_kwargs ={
            'server_default': sqlalchemy.func.now()
        },
        nullable = False 
    )

class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    timeleft: int = 5

    #@rx.var
    #def timeleft_label(self) -> str:
    #    if self.timeleft < 1 :
    #        return "no time left"
    #    return f"{self.timeleft} seconds"
    

        # we don't have first_name in ContactState but we have it in dict of form
    @rx.var
    def thank_you(self) ->  str :
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + "!"
    

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        data = {}
        for k , v in form_data.items():
            if v == "" or v is None:
                continue
            data[k]=v

        with rx.session() as session:
            db_entry = ContactEntryModel(
                **form_data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            #sleep
            yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield


    #async def start_timer(self):
    #    while self.timeleft > 0 :
    #        await asyncio.sleep(1)
    #        self.timeleft -= 1
    #        yield

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
        on_submit = ContactState.handle_submit,
        reset_on_submit=True,
    )

    my_child = rx.vstack(
            rx.heading("contact us", size="9"),
            # rx.text(ContactState.timeleft_label),
            rx.cond(
                ContactState.did_submit , ContactState.thank_you ,""
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

