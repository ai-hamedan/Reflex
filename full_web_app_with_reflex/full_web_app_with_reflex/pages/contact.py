# import reflex as rx

# from .. import contact
# from .. import navigation
# from ..ui.base import base_page


# @rx.page(route = navigation.routes.CONTACT_US_ROUTE)
# def contact_page() -> rx.Component:
#     # Welcome Page (Index)
#     my_child = rx.vstack(
#             rx.heading("contact us", size="9"),
#             # rx.text(ContactState.timeleft_label),
#             rx.cond(
#                 contact.ContactState.did_submit , contact.ContactState.thank_you ,""
#             ), 
#             rx.desktop_only(
#                 rx.box(
#                     contact.contact_form(),
#                     width = "50vw",                   
#                 )
#             ),
#             rx.tablet_only(
#                 rx.box(
#                     contact.contact_form(),
#                     width = "75vw",
#                 )
#             ),
#             rx.mobile_only(
#                 rx.box(
#                     contact.contact_form(),
#                     width = '95vw'
#                 )
#             ),
#             spacing="5",
#             justify="center",
#             align = "center",
#             min_height="85vh",
#             id = "my-child",
#     )
    
#     return base_page(my_child)

  




         


