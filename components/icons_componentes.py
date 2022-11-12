from flet import (
    Row,
    Container,
    Image,
    border_radius,
    UserControl,
    padding
)

import requests

class IconComponents(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
    
    def build(self):
        return Row(
            [
                Container(
                    Image(src="/assets/instagram.png",),
                    width=50,
                    ink=True,
                    on_click= lambda e: self.page.launch_url("https://www.instagram.com/felipeagq_/")
                ),
                Container(
                    Image(src="/assets/linkedin.png"),
                    width=50,
                    on_click=lambda e: self.page.launch_url("https://www.linkedin.com/in/felipeagq/")
                ),
            ],
            alignment="center"
        )


class IconComponentsTwo(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
    
    def build(self):
        return Row(
            controls=[
                Container(
                    Row([
                        Container(
                            Image(src="/assets/instagram.png",),
                            width=50,
                            ink=True,
                            on_click= lambda e: self.page.launch_url("https://www.instagram.com/felipeagq_/")
                        ),
                        Container(
                            Image(src="/assets/linkedin.png"),
                            width=50,
                            on_click=lambda e: self.page.launch_url("https://www.linkedin.com/in/felipeagq/")
                        ),
                    ],
                        spacing=50),
                    padding=padding.only(top=200),
                ),
            ],
            alignment="center",
        )