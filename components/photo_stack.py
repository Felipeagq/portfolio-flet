from flet import (
    UserControl,
    Stack,
    Container,
    border_radius,
    Text,
    Image,
    alignment
)
from flet.types import BoxShape

class PhotoStack(UserControl):
    def __init__(self,source):
        super().__init__()
        self.source = source
    
    def build(self):
        return Stack([
            Container(
            content=Image(
                    src=self.source,
                    width=500,
                    height=500,
                    border_radius=border_radius.all(100),
                    fit="fitWidth"
                ),
            shape=BoxShape.CIRCLE,
            width=500,
            height=500
        ),
            Container(
                content=Text("Hello!",color="white",size=25,weight="w900"),
                alignment=alignment.bottom_left,

            )
        ],
        width=300,
        height=300
)