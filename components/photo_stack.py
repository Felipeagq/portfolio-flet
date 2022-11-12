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
                    width=100,
                    height=100,
                    border_radius=border_radius.all(100),
                    fit="fitWidth"
                ),
            shape=BoxShape.CIRCLE,
            width=200,
            height=200
        ),
            Container(
                content=Text("Hello!",color="white",size=25,weight="w900"),
                alignment=alignment.bottom_left,

            )
        ],
        width=200,
        height=200
)