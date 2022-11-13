from flet import (
    UserControl,
    Stack,
    Container,
    border_radius,
    Text,
    Image,
    alignment,
    animation,
)
from flet.types import BoxShape
from utils.utils import ScaleUp


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
            height=500,
            animate_scale=animation.Animation(800,"bounceOut"),
        ),
            Container(
                content=Text("Hello!",color="white",size=25,weight="w900"),
                alignment=alignment.bottom_left,
                animate_scale=animation.Animation(800,"bounceOut"),
                on_hover= lambda x: ScaleUp(x,1.1)

            )
        ],
        width=350,
        height=350
)