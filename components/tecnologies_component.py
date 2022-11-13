from flet import (
    Container,
    Image,
    animation,
    UserControl,
    colors
)

from utils.utils import ScaleUp

class TecnologiesComponent(UserControl):
    def __init__(self,image):
        super().__init__()
        self.image = image 
    
    def build(self):
        return Container(
            Image(self.image),
            width=300,
            height=300,
            on_hover= lambda x:ScaleUp(x,1.3),
            animate_scale= animation.Animation(800,"bounceOut"),
        )