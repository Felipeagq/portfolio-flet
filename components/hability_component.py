from flet import (
    Container,
    Column,
    Icon,
    Text,
    UserControl,
    padding,
    margin,
    colors,
    Row,
    animation,
    icons
)

from utils.utils import ScaleUp




class HabilityComponent(UserControl):
    def __init__(self,icono,titulo,texto):
        super().__init__()
        self.icono = icono
        self.titulo = titulo
        self.texto = texto
    
    def build(self):
        return Container(
            Column([
                Container(
                    Icon(self.icono,
                        color=colors.BLACK,
                        size=40),
                ),
                Container(
                    Text(self.titulo,
                        color=colors.BLACK),
                ),
                Container(
                    Text(self.texto,
                        text_align="center",
                        color=colors.BLACK
                        ),
                    
                ),
            ],alignment="spaceEvenly",
            horizontal_alignment="center"),
            width=300,
            height=300,
            # bgcolor=colors.BLACK45,
            margin=margin.all(50),
            on_hover= lambda x: ScaleUp(x,1.2),
            animate_scale= animation.Animation(800,"bounceOut")
        )
