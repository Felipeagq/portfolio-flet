from flet import (
    Column,
    Row,
    UserControl,
    Text,
    Container,
    ListTile,
    Icon,
    icons,
    margin,
    animation
)

from utils.utils import ScaleUp


class ItemComponent(UserControl):
    
    def __init__(self,icono,titulo,subtitulo):
        super().__init__()
        self.icono =icono
        self.titulo = titulo
        self.subtitulo = subtitulo
    
    def build(self):
        return Container(ListTile(
                leading=Icon(self.icono),
                title=Text(self.titulo),
                subtitle=Text(self.subtitulo)
                ),
                margin=margin.only(top=25,bottom=25),
                            on_hover= lambda x : ScaleUp(x,1.3),
            animate_scale=animation.Animation(800,"bounceOut"),
                )



class HistoryComponentEducate(UserControl):
    
    def build(self):
        return Container(
            Column([
                ItemComponent(
                    icons.OFFLINE_BOLT_OUTLINED,
                    "Ingenieria Mecatronica",
                    "Universidad Autonoma del caribe UAC"),
            ]),
                # on_hover= lambda x : ScaleUp(x,1.3),
                # animate_scale=animation.Animation(800,"bounceOut"),
            width=600
        )


class HistoryComponentWork(UserControl):
    
    def build(self):
        return Container(
            Column([
                ItemComponent(
                    icons.OFFLINE_BOLT_OUTLINED,
                    "LA Electronic SAS",
                    "Project Manager, BackEnd Developer and DevOps"),
                ItemComponent(
                    icons.OFFLINE_BOLT_OUTLINED,
                    "Neero SAS",
                    "Project Manager and DevOps"),
                ItemComponent(
                    icons.OFFLINE_BOLT_OUTLINED,
                    "Tata Consulting services TCS",
                    "DevOps"),
            ]),
                # on_hover= lambda x : ScaleUp(x,1.3),
                # animate_scale=animation.Animation(800,"bounceOut"),
            width=600
        )