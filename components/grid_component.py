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
                    Icon(self.icono),
                ),
                Container(
                    Text(self.titulo),
                ),
                Container(
                    Text(self.texto,
                        text_align="center"),
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





class GridComponent(UserControl):
    # def __init__(self,component):
    #     super().__init__()
    #     self.component = component
    
    def build(self):
        return Container(
            Row([
                HabilityComponent(
                    icons.MANAGE_ACCOUNTS,
                    "Project Manager",
                    "Todo en la vida tiene un orden, incluso los proyectos"
                    ),
                HabilityComponent(
                    icons.STORAGE_OUTLINED,
                    "BackEnd Development",
                    "Gestion de la logica de negocio de un proyecto y base de datos"
                    ),
                HabilityComponent(
                    icons.COMPUTER_SHARP,
                    "DevOps",
                    "Despliegue de proyectos con tecnologias en la vanguardia"
                    ),

            ],
                wrap=True,
                run_spacing=50,
                width=1500,
                alignment="center",

                ),
            bgcolor=colors.BLACK38
        )