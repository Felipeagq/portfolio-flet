from flet import (
    Column,
    Row,
    Text,
    Container,
    ListTile,
    Icon,
    icons,
    margin,
    animation,
    alignment
)

from utils.utils import ScaleUp


class ItemComponent(Column):

    def __init__(self, icono, titulo, subtitulo):
        super().__init__()
        self.icono = icono
        self.titulo = titulo
        self.subtitulo = subtitulo

    def build(self):
        return Container(ListTile(
            leading=Icon(self.icono,
                            color="black"),
            title=Text(self.titulo,
                            color="black"),
            subtitle=Text(self.subtitulo,
                            color="black"),
        ),
            # margin=margin.only(top=25,bottom=25),
            on_hover=lambda x: ScaleUp(x, 1.1),
            animate_scale=animation.Animation(800, "bounceOut"),
        )


class HistoryComponentEducate(Column):

    def build(self):
        return Container(
            Column([
                # Container(Text("EDUCATION", color="black", size=25,
                #         text_align="center", bgcolor="white")),
                ItemComponent(
                    icons.COLLECTIONS_BOOKMARK_OUTLINED,
                    "Ingenieria Mecatronica",
                    "Universidad Autonoma del caribe UAC (2017 -2022)",
                ),
            ],
                alignment="end",
            ),
            # on_hover= lambda x : ScaleUp(x,1.3),
            # animate_scale=animation.Animation(800,"bounceOut"),
            width=600
        )


class HistoryComponentWork(Column):

    def build(self):
        return Container(
            Column([
                # Container(Text("EXPERIENCE", color="black",
                #         size=25, text_align="center")),
                ItemComponent(
                    icons.TASK_ALT_OUTLINED,
                    "Project Manager, BackEnd Developer and DevOps",
                    "LA Electronic SAS (20 December 2020 - 01 Agoust 2022)"),
                ItemComponent(
                    icons.TASK_ALT_OUTLINED,
                    "Project Manager and DevOps",
                    "Neero SAS (01 Agoust 2022 - 01 October 2022)"),
                ItemComponent(
                    icons.ADD_TASK,
                    "DevOps",
                    "Tata Consulting services TCS (01 October 2022 - NowDays)"),
                ItemComponent(
                    icons.ADD_TASK,
                    "Co-Founder",
                    "FEANWare (September 2022)"),
            ]),
            # on_hover= lambda x : ScaleUp(x,1.3),
            # animate_scale=animation.Animation(800,"bounceOut"),
            width=600
        )
