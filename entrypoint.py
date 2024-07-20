import flet
from flet import (
    icons,
)
from flet import Page, colors, Column, Text, Container
from components.photo_stack import PhotoStack
from components.text_component import TextComponent
from components.resume_component import ResumeComponent
from components.icons_componentes import  IconComponentsTwo
from components.grid_component import GridComponent
from components.hability_component import HabilityComponent
from components.tecnologies_component import TecnologiesComponent
from components.history_component import HistoryComponentEducate, HistoryComponentWork


def main(page: Page):
    # Configuraciones    
    page.title = "Felipe Portfolio"
    page.padding = 50
    page.bgcolor = colors.BROWN_400
    page.scroll = "hidden"

    # page.add(Text("Hola"))
    # Componentes
    page.add(
        Column([
            Container(content=Column(
                
                controls=[
                    PhotoStack("image.png"),
                    TextComponent(),
                    ResumeComponent(),
                    # IconComponents(page),
                    IconComponentsTwo(page),
                    GridComponent([
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
                                #--
                    ]),
                    GridComponent([
                        HistoryComponentEducate(),
                        HistoryComponentWork()
                        ]),
                    GridComponent([
                        TecnologiesComponent("logo-teal.png"),
                        TecnologiesComponent("aws.png"),
                        TecnologiesComponent("flask-bg.png"),
                        TecnologiesComponent("trello.png"),
                        TecnologiesComponent("git.png"),
                        TecnologiesComponent("python.png"),
                        TecnologiesComponent("flet.png"),
                        TecnologiesComponent("drf.png"),
                        TecnologiesComponent("docker.png"),
                                #--
                    ])
                ],
                horizontal_alignment="center",
                spacing=55,
                # alignment="center",
                
            ),
            width=page.width
            # width=page.window_width
            )
        ],
    )
    )
    page.update()


if __name__ == "__main__":
    flet.app(target=main,
             assets_dir="assets",
            host="localhost",
            port=5000
            )
