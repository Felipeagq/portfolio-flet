import flet
from flet import Page, colors, Column, Text, Container
from components.photo_stack import PhotoStack
from components.text_component import TextComponent
from components.resume_component import ResumeComponent
from components.icons_componentes import IconComponents, IconComponentsTwo


def main(page: Page):
    # Configuraciones    
    page.title = "Felipe Portfolio"
    page.padding = 50
    page.bgcolor = colors.BROWN
    page.scroll = "hidden"

    # Componentes
    page.add(
        Column([
            Container(content=Column(
                controls=[
                    PhotoStack("/assets/felipe.jpeg"),
                    TextComponent(),
                    ResumeComponent(),
                    # IconComponents(page),
                    IconComponentsTwo(page),
                ],
                horizontal_alignment="center",
                spacing=55,
                alignment="center",
                
            ),
            width=page.width
            )
        ],
    )
    )
    page.update()


if __name__ == "__main__":
    flet.app(target=main,
            assets_dir="assets",
            view=flet.WEB_BROWSER,
            )
