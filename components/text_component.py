from flet import (
    Text,
    Row,
    colors,
    Container,
    UserControl,
    margin
)

class TextComponent(UserControl):
    
    def build(self):
        return Row(
            controls=[
                Container(
            content=Text(
            "My Name is",
            size=20,
            weight="w500",
            color=colors.BLACK87
        )
        ),
        Container(
            content=Text(
            "Felipe Andres Gonzalez Quintero",
            size=35,
            weight="w700",
            color=colors.BLACK87
        )
            # ,margin=margin.only(right=300)
        )
            ],
            alignment="center",
            
        )