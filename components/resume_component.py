from flet import (
    Text,
    Row,
    colors,
    Container,
    UserControl,
)

class ResumeComponent(UserControl):
    
    def build(self):
        return Row(
            controls=[
                Container(
            content=Text(
            "Lover of cats, good coffee and elegant code, I have experience in BackEnd development with Pyhton, DevOps and AWS, I am creative and curious but at the same time methodical and analytical, I have the skills to work in a team and present optimal solutions in order to to seek the success of the company at the same time that I grow professionally.",
            size=17,
            weight="w500",
            color=colors.BLACK87,
            text_align="center",
            no_wrap=False,
        ),width=500
        )
            ],
            alignment="center",
            
        )