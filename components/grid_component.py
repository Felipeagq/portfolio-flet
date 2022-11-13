from flet import (
    Container,
    UserControl,
    colors,
    Row,
    border_radius
)



class GridComponent(UserControl):
    def __init__(self,component):
        super().__init__()
        self.component = component
    
    def build(self):
        return Container(
            Row(
                self.component,
                wrap=True,
                run_spacing=50,
                width=1500,
                alignment="spaceEvenly",
                ),
            bgcolor=colors.WHITE24,
            border_radius=border_radius.all(25)
        )