from flet import (
    Row,
    Container,
    Image,
    UserControl,
    padding,
    animation
)

from utils.utils import ScaleUp

class IconComponents(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
    
    def build(self):
        return Row(
            [
                Container(
                    Image(src="/assets/instagram.png",),
                    width=50,
                    ink=True,
                    on_click= lambda e: self.page.launch_url("https://www.instagram.com/felipeagq_/")
                ),
                Container(
                    Image(src="/assets/linkedin.png"),
                    width=50,
                    on_click=lambda e: self.page.launch_url("https://www.linkedin.com/in/felipeagq/")
                ),
            ],
            alignment="center"
        )



class IconComponentsTwo(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
    
    def build(self):
        return Row(
            controls=[
                Container(
                    Row([
                        Container(
                            Image(src="/assets/instagram.png",),
                            width=50,
                            ink=True,
                            on_click= lambda e: self.page.launch_url("https://www.instagram.com/felipeagq_/"),
                            on_hover= lambda x : ScaleUp(x,1.5),
                            animate_scale= animation.Animation(800,"bounceOut")
                        ),
                        Container(
                            Image(src="/assets/linkedin.png"),
                            width=50,
                            on_click=lambda e: self.page.launch_url("https://www.linkedin.com/in/felipeagq/"),
                            on_hover= lambda x : ScaleUp(x,1.5),
                            animate_scale= animation.Animation(800,"bounceOut")
                        ),
                    ],
                    spacing=50),
                    padding=padding.only(top=130),
                    # on_hover= lambda x : ScaleUp(x),
                    # animate= animation.Animation(800,"bounceOut")
                ),
            ],
            alignment="center",
        )