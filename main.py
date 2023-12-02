from flet import * 
import pyqrcode 
import png 
from pyqrcode import QRCode 
from time import sleep

def main(page: Page):
    page.title = "Aditya's QR code generator"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme = Theme("green")
    page.theme_mode = ThemeMode.DARK
    page.appbar=AppBar(

        leading=Icon(icons.QR_CODE_SCANNER),
        leading_width=30,
        title=Text("QR code generator"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,)

    

    def generate(e):
        url = pyqrcode.create(inp.value) 
        url.png(f'{inp.value[:5]}.png', scale = 6) 
        t1 = Text("generating...")
        page.add(t1)
        sleep(1)
        t2 = Text("generating done!")
        qrcode = Image(src=f"./{inp.value[:5]}.png",tooltip=inp.value)
        page.add(t2,qrcode)
        
        page.update()
        
    
    inp = TextField(label="enter url here")
    btn = FilledButton("generate now",on_click=lambda e:generate(e))

    page.add(
        Row(
            [inp,btn],
            alignment="center",
        ))
    
app(main,view=AppView.FLET_APP_WEB)
