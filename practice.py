import flet as ft
from datetime import datetime as dt

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value="Hello world", color=ft.Colors.BLACK)

    def on_button(e):
        now = dt.now().strftime("%d - %m - %Y    %H : %M : %S")
        print(name_input.value)
        if name_input.value:
            greeting_text.value = f'Hello {name_input.value} and time is now {now}'
            greeting_text.color = None
            name_input.value = None
        else:
            greeting_text.value = 'Enter correct name!'
            greeting_text.color = ft.Colors.RED
        page.update()

    name_input = ft.TextField(label='Enter your name', on_submit=on_button)
    button1 = ft.TextButton(text='sending', on_click=on_button)
    button2 = ft.ElevatedButton(text='send', on_click=on_button)
    button3 = ft.IconButton(icon=ft.Icons.ACCESS_ALARMS_ROUNDED, on_click=on_button)






    button4 = ft.TextButton(text='sending', on_click=on_button)
    button5 = ft.IconButton(icon=ft.Icons.ACCESSIBLE_FORWARD_SHARP, on_click=on_button)
    button6 = ft.ElevatedButton(text='send', on_click=on_button)


    page.add(greeting_text, name_input, button1, button2, button3, button4, button5, button6)

ft.app(target=main, view=ft.WEB_BROWSER)
