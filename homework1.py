import flet as ft

def main(page: ft.Page):
    page.title = 'Homework_1'
    page.theme_mode = ft.ThemeMode.LIGHT
    text = ft.Text(value='Light / Dark', color=ft.Colors.BLACK)

    def theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            text.color = ft.Colors.WHITE
            button.icon = ft.Icons.BRIGHTNESS_4
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            text.color = None
            button.icon = ft.Icons.BRIGHTNESS_7

        page.update()

    button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=theme)
    page.add(text, button)

ft.app(target=main, view=ft.WEB_BROWSER)