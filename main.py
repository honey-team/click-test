import flet as ft
from pages.clicker import init_clicker
from pages.history import init_history
from pages.settings import init_settings
import utils.settings_setter as wwsettings
from utils.constants import WIN_SIZE, WIN_RESIZABLE, WIN_MAXIMIZABLE, WIN_VERTICAL_ALIGN, WIN_HORIZONTAL_ALIGN, THEME, NAVIGATION_BAR, synthetic_event

def main(page: ft.Page):
    def change(e: ft.ControlEvent):
        page.controls.clear()
        # page.update()

        match e.control.selected_index:
            case 0:
                init_clicker(page)
            case 1:
                init_history(page)
            case 2:
                init_settings(page)
        page.update()

    page.window_height, page.window_width = WIN_SIZE
    page.window_resizable = WIN_RESIZABLE
    page.window_maximizable = WIN_MAXIMIZABLE
    page.vertical_alignment = WIN_VERTICAL_ALIGN
    page.horizontal_alignment = WIN_HORIZONTAL_ALIGN

    page.theme = THEME
    page.navigation_bar = NAVIGATION_BAR
    page.navigation_bar.on_change = change
    page.navigation_bar.did_mount = lambda: synthetic_event(page=page, control=page.navigation_bar)

    if wwsettings.loadSettings()['light_theme']:
        page.theme_mode = ft.ThemeMode.LIGHT
    else:
        page.theme_mode = ft.ThemeMode.DARK

    page.window_center()

    page.update()

if __name__ == '__main__':
    ft.app(main)
