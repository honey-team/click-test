import sqlite3

import flet as ft

import utils.colors as clr
import utils.settings_setter as wwsettings
from utils.constants import HDIVIDER, set_appbar
from utils.labels import DONT_WRITE_HISTORY, RESET_HISTORY, LIGHT_THEME, DARK_THEME, LINECHART, HISTORY, PERSONALIZATION, DEV, HISTORY_RESETED

def init_settings(page: ft.Page):
    set_appbar(page, 'settings')
    page.update()

    data = wwsettings.loadSettings()

    def change_page():
        if light_theme.value:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        light_theme.label = (
            LIGHT_THEME if page.theme_mode == ft.ThemeMode.LIGHT else DARK_THEME
        )

        set_appbar(page, 'settings')

        page.update()

    def change_settings(e=None):
        global data
        for i in (history_paused, light_theme, linechart):
            data = wwsettings.changeSetting(i.data, i.value)

        change_page()
        page.update()

    def reset_history_func(e):
        cn = sqlite3.connect('history.db')
        cr = cn.cursor()

        cr.execute('DELETE FROM history')
        cn.commit()

        page.snack_bar = ft.SnackBar(
            content=ft.Text(HISTORY_RESETED, color=clr.snackbar_text(page)),
            bgcolor=clr.snackbar(page),
        )
        page.snack_bar.open = True
        page.update()

    history_paused = ft.Switch(
        label=DONT_WRITE_HISTORY,
        value=data['history_paused'],
        on_change=change_settings,
        data='history_paused',
    )
    reset_history = ft.FilledButton(text=RESET_HISTORY, on_click=reset_history_func)

    light_theme = ft.Switch(
        label=LIGHT_THEME,
        value=data['light_theme'],
        on_change=change_settings,
        data='light_theme',
    )

    linechart = ft.Switch(
        label=LINECHART, value=data['linechart'], on_change=change_settings, data='linechart'
    )

    categories = {
        HISTORY: [history_paused, reset_history],
        PERSONALIZATION: [
            light_theme,
        ],
        DEV: [
            linechart,
        ],
    }

    def get_result():
        res = []
        for name, controls in categories.items():
            res.append(ft.Text(name))
            for i in controls:
                res.append(i)

            res.append(HDIVIDER)

        return res[:-1]

    page.add(*get_result())
