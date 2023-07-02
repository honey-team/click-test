from typing import Literal, Callable

import flet as ft

import utils.colors as clr

# Page settings
WIN_SIZE = [800, 600] # height, width
WIN_RESIZABLE = False
WIN_MAXIMIZABLE = False
WIN_VERTICAL_ALIGN = ft.MainAxisAlignment.CENTER
WIN_HORIZONTAL_ALIGN = ft.MainAxisAlignment.CENTER

THEME = ft.Theme(
    color_scheme=ft.ColorScheme(primary=ft.colors.GREEN, primary_container=ft.colors.GREEN_200)
)
NAVIGATION_BAR = ft.NavigationBar(
    destinations=[
        ft.NavigationDestination(
            icon=ft.icons.MOUSE_OUTLINED, selected_icon=ft.icons.MOUSE, label='Click'
        ),
        ft.NavigationDestination(icon=ft.icons.HISTORY, label='History'),
        ft.NavigationDestination(icon=ft.icons.SETTINGS, label='Settings'),
    ],
    selected_index=0,
)

# Program
TIMES = [1, 2, 5, 10, 30, 60]  # seconds

# Views
HORIZONTAL_DIVIDER = HDIVIDER = ft.Divider(visible=True)

# Functions
def set_appbar(page: ft.Page, name: Literal['clicker', 'history', 'settings'], get_items_for_appbar: Callable = None):
    if name == 'clicker':
        page.appbar = ft.AppBar(
            title=ft.Text('Click test'),
            center_title=False,
            bgcolor=clr.appbar(page),
            actions=[ft.PopupMenuButton(items=get_items_for_appbar())],
        )
    else:
        page.appbar = ft.AppBar(
        title=ft.Text('Click test'),
        center_title=False,
        bgcolor=clr.appbar(page),
    )

# BUGFIX
def synthetic_event(page: ft.Page, control: ft.NavigationBar):
    control.on_change(
        ft.ControlEvent(
            target=control.uid,
            name="change",
            data=str(control.selected_index),
            control=control,
            page=page,
        )
    )
