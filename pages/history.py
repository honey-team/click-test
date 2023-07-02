import sqlite3

import flet as ft

from utils.constants import set_appbar


def init_history(page: ft.Page):
    set_appbar(page, 'history')
    page.update()

    def get_history():
        cn = sqlite3.connect('history.db')
        cr = cn.cursor()

        cr.execute('SELECT * FROM history')
        rows = cr.fetchall()
        return rows

    rows = get_history()

    datarows = []

    for clicks, cps, time in rows[::-1]:
        datarows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(clicks)),
                    ft.DataCell(ft.Text(cps)),
                    ft.DataCell(ft.Text(time)),
                ]
            )
        )

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text('Клики'), numeric=True),
            ft.DataColumn(ft.Text('Средний КПС'), numeric=True),
            ft.DataColumn(ft.Text('Время'), numeric=True),
        ],
        rows=datarows,
    )
    lv = ft.ListView([table], expand=True, spacing=10)
    page.add(lv)
