import flet as ft
from flet import *

def _input_froms(pg: ft.Page):
    pg.title = 'Заявки'
    pg.add(ft.Text(value='Заявки'))



if __name__ == '__main__':
    ft.app(target=_input_froms, view=WEB_BROWSER)