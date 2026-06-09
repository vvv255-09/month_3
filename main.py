import flet as ft
from datetime import datetime


def main_page(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = 'Мое первое приложение'

    text_hello = ft.Text(value='Hello World')

    history = []
    history_view = ft.Column()

    def render_history():
        history_view.controls = [ft.Text(item['message']) for item in history]

    def on_button_click(_):
        if name_input.value:
            name = name_input.value.strip()
            now = datetime.now().strftime('%Y:%m:%d - %H:%M:%S')
            message = f'{now} - Привет, {name}!'

            history.append({'name': name, 'message': message})
            render_history()

            text_hello.value = message
            text_hello.color = None
            name_input.value = None
        else:
            text_hello.value = 'enter name'
            text_hello.color = ft.Colors.RED
        page.update()

    def on_delete_last(_):
        if history:
            history.pop()         
            render_history()
            text_hello.value = 'Удалено последнее приветствие'
            text_hello.color = None
        else:
            text_hello.value = 'История пуста!'
            text_hello.color = ft.Colors.RED
        page.update()

    def on_sort(_):
        history.sort(key=lambda item: item['name'].lower())
        render_history()
        page.update()

    name_input = ft.TextField(on_submit=on_button_click)
    button_send = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_button_click)
    button_delete = ft.ElevatedButton('Удалить последнее', icon=ft.Icons.DELETE, on_click=on_delete_last)
    button_sort = ft.ElevatedButton('Сортировать по алфавиту', icon=ft.Icons.SORT, on_click=on_sort)

    page.add(
        text_hello,
        name_input,
        ft.Row([button_send, button_delete, button_sort]),
        ft.Divider(),
        ft.Text('История:'),
        history_view,
    )


ft.run(main_page)