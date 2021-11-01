"""
Podcast desktop player
"""

import toga
import httpx
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class MintDeck(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        

        data = [
            ('root%s' % i, 'value %s' % i)
            for i in range(1, 100)
        ]
        left_container = toga.Table(
            headings=['col1', 'col2'], 
            data=data,
            # accessors=[self.col1]
            on_select=self.table_select
        )
        # left_container = toga.Table(headings=['Hello', 'World'], data=[(1, 2), (3, 4)])
        right_content = toga.Box(
            style=Pack(direction=COLUMN, padding_top=50)
        )
        input = toga.Switch('Switch')
        right_content.add(input)
        right_container = toga.ScrollContainer(horizontal=False)
        right_container.content = right_content
        split = toga.SplitContainer()
        split.content = [
            (left_container, 1),
            (right_container, 2)
        ]

        main_box.add(name_box)
        main_box.add(button)
        main_box.add(split)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def table_select(self, table, row):
        print('table select', table, row)
        print(table.data)
        print(table.data[0])
        print(table.selection)
        print(table.selection)
        print(dir(row))
        print(row)
        print(row.col1)
        print(row.col2)

    def say_hello(self, widget):
        if self.name_input.value:
            name = self.name_input.value
        else:
            name = 'stranger'

        response = httpx.get("https://jsonplaceholder.typicode.com/posts/42")
        payload = response.json()

        self.main_window.info_dialog(
            f'Hello, {name}',
            payload['body']
        )


def main():
    return MintDeck()
