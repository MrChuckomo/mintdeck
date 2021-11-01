"""
File         : app.py
Description  : Podcast desktop player

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 01-Nov-2021
"""

import toga
import httpx

from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from mintdeck.components import EpisodeTable

# ---------------------------------------------------------------------------------------------------------------------

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
        self.name_input = toga.TextInput(placeholder='Search', style=Pack(flex=1))

        button = toga.Button(
            'Search',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        name_box.add(button)

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
            style=Pack(direction=COLUMN, padding_top=5, background_color='red')
        )
        right_content.add(toga.Switch('Switch'))
        right_content.add(EpisodeTable(data=[('Foo', '2021-10-25', '01:24h', None, toga.Button('Add'))]))
        right_container = toga.ScrollContainer(horizontal=False)
        right_container.content = right_content
        split = toga.SplitContainer()
        split.content = [
            (left_container, 1),
            (right_container, 2)
        ]

        backw = toga.Button('back')
        play = toga.Button('play')
        forw = toga.Button('forw')
        start_label = toga.Label('00:00:00',style=Pack(padding=(0, 5)))
        end_label = toga.Label('00:00:00',style=Pack(padding=(0, 5)))
        progress = toga.ProgressBar(max=100, value=20, style=Pack(flex=1))
        # progress = toga.Slider(default=20, range=(1, 100))
        player_box = toga.Box(style=Pack(direction=ROW, padding=5, background_color='#898989'))
        player_box.add(backw)
        player_box.add(play)
        player_box.add(forw)
        player_box.add(start_label)
        player_box.add(progress)
        player_box.add(end_label)


        main_box.add(name_box)
        # main_box.add(button)
        main_box.add(player_box)
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
