"""
File         : components.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 01-Nov-2021
"""

import toga

from toga.style import Pack


# ---------------------------------------------------------------------------------------------------------------------

class EpisodeTable(toga.Table):

    def __init__(
        self,
        headings=['Name', 'Date', 'Length', 'Status', 'Action'],
        id=None,
        style=Pack(flex=1),
        data=None,
        accessors=None,
        multiple_select=False,
        on_select=None,
        on_double_click=None,
        missing_value=None,
        factory=None
    ):
        super().__init__(headings, id=id, style=style, data=data, accessors=accessors, multiple_select=multiple_select, on_select=on_select, on_double_click=on_double_click, missing_value=missing_value, factory=factory)
