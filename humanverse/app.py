"""
We read and write poetry because we are members of the human race.
"""
import asyncio

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW

text = """
Oh me! Oh life! of the questions of these recurring,
Of the endless trains of the faithless, of cities fill’d with the foolish,
Of myself forever reproaching myself, (for who more foolish than I, and who more faithless?)
Of eyes that vainly crave the light, of the objects mean, of the struggle ever renew’d,
Of the poor results of all, of the plodding and sordid crowds I see around me,
Of the empty and useless years of the rest, with the rest me intertwined,
The question, O me! so sad, recurring—What good amid these, O me, O life?

                                       Answer.
That you are here—that life exists and identity,
That the powerful play goes on, and you may contribute a verse.
"""


class HumanVerse(toga.App):
    async def fetch_poem(self, app):

        await asyncio.sleep(5)
        self.poetry_box.value = text

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()
        main_box.style.update(direction=COLUMN, padding_top=10)
        self.poetry_box = toga.MultilineTextInput(
            readonly=True,
            style=Pack(
                flex=1, padding=(10, 10, 10, 10), font_size=42, font_family="Helvetica"
            ),
        )
        self.poetry_box.value = "Loading..."

        main_box.add(self.poetry_box)

        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()

        self.add_background_task(self.fetch_poem)


def main():
    return HumanVerse("Human. Verse.", "com.humanverse.humanverse")
