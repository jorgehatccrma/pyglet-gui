from .setup import TestPygletGUI

from pyglet_gui.containers import HorizontalLayout, VerticalLayout
from pyglet_gui.widgets import Spacer, Widget
from pyglet_gui.dialog import Dialog


class TestSpacer(TestPygletGUI):
    """
    Tests that the spacer is working correctly
    inside containers.
    """
    def setUp(self):
        TestPygletGUI.setUp(self)

        self.widgets = []
        for i in range(2):
            self.widgets.append(Widget(width=100, height=50))
        for i in range(2):
            self.widgets.append(Widget(width=20, height=50))

        self.container = VerticalLayout([HorizontalLayout([self.widgets[0],
                                                           self.widgets[1]], padding=0),
                                         HorizontalLayout([Spacer(),
                                                           self.widgets[2],
                                                           Spacer(),
                                                           self.widgets[3],
                                                           Spacer()], padding=0)], padding=0)

        self.dialog = Dialog(self.container, window=self.window, batch=self.batch, theme=self.theme)

    def test_initial(self):
        self.assertEqual(self.container.width, 200)

        # space left for the spacers occupy:
        width_left = 200 - 40

        # expected spacer size
        spacer_size = int(width_left/3.)

        # Spacers should occupy same space
        self.assertEqual(self.widgets[2].x, self.container.x + spacer_size)
        self.assertEqual(self.widgets[3].x, self.widgets[2].x + self.widgets[2].width + spacer_size)

    def tearDown(self):
        self.dialog.delete()
        super().tearDown()

if __name__ == "__main__":
    import unittest
    unittest.main()
