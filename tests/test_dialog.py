from .setup import TestPygletGUI

from pyglet_gui.widgets import Widget
from pyglet_gui.dialog import Dialog

import pyglet_gui.constants


class TestDialog(TestPygletGUI):
    """
    This test case tests basic functionality of
    viewer+dialog. We use an empty widget for this.
    """

    def setUp(self):
        super().setUp()

        self.widget = Widget(width=50, height=50)
        self.dialog = Dialog(self.widget, window=self.window, batch=self.batch, theme=self.theme)

    def test_top_down_draw(self):
        """
        Tests that the dialog's size was set
        according to the child size.
        """
        # dialog size is correct
        self.assertEqual(self.dialog.width, 50)
        self.assertEqual(self.dialog.height, 50)

        # widget is centered in the window
        self.assertEqual(self.widget.x, self.window.width/2 - self.widget.width/2)
        self.assertEqual(self.widget.y, self.window.height/2 - self.widget.height/2)

    def test_bottom_up_draw(self):
        """
        Tests that the dialog's size is modified
        if we set a new size to the widget.
        """
        self.widget.width = 60
        self.widget.parent.reset_size()

        # dialog size was reset
        self.assertEqual(self.dialog.width, self.widget.width)

        # widget and dialog were re-centered in the window
        self.assertEqual(self.widget.x, self.window.width/2 - self.widget.width/2)
        self.assertEqual(self.dialog.x, self.window.width/2 - self.dialog.width/2)

    def test_substitute_widget(self):
        """
        Tests substitution of dialog's content
        by other widget.
        """
        self.new_widget = Widget(width=60, height=50)

        self.dialog.content = self.new_widget

        self.assertTrue(not self.widget.has_manager())
        self.assertTrue(self.new_widget.has_manager())

        # dialog size was reset, new widget position is correct
        self.assertEqual(self.dialog.width, self.new_widget.width)
        self.assertEqual(self.new_widget.x, self.window.width/2 - self.new_widget.width/2)

    def test_window_resize(self):
        self.window.width = 100
        self.dialog.on_resize(self.window.width, self.window.height)

        # dialog size didn't changed.
        self.assertEqual(self.dialog.width, 50)

        # dialog is still centered.
        self.assertEqual(self.dialog.x, self.window.width/2 - self.dialog.width/2)

    def test_change_offset(self):
        self.dialog.offset = (10, 0)

        # dialog is still centered.
        self.assertEqual(self.dialog.x - 10, self.window.width/2 - self.dialog.width/2)

    def test_change_anchor(self):
        self.dialog.anchor = pyglet_gui.constants.ANCHOR_TOP_LEFT

        # dialog is still centered.
        self.assertEqual(self.dialog.x, 0)


    def test_deletion(self):
        self.dialog.delete()

        # confirm that widget is also deleted
        self.assertTrue(not self.widget.has_manager())

    def tearDown(self):
        self.dialog.delete()
        super().tearDown()

if __name__ == "__main__":
    import unittest
    unittest.main()