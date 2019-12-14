from PyQt5.QtWidgets import QWidget
from csh.qwidgets.jtk_point import JtkPoint


class JtkPointSeek(QWidget, JtkPoint):

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type qwidgets
        """
        super(JtkPointSeek, self).__init__(parent)
        self.setupUi(self)
