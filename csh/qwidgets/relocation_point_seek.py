from PyQt5.QtWidgets import QWidget
from csh.qwidgets.relocation_point import RelocationPoint


class RelocationPointSeek(QWidget, RelocationPoint):

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type qwidgets
        """
        super(RelocationPointSeek, self).__init__(parent)
        self.setupUi(self)
