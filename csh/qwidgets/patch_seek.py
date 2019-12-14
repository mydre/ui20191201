from PyQt5.QtWidgets import QWidget
from csh.qwidgets.patch import Patch


class PatchSeek(QWidget, Patch):

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type qwidgets
        """
        super(PatchSeek, self).__init__(parent)
        self.setupUi(self)
