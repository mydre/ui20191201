from PyQt5.QtWidgets import QWidget
from csh.qwidgets.free_field_address import FreeFieldAddress


class FreeFieldAddressSeek(QWidget, FreeFieldAddress):

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type qwidgets
        """
        super(FreeFieldAddressSeek, self).__init__(parent)
        self.setupUi(self)
