from PyQt5.QtWidgets import QWidget
from csh.qwidgets.self_carry_address import SelfCarryAddress


class SelfCarryAddressSeek(QWidget, SelfCarryAddress):

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type qwidgets
        """
        super(SelfCarryAddressSeek, self).__init__(parent)
        self.setupUi(self)
