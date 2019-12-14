from PyQt5.QtWidgets import QWidget
from csh.qwidgets.multiple_parameters import MultipleParameters


class MultipleParametersSeek(QWidget, MultipleParameters):

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type qwidgets
        """
        super(MultipleParametersSeek, self).__init__(parent)
        self.setupUi(self)
