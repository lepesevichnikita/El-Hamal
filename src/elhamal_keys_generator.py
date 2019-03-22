from .elhamal import ElHamal

from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal
from PyQt5.QtGui import QClipboard, QGuiApplication


class ElHamalKeysGenerator(QObject):
    keysChanged = pyqtSignal()
    keysDefaultValue = [0] * 4

    def __init__(self, parent=None):
        super().__init__(parent)
        self._elhamal = ElHamal()
        self._keys = self.keysDefaultValue
        self._clipboard = QGuiApplication.clipboard()

    @pyqtSlot()
    def genKeys(self):
        self._keys = self._elhamal.gen_keys()
        self.keysChanged.emit()

    @pyqtSlot()
    def copyKeysToClipboard(self):
        keys = ' '.join([str(x) for x in self._keys])
        self._clipboard.setText(keys, QClipboard.Clipboard)
        self._clipboard.setText(keys, QClipboard.Selection)

    @pyqtProperty(int, notify=keysChanged, freset=genKeys)
    def p(self):
        return self._keys[0] or 0

    @pyqtProperty(int, notify=keysChanged, freset=genKeys)
    def g(self):
        return self._keys[1] or 0

    @pyqtProperty(int, notify=keysChanged, freset=genKeys)
    def y(self):
        return self._keys[2] or 0

    @pyqtProperty(int, notify=keysChanged, freset=genKeys)
    def x(self):
        return self._keys[3] or 0
