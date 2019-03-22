from .elhamal import ElHamal

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtCore import pyqtProperty


class ElHamalEncryptor(QObject):
    keyChanged = pyqtSignal()
    sourceMessageChanged = pyqtSignal()
    encryptedMessageChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._p = 0
        self._g = 0
        self._y = 0
        self._source_message = ""

    @pyqtProperty(int, notify=keyChanged)
    def p(self):
        return self._p

    @pyqtProperty(int, notify=keyChanged)
    def g(self):
        return self._g

    @pyqtProperty(int, notify=keyChanged)
    def y(self):
        return self._y

    @pyqtProperty(str, notify=sourceMessageChanged)
    def sourceMessage(self):
        return self._source_message

    @pyqtProperty(str, notify=encryptedMessageChanged)
    def encryptedMessage(self):
        keys = [self._p, self._g, self._y]
        result = ''
        if len(self._source_message) > 0:
            try:
                cryptogram = ElHamal.encrypt(self._source_message, keys)
                result = ElHamal.cryptogram_to_str(cryptogram)
            except:
                result = 'error'
        return result

    @p.setter
    def p(self, p):
        self._p = p or 0
        self.keyChanged.emit()
        self.encryptedMessageChanged.emit()

    @g.setter
    def g(self, g):
        self._g = g or 0
        self.keyChanged.emit()
        self.encryptedMessageChanged.emit()

    @y.setter
    def y(self, y):
        self._y = y or 0
        self.keyChanged.emit()
        self.encryptedMessageChanged.emit()

    @sourceMessage.setter
    def sourceMessage(self, source_message):
        self._source_message = source_message or ""
        self.sourceMessageChanged.emit()
        self.encryptedMessageChanged.emit()
