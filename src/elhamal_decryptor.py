from .elhamal_encryptor import ElHamal

from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot
from PyQt5.QtGui import QClipboard, QGuiApplication


class ElHamalDecryptor(QObject):
    keyChanged = pyqtSignal()
    encryptedMessageChanged = pyqtSignal()
    sourceMessageChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._p = 0
        self._g = 0
        self._y = 0
        self._x = 0
        self._encryptedMessage = ""
        self._sourceMessage = ""
        self._clipboard = QGuiApplication.clipboard()

    @pyqtSlot()
    def pasteEncryptedMessageFromClipboard(self):
        self.encryptedMessage = self._clipboard.text(QClipboard.Clipboard)

    @pyqtSlot()
    def pasteKeysFromClipboard(self):
        keys = self._clipboard.text(QClipboard.Clipboard).split(' ')
        if len(keys) >= 4 and all(x.isalnum() for x in keys):
            keys = [int(x) for x in keys]
            self.p, self.g, self.y, self.x = keys[:4]

    @pyqtSlot()
    def copySourceMessageToClipboard(self):
        self._clipboard.setText(self._sourceMessage, QClipboard.Clipboard)

    @pyqtProperty(int, notify=keyChanged)
    def p(self) -> int:
        return self._p

    @pyqtProperty(int, notify=keyChanged)
    def g(self) -> int:
        return self._g

    @pyqtProperty(int, notify=keyChanged)
    def y(self) -> int:
        return self._y

    @pyqtProperty(int, notify=keyChanged)
    def x(self) -> int:
        return self._x

    @pyqtProperty(str, notify=keyChanged)
    def sourceMessage(self) -> str:
        self.decryptMessage()
        return self._sourceMessage

    @pyqtProperty(str, notify=keyChanged)
    def encryptedMessage(self) -> str:
        return self._encryptedMessage

    @p.setter
    def p(self, p):
        self._p = p
        self.keyChanged.emit()
        self.sourceMessageChanged()

    @g.setter
    def g(self, g):
        self._g = g
        self.keyChanged.emit()
        self.sourceMessageChanged()

    @y.setter
    def y(self, y):
        self._y = y
        self.keyChanged.emit()
        self.sourceMessageChanged()

    @x.setter
    def x(self, x):
        self._x = x
        self.keyChanged.emit()
        self.sourceMessageChanged()

    @encryptedMessage.setter
    def encryptedMessage(self, encryptedMessage):
        self._encryptedMessage = encryptedMessage
        self.encryptedMessageChanged.emit()
        self.sourceMessageChanged.emit()

    def decryptMessage(self):
        keys = [self._p, self._g, self._y, self._x]
        result = ''
        try:
            cryptogram = ElHamal.cryptogram_from_string(self._encryptedMessage)
            result = ElHamal.decrypt(cryptogram, keys)
        except:
            result = 'error'
        self._sourceMessage = result

