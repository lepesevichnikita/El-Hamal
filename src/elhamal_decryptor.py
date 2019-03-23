from .elhamal_encryptor import ElHamal

from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot
from PyQt5.QtGui import QClipboard, QGuiApplication


class ElHamalDecryptor(QObject):
    keysChanged = pyqtSignal()
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
            self._p, self._g, self._y, self._x = keys[:4]
            self.keysChanged.emit()
            self.sourceMessageChanged.emit()

    @pyqtSlot()
    def copySourceMessageToClipboard(self):
        self._clipboard.setText(self._sourceMessage, QClipboard.Clipboard)

    @pyqtProperty(int, notify=keysChanged)
    def p(self) -> int:
        return self._p

    @pyqtProperty(int, notify=keysChanged)
    def g(self) -> int:
        return self._g

    @pyqtProperty(int, notify=keysChanged)
    def y(self) -> int:
        return self._y

    @pyqtProperty(int, notify=keysChanged)
    def x(self) -> int:
        return self._x

    @pyqtProperty(str, notify=sourceMessageChanged)
    def sourceMessage(self) -> str:
        self.decryptMessage()
        return self._sourceMessage

    @pyqtProperty(str, notify=encryptedMessageChanged)
    def encryptedMessage(self) -> str:
        return self._encryptedMessage

    @p.setter
    def p(self, p):
        self._p = p
        self.keysChanged.emit()
        self.sourceMessageChanged.emit()

    @g.setter
    def g(self, g):
        self._g = g
        self.keysChanged.emit()
        self.sourceMessageChanged.emit()

    @y.setter
    def y(self, y):
        self._y = y
        self.keysChanged.emit()
        self.sourceMessageChanged.emit()

    @x.setter
    def x(self, x):
        self._x = x
        self.keysChanged.emit()
        self.sourceMessageChanged.emit()

    @encryptedMessage.setter
    def encryptedMessage(self, encryptedMessage):
        self._encryptedMessage = encryptedMessage
        self.encryptedMessageChanged.emit()
        self.sourceMessageChanged.emit()

    def decryptMessage(self):
        keys = [self._p, self._g, self._y, self._x]
        result = ''
        if all(x >= 0 for x in keys) and len(self._encryptedMessage) > 0:
            try:
                cryptogram = ElHamal.cryptogram_from_string(
                    self._encryptedMessage)
                result = ElHamal.decrypt(cryptogram, keys)
            except Exception as e:
                print(str(e))
                result = 'error'
        self._sourceMessage = result
