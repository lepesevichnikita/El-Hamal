#!/bin/python3
import sys

import PyQt5.QtCore

from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QDirIterator, QUrl, qInstallMessageHandler
from PyQt5.QtQuick import QQuickView

from src import ElHamalEncryptor, ElHamalDecryptor, ElHamalKeysGenerator

import resources_rc


def handleStatusChange(mode, message, context):
    print(message, context)

def main():
    mainView = "qrc:///main.qml"
    application = QGuiApplication(sys.argv)

    qmlRegisterType(ElHamalEncryptor, 'elhamal', 1, 0, 'Encryptor')
    qmlRegisterType(ElHamalDecryptor, 'elhamal', 1, 0, 'Decryptor')
    qmlRegisterType(ElHamalKeysGenerator, 'elhamal', 1, 0, 'KeysGenerator')

    qInstallMessageHandler(handleStatusChange)

    it = QDirIterator(":", QDirIterator.Subdirectories)
    while it.hasNext():
        print(it.next())

    view = QQuickView()
    view.setResizeMode(QQuickView.SizeViewToRootObject)
    view.setSource(QUrl(mainView))

    sys.exit(application.exec_())


entry_point = {
    '__main__': main
}

entry_point[__name__]()
