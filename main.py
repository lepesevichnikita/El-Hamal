#!/bin/python3
import sys

import PyQt5.QtCore

from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType, QQmlComponent
from PyQt5.QtQuick import QQuickView
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QDirIterator, QUrl, qInstallMessageHandler

from src import ElHamalEncryptor, ElHamalDecryptor

import resources_rc

def handleStatusChange(mode, message, context):
    print(message, context)

def main():
    mainView = "qrc:///main.qml"
    application = QGuiApplication(sys.argv)
    qmlRegisterType(ElHamalEncryptor, 'elhamal', 1, 0, 'Encryptor')
    qmlRegisterType(ElHamalDecryptor, 'elhamal', 1, 0, 'Decryptor')
    qInstallMessageHandler(handleStatusChange)

    engine = QQmlApplicationEngine()

    it = QDirIterator(":", QDirIterator.Subdirectories)
    while it.hasNext():
        print(it.next())

    engine.load(QUrl(mainView))
    engine.rootObjects()[0].show()
    sys.exit(application.exec_())


entry_point = {
    '__main__': main
}

entry_point[__name__]()
