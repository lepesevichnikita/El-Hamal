import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

import elhamal 1.0

ColumnLayout {

    anchors.fill: parent
    anchors.margins: 20

    Encryptor {
        id: encryptor
    }

    Button {
        Layout.fillWidth: true
        text: qsTr("Вставить ключи")
        onClicked: encryptor.pasteKeysFromClipboard()
    }

    RowLayout {
        Label {
            Layout.fillWidth: true
            text: qsTr("P")
        }
        TextField {
            Layout.fillWidth: true

            text: encryptor.p
            placeholderText: qsTr("Введите P")
            onEditingFinished: {
                encryptor.p = parseInt(text) || 0
                print("p: ", encryptor.p)
            }
        }
    }

    RowLayout {
        Label {
            Layout.fillWidth: true
            text: qsTr("G")
        }

        TextField {
            Layout.fillWidth: true

            text: encryptor.g
            placeholderText: qsTr("Введите G")
            onEditingFinished: {
                encryptor.g = parseInt(text) || 0
                print("g: ", encryptor.g)
            }
        }
    }

    RowLayout {
        Label {
            Layout.fillWidth: true
            text: qsTr("Y")
        }

        TextField {
            Layout.fillWidth: true

            text: encryptor.y
            placeholderText: qsTr("Введите Y")
            onEditingFinished: {
                encryptor.y = parseInt(text) || 0
                print("y: ", encryptor.y)
            }
        }
    }

    RowLayout {
        Label {
            Layout.fillWidth: true
            text: qsTr("Текст для зашифровки")
        }

        TextField {
            Layout.fillWidth: true

            text: encryptor.sourceMessage
            placeholderText: qsTr("Введите текст для зашифровки")
            onEditingFinished: {
                encryptor.sourceMessage = text
                print("source message: ", encryptor.sourceMessage)
            }
        }
    }

    RowLayout {
        Label {
            Layout.fillWidth: true
            text: qsTr("Зашифрованный текст")
        }

        TextField {
            Layout.fillWidth: true

            text: encryptor.encryptedMessage
            placeholderText: qsTr("Ваш зашифрованный текст")
            readOnly: true
            selectByMouse: true
        }
    }

    RowLayout {
        Button {
            Layout.fillWidth: true
            text: qsTr("Скопировать криптограмму")
            onClicked: encrypt.copyCryptogramToClipboard()
        }
    }
}
