import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

import elhamal 1.0

ColumnLayout {
    id: root
    anchors.fill: parent
    anchors.margins: 20

    Decryptor {
        id: decryptor
    }

    Button {
        Layout.fillWidth: true
        text: qsTr("Вставить ключи")
        onClicked: decryptor.pasteKeysFromClipboard()
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("P")
    }
    TextField {
        Layout.fillWidth: true
        text: decryptor.p
        placeholderText: qsTr("Введите P")
        onEditingFinished: decryptor.p = parseInt(text)
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("G")
    }
    TextField {
        Layout.fillWidth: true
        text: decryptor.g
        placeholderText: qsTr("Введите G")
        onEditingFinished: decryptor.g = parseInt(text) || 0
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("Y")
    }
    TextField {
        Layout.fillWidth: true
        text: decryptor.y
        placeholderText: qsTr("Введите Y")
        onEditingFinished: decryptor.y = parseInt(text) || 0
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("X")
    }
    TextField {
        Layout.fillWidth: true
        text: decryptor.x
        placeholderText: qsTr("Введите X")
        onEditingFinished: decryptor.x = parseInt(text)
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("Криптограмма")
    }
    TextField {
        Layout.fillWidth: true
        text: decryptor.encryptedMessage
        placeholderText: qsTr("Введите криптограмму")
        onEditingFinished: decryptor.encryptedMessage = text
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("Исходное сообщение")
    }
    TextField {
        Layout.fillWidth: true
        text: decryptor.sourceMessage
        placeholderText: qsTr("Исходное сообщение")
        readOnly: true
        selectByMouse: true
    }

}
