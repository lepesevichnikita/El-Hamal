import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

import elhamal 1.0

ColumnLayout {
    id: root
    anchors.fill: parent

    KeysGenerator {
        id: keysGenerator
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("P")
    }
    TextField {
        Layout.fillWidth: true
        id: p
        text: keysGenerator.p
        placeholderText: qsTr("P")
        readOnly: true
        selectByMouse: true
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("G")
    }
    TextField {
        Layout.fillWidth: true
        id: g
        text: keysGenerator.g
        placeholderText: qsTr("G")
        readOnly: true
        selectByMouse: true
    }

    Label {
        Layout.fillWidth: true
        text: qsTr("Y")
    }
    TextField {
        Layout.fillWidth: true
        id: y
        text: keysGenerator.y
        placeholderText: qsTr("Y")
        readOnly: true
        selectByMouse: true
    }

    Layout.fillWidth: true
    Label {
        Layout.fillWidth: true
        text: qsTr("X")
    }
    TextField {
        Layout.fillWidth: true
        id: x
        text: keysGenerator.x
        placeholderText: qsTr("X")
        readOnly: true
        selectByMouse: true
    }

    Button {
        Layout.fillWidth: true
        text: qsTr("Сгенерировать ключи")
        onClicked: keysGenerator.genKeys()
    }
    Button {
        Layout.fillWidth: true
        text: qsTr("Скопировать ключи")
        onClicked: keysGenerator.copyKeysToClipboard()
    }
}