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

}
