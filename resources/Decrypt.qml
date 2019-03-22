import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

ColumnLayout {
    id: root
    anchors.fill: parent

    Label {
        Layout.fillWidth: true
        text: qsTr('Расшифровка')
    }
}
