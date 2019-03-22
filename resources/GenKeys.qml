import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

ColumnLayout {
    id: root
    anchors.fill: parent

    Button {
        Layout.fillWidth: true
        text: qsTr('Сгенерировать ключи')
    }
}