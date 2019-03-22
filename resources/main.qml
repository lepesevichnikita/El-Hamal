import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

ApplicationWindow {
    property int buttonMinimumWidth: 100

    visible: true
    title: qsTr("El Hamal")
    minimumWidth: 320
    minimumHeight: 640

    footer: TabBar {
        id: bar
        width: parent.width
        Repeater {
            model: ["Сгенерировать ключи", "Зашифровать", "Расшифровать"]

            TabButton {
                text: qsTr(modelData)
                width: Math.max(buttonMinimumWidth, bar.width/model.length)
            }
        }
    }

    StackLayout {
        anchors.fill: parent
        currentIndex: bar.currentIndex

        Item {
            GenKeys {}
        }

        Item {
            Encrypt {}
        }

        Item {
            Decrypt {}
        }
    }
}