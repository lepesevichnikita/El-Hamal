import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

ApplicationWindow {
    property int buttonMinimumWidth: 100

    visible: true
    title: qsTr("El Hamal")
    minimumWidth: 480
    minimumHeight: 480

    onWidthChanged: print(width, height)
    onHeightChanged: print(width, height)

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

    ScrollView {
        anchors.fill: parent
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
        ScrollBar.vertical.policy: ScrollBar.AlwaysOn

        StackLayout {
            anchors.fill: parent
            anchors.margins: 20
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
}