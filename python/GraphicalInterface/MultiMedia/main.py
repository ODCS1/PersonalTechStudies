from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QSlider
)
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaDevices
from PySide6.QtMultimediaWidgets import QVideoWidget


class MediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Media Player")
        self.setGeometry(200, 100, 800, 600)

        # MEDIA PLAYER AND AUDIO OUTPUT
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)


        # CREATE AN INSTANCE OF QMEDIADEVICES
        self.media_devices = QMediaDevices()
        self.set_default_audio_device()

        # MONITOR CHANGES IN AVAILABLE AUDIO DEVICES
        self.media_devices.audioOutputsChanged.connect(self.on_audio_device_changed)

        # VIDEO WIDGET
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)


        # BUTTONS AND SLIDER
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")
        self.open_button = QPushButton("Open File")
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.sliderMoved.connect(self.set_position)

        self.play_button.clicked.connect(self.media_player.play)
        self.pause_button.clicked.connect(self.media_player.pause)
        self.stop_button.clicked.connect(self.media_player.stop)
        self.open_button.clicked.connect(self.open_file)


        # LAYOUT
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.slider)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.open_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


        # CONNECT SLIDER UPDATES
        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.durationChanged.connect(self.update_duration)

    def set_default_audio_device(self):
        """Set the default audio device."""
        default_device = QMediaDevices.defaultAudioOutput()
        self.audio_output.setDevice(default_device)

    def on_audio_device_changed(self):
        """Update the audio output device when devices change."""
        self.set_default_audio_device()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Media File")
        if file_name:
            self.media_player.setSource(file_name)
           
    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_slider(self, position):
        self.slider.setValue(position)

    def update_duration(self, duration):
        self.slider.setRange(0, duration)


if __name__ == "__main__":
    app = QApplication([])
    player = MediaPlayer()
    player.show()
    app.exec()